from __future__ import annotations
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
from graphviz import Digraph
import streamlit as st
from dataclasses import dataclass
from pickle import dumps, loads  # per Streamlit
from antlr4.error.ErrorListener import ErrorListener

# Generador per les variables de tipus


def generador_lletres():
    for c in range(ord('a'), ord('z') + 1):
        yield chr(c)


lletres = generador_lletres()

# ----------------- Classe d'arbre semàntic ------------------------- #


class Buit:
    pass


@dataclass
class Node:
    index: int
    simbol: str
    esq: Arbre
    dre: Arbre
    tipus: str = ''


Arbre = Node | Buit

# ----------------- Funcions amb l'arbre ------------------------- #


def valorNode(a: Arbre):
    match a:
        case Buit():
            return (-1, "NONE")
        case Node():
            return (a.index, a.simbol)


def setTipus(a: Arbre, tipus: str):
    match a:
        case Node(i, s, e, d, t):
            return Node(i, s, e, d, tipus)


def esBuit(t: Arbre):
    match t:
        case Buit():
            return True
        case Node():
            return False

# type_table és el diccionari amb els tipus explícitament definits
# temporal_type_table és el diccionari amb símbols -> variables de tipus
# ('a', 'b', 'c'...)
def assignaTipus(t: Arbre, type_table: dict, temporal_type_table: dict):
    match t:
        case Node(ind, sim, l, r, tip):

            # Els diccionaris no tracten ni @ ni lambda
            if sim not in ['@', '\u03BB']:
                temp = False
                if sim not in type_table.keys():  # No te tipus ja definit
                    if sim not in temporal_type_table.keys():  # Tampoc te variable de tipus
                        temporal_type_table[sim] = next(lletres)
                    temp = True
                t = setTipus(
                    t, temporal_type_table[sim]) if temp else setTipus(
                    t, type_table[sim])
            else:
                t = setTipus(t, next(lletres))

            le = assignaTipus(l, type_table, temporal_type_table)
            ri = assignaTipus(r, type_table, temporal_type_table)
            return Node(ind, sim, le, ri, t.tipus)
        case Buit():
            return Buit()

# Crea nodes i els connecta a l'arbre DOT


def printArbre(t: Arbre):
    match t:
        case Node(ind, sim, l, r, tip):
            dot.node(str(ind), sim + "\n" + tip)
            printArbre(l)
            printArbre(r)
            if not esBuit(l):
                (il, sl) = valorNode(l)
                dot.edge(str(ind), str(il))
            if not esBuit(r):
                (ir, sr) = valorNode(r)
                dot.edge(str(ind), str(ir))


class ExcepcioTipus(Exception):
    pass

# A una definicio com (Tip -> (Tip2 -> Tip3)), agafa ('Tip', '(Tip2 -> Tip3)')


def grabTipus(tipus_sencer: str):
    try:
        st = 1
        ultim = -1

        # El primer es una expressio amb parentesi [ex: (N -> N)]
        if tipus_sencer[st] == '(':
            # Cal verificar parentesis multinivell
            equil = 1
            ind = 2
            while equil > 0:
                if tipus_sencer[ind] == '(':
                    equil += 1
                elif tipus_sencer[ind] == ')':
                    equil -= 1
                ind += 1
            end = ind
        else:  # Nomes es una paraula
            end = tipus_sencer.find(' ', st)

        # +4 per treure ' -> '
        return tipus_sencer[st:end], tipus_sencer[end + 4:ultim]
    except Exception as e:
        raise Exception(
            'Probablement estàs fent servir una funció sense definir-la primer.')

# Deixa a type_vars_table per cada valor de temporal_type_table (variables
# de tipus) quin tipus real correspon
def infereixTipus(
        t: Arbre,
        type_table: dict,
        temporal_type_table: dict,
        type_vars_table: dict):
    match t:
        case Node(ind, sim, l, r, tip):

            if sim in type_table.keys():  # Ja se sap el tipus
                return Node(ind, sim, l, r, type_table[sim])

            elif sim in temporal_type_table.keys():
                
                # Te un tipus temporal, però ja se'n sap el tipus real  
                if temporal_type_table[sim] in type_vars_table.keys():  
                    return Node(ind, sim, l, r, type_vars_table[temporal_type_table[sim]])
                return Node(ind, sim, l, r, temporal_type_table[sim])

            elif sim == '@':  # Aplicació
                l = infereixTipus(l, type_table, temporal_type_table, type_vars_table)
                ltip = l.tipus
                r = infereixTipus(r, type_table, temporal_type_table, type_vars_table)
                rtip = r.tipus

                ltipus, lresta = grabTipus(ltip)

                # Es el tipus ja concret, o es una variable de tipus?
                l_concret = True  # No es gestionen funcions amb variables de tipus de moment
                r_concret = rtip in type_table.values()
                iguals = ltipus == rtip

                if not iguals and l_concret and r_concret:
                    raise ExcepcioTipus(f"Error de tipus: {ltipus} vs {rtip}")

                if l_concret and not r_concret:  # Sabem quin tipus ha de tenir R per entrar a la funcio de L
                    r = setTipus(r, ltipus)
                    type_vars_table[rtip] = ltipus

                # El tipus de l'aplicació @ és el que queda de la funció aplicada
                t = setTipus(t, lresta)
                type_vars_table[tip] = lresta
                return Node(ind, sim, l, r, lresta)

            elif sim == '\u03BB':  # Abstracció

                # La funció està a la dreta, important començar per aquí
                r = infereixTipus(r, type_table, temporal_type_table, type_vars_table)
                l = infereixTipus(l, type_table, temporal_type_table, type_vars_table)
                tipus = '(' + l.tipus + ' -> ' + r.tipus + ')'
                t = setTipus(t, tipus)
                type_vars_table[tip] = tipus
                return Node(ind, sim, l, r, tipus)

# Per poder treure els errors de sintaxi per Streamlit
class HinnerErrorListener(ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error de sintaxi a {line}:{column}: {msg}"
        self.errors.append(error_message)

    def getErrors(self):
        return self.errors

# ------------------------------- Visitador ---------------------------------- #


class TreeVisitor(hmVisitor):

    def __init__(self, type_table) -> None:
        super().__init__()
        self.arbre = Buit()
        self.comptador = 0  # Per numerar els nodes DOT
        self.type_table = type_table

    def getTable(self):
        return self.type_table

    def visitRoot(self, ctx: hmParser.RootContext):
        res = self.visitChildren(ctx)
        return res

    def visitDefinicio(self, ctx: hmParser.DefinicioContext):
        [thing, symb, typedef] = list(ctx.getChildren())
        text = self.visit(typedef)
        self.type_table[thing.getText()] = text

    def visitTipusCompost(self, ctx: hmParser.TipusCompostContext):
        [pL, tipusL, op, tipusR, pR] = list(ctx.getChildren())
        return '(' + self.visit(tipusL) + ' -> ' + self.visit(tipusR) + ')'

    def visitTipusBase(self, ctx: hmParser.TipusBaseContext):
        [base] = list(ctx.getChildren())
        return base.getText()

    def visitTipusFuncio(self, ctx: hmParser.TipusFuncioContext):
        [l, op, r] = ctx.getChildren()
        return '(' + self.visit(l) + ' -> ' + self.visit(r) + ')'

    def visitTermeAbstraccio(self, ctx: hmParser.TermeAbstraccioContext):
        [lamb, var, fletxa, terme] = list(ctx.getChildren())
        t = self.visit(terme)

        self.comptador += 1
        return Node(
            self.comptador,
            '\u03BB',
            Node( 
                self.comptador +
                1,
                str(var),
                Buit(),
                Buit()),
            t)

    def visitNumero(self, ctx: hmParser.NumeroContext):
        self.comptador += 1
        return Node(self.comptador, ctx.getText(), Buit(), Buit())

    def visitParentesi(self, ctx: hmParser.ParentesiContext):
        [left, terme, right] = list(ctx.getChildren())

        t = self.visit(terme)
        self.comptador += 1
        return Node(self.comptador, '(' + t.simbol + ')', Buit(), Buit())

    def visitTermeOperador(self, ctx: hmParser.TermeOperadorContext):
        [op] = list(ctx.getChildren())

        self.comptador += 1
        return Node(self.comptador, str(op), Buit(), Buit())

    def visitParaula(self, ctx: hmParser.ParaulaContext):
        self.comptador += 1
        return Node(self.comptador, ctx.getText(), Buit(), Buit())

    def visitTermeAplicacio(self, ctx: hmParser.TermeAplicacioContext):
        [left, right] = list(ctx.getChildren())
        l = self.visit(left)
        r = self.visit(right)

        self.comptador += 1
        return Node(self.comptador, "@", l, r)

# -------------------------------------- Part Streamlit ------------------------------------ #

# Crea interficie
user_input = st.text_input("Expressió:")
submit_button = st.button("Fer")

# Crea graf
dot = Digraph()

# Crea diccionari de tipus reals si es el primer cop que s'executa
if 'type_table' not in st.session_state:
    st.session_state['type_table'] = dumps({})

# Quan es prem el boto
if submit_button:

    definicio = user_input.find('::') != -1

    input_stream = InputStream(user_input)

    dot = Digraph()

    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)

    # Per gestionar els errors de sintaxi de forma custom
    err_listener = HinnerErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)

    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() == 0:
        try:
            type_table = loads(st.session_state['type_table'])

            # Visita l'arbre sintàctic
            visitor = TreeVisitor(type_table)
            arbre = visitor.visit(tree)

            temporal_type_table = {}
            arbre = assignaTipus(arbre, type_table, temporal_type_table)

            st.dataframe(type_table)

            if not definicio:  # Si és una expressió, continua amb inferència

                # Fa arbre DOT
                printArbre(arbre)
                st.graphviz_chart(dot.source)

                type_vars_table = {}
                arbre = infereixTipus(
                    arbre, type_table, temporal_type_table, type_vars_table)

                # Reset de l'arbre DOT per fer un altre amb els nous tipus
                dot = Digraph()
                printArbre(arbre)
                st.graphviz_chart(dot.source)

                # Ara volem la traducció variable tipus -> tipus
                st.dataframe(type_vars_table)

            st.session_state['type_table'] = dumps(type_table)
        except ExcepcioTipus as e:
            st.write(str(e))
            print(str(e))
        except Exception as e:
            st.write('Hi ha hagut un error:\n', str(e))
            print('Hi ha hagut un error:\n', str(e))

    else:  # Hi ha errors de sintaxi
        syntax_errors = parser.getNumberOfSyntaxErrors()
        if syntax_errors == 1:
            st.write(1, 'error de sintaxi.')
        else:
            st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        for error in err_listener.errors:
            st.write(error)
