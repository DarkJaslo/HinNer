from __future__ import annotations
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
from graphviz import Digraph
import streamlit as st
from dataclasses import dataclass
from pickle import dumps, loads  #per Streamlit 
from antlr4.error.ErrorListener import ErrorListener
import pandas as pd # DataFrames

# Generador pels tipus
def generador_lletres():
    for c in range(ord('a'),ord('z')+1):
        yield chr(c)

lletres = generador_lletres()

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

def valorNode(a: Arbre):
    match a:
        case Buit():
            return (-1,"NONE")
        case Node():
            return (a.index,a.simbol)
        
def setTipus(a: Arbre, tipus:str):
    match a:
        case Node(i,s,e,d,t):
            return Node(i,s,e,d,tipus)
        
def arbreEsq(a: Arbre): 
    match a:
        case Buit():
            return Buit
        case Node():
            return a.esq
        
def arbreDre(a: Arbre): 
    match a:
        case Buit():
            return Buit
        case Node():
            return a.dre
        
def creaArbre(t: TreeVisitor):
    return t.visitRoot()

def esBuit(t: Arbre):
    match t:
        case Buit():
            return True
        case Node():
            return False
        
def assignaTipus(t: Arbre, type_table: dict, temporal_type_table: dict):
    match t:
        case Node(ind,sim,l,r,tip):

            if sim not in ['@','\u03BB']:
                temp = False
                if sim not in type_table.keys():
                    if sim not in temporal_type_table.keys():
                        temporal_type_table[sim] = next(lletres)
                    temp = True
                t = setTipus(t,temporal_type_table[sim]) if temp else setTipus(t,type_table[sim])
            else:
                t = setTipus(t,next(lletres))                
                
            le = assignaTipus(l,type_table,temporal_type_table)
            ri = assignaTipus(r,type_table,temporal_type_table)
            return Node(ind,sim,le,ri,t.tipus)
        case Buit():
            return Buit()

def printArbre(t: Arbre):
    match t:
        #case Buit():
            #st.write("Buit")
        case Node(ind, sim, l, r, tip):
            dot.node(str(ind),sim+"\n"+tip)
            #st.write("Node:",i,s)
            printArbre(l)
            printArbre(r)
            if not esBuit(l):
                (il,sl) = valorNode(l)
                dot.edge(str(ind),str(il))
            if not esBuit(r):
                (ir,sr) = valorNode(r)
                dot.edge(str(ind),str(ir))

class HinnerErrorListener(ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error de sintaxi a {line}:{column}: {msg}"
        self.errors.append(error_message)

    def getErrors(self):
        return self.errors

class TreeVisitor(hmVisitor):

    def __init__(self, type_table) -> None:
        super().__init__()
        self.arbre = Buit()
        self.comptador = 0
        self.type_table = type_table

    def getTable(self):
        return self.type_table

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        res = self.visitChildren(ctx)
        return res
    
    def visitDefinicio(self, ctx:hmParser.DefinicioContext):
        [thing, symb, typedef] = list(ctx.getChildren())
        # La idea per mes tard es que type_id no sigui una string, sino un arbre d'inferencia
        text = self.visit(typedef)
        self.type_table[thing.getText()] = text 

    def visitTipusBase(self, ctx:hmParser.TipusBaseContext):
        [base] = list(ctx.getChildren())
        return base.getText()

    def visitTipusFuncio(self, ctx:hmParser.TipusFuncioContext):
        [l, op, r] = ctx.getChildren()
        return '(' + self.visit(l) + ' -> ' + self.visit(r) + ')'


    # Visit a parse tree produced by hmParser#termeAbstraccio.
    def visitTermeAbstraccio(self, ctx:hmParser.TermeAbstraccioContext):

        [lamb, var, fletxa, terme] = list(ctx.getChildren())
        t = self.visit(terme)

        self.comptador += 1
        return Node(self.comptador,'\u03BB',Node(self.comptador+1,str(var),Buit(),Buit()),t)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        self.comptador += 1
        return Node(self.comptador,ctx.getText(),Buit(),Buit())


    # Visit a parse tree produced by hmParser#parentesi.
    def visitParentesi(self, ctx:hmParser.ParentesiContext):
        [left, terme, right] = list(ctx.getChildren())

        t = self.visit(terme)
        self.comptador += 1
        return Node(self.comptador,'('+t.simbol+')',Buit(),Buit())


    # Visit a parse tree produced by hmParser#termeOperador.
    def visitTermeOperador(self, ctx:hmParser.TermeOperadorContext):
        [op] = list(ctx.getChildren())

        self.comptador += 1
        return Node(self.comptador,str(op),Buit(),Buit())


    # Visit a parse tree produced by hmParser#paraula.
    def visitParaula(self, ctx:hmParser.ParaulaContext):

        self.comptador += 1
        return Node(self.comptador,ctx.getText(),Buit(),Buit())


    # Visit a parse tree produced by hmParser#termeAplicacio.
    def visitTermeAplicacio(self, ctx:hmParser.TermeAplicacioContext):
        #dot.node(str(ctx[0]),'@')

        [left, right] = list(ctx.getChildren())
        l = self.visit(left)
        r = self.visit(right)

        self.comptador += 1
        return Node(self.comptador,"@",l,r)
        
# Crea interficie
user_input = st.text_input("Expressió:")
submit_button = st.button("Submit")

# Crea graf
dot = Digraph()

# Crea diccionari si es el primer cop que s'executa
if 'type_table' not in st.session_state:
    st.session_state['type_table'] = dumps({})

# Quan es prem el boto
if submit_button:

    #st.write("Text:", user_input)
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
        type_table = loads(st.session_state['type_table'])

        visitor = TreeVisitor(type_table)
        arbre = visitor.visit(tree)

        # Crea i dibuixa arbre d'expressions
        temporal_type_table = {}

        arbre = assignaTipus(arbre,type_table,temporal_type_table)

        # Dibuixa taula de tipus
        #type_table = visitor.getTable()

        final_table = { keys : values for keys, values in type_table.items()}
        print('types')
        print(type_table.items())
        print('final types')
        print(final_table.items())

        for key,value in temporal_type_table.items():
            final_table[key] = value

        st.dataframe(final_table)

        printArbre(arbre)
        st.graphviz_chart(dot.source)

        print('types2')
        print(type_table.items())
        print('final types2')
        print(final_table.items())

        st.session_state['type_table'] = dumps(type_table)
    else: # Hi ha errors
        st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        for error in err_listener.errors:
            st.write(error)
        #st.write(tree.toStringTree(recog=parser))