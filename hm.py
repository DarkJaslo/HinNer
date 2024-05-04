from __future__ import annotations
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
from graphviz import Digraph
import streamlit as st
from dataclasses import dataclass

class Buit:
    pass

@dataclass
class Node:
    index: int
    simbol: str
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

def valorNode(a: Arbre):
    match a:
        case Buit():
            return (-1,"NONE")
        case Node():
            return (a.index,a.simbol)
        
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

def printArbre(t: Arbre):
    match t:
        #case Buit():
            #st.write("Buit")
        case Node():
            (i,s) = valorNode(t)
            dot.node(str(i),s)
            #st.write("Node:",i,s)
            l = arbreEsq(t)
            r = arbreDre(t)
            printArbre(l)
            printArbre(r)
            if not esBuit(l):
                (il,sl) = valorNode(l)
                dot.edge(str(i),str(il))
            if not esBuit(r):
                (ir,sr) = valorNode(r)
                dot.edge(str(i),str(ir))


class TreeVisitor(hmVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.arbre = Buit()
        self.comptador = 0

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        res = self.visitChildren(ctx)
        return res


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

# Quan es prem el boto
if submit_button:

    #st.write("Text:", user_input)
    input_stream = InputStream(user_input)

    dot = Digraph()

    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() == 0:
        #st.write("No errors!")
        visitor = TreeVisitor()
        arbre = visitor.visit(tree)
        printArbre(arbre)
        st.graphviz_chart(dot.source)
    else:
        st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        st.write(tree.toStringTree(recog=parser))