from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor

from graphviz import Digraph
import streamlit as st

class TreeVisitor(hmVisitor):

    def __init__(self) -> None:
        super().__init__()
        comptador = 0
        pila = []

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        st.write("root")
        st.write(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#termeAbstraccio.
    def visitTermeAbstraccio(self, ctx:hmParser.TermeAbstraccioContext):
        st.write("abstraccio")
        st.write(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        st.write("numero")
        st.write(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parentesi.
    def visitParentesi(self, ctx:hmParser.ParentesiContext):
        st.write("parentesi")
        st.write(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#termeOperador.
    def visitTermeOperador(self, ctx:hmParser.TermeOperadorContext):
        st.write("operador")
        st.write(ctx)
        a = self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#paraula.
    def visitParaula(self, ctx:hmParser.ParaulaContext):
        st.write("paraula")
        st.write(ctx)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#termeAplicacio.
    def visitTermeAplicacio(self, ctx:hmParser.TermeAplicacioContext):
        #dot.node(str(ctx[0]),'@')
        st.write("aplicacio")
        st.write(ctx)
        return self.visitChildren(ctx)
        
    # Visit a parse tree produced by hmParser#abstraccio.
    def visitAbstraccio(self, ctx:hmParser.AbstraccioContext):
        return self.visitChildren(ctx)
        
# Crea interficie
user_input = st.text_input("Expressió:")
submit_button = st.button("Submit")

# Crea graf
dot = Digraph()

# Quan es prem el boto
if submit_button:

    st.write("Text:", user_input)
    input_stream = InputStream(user_input)

    dot = Digraph()

    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() == 0:
        st.write("No errors!")
        visitor = TreeVisitor()
        visitor.visit(tree)
        st.graphviz_chart(dot.source)
    else:
        st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        st.write(tree.toStringTree(recog=parser))