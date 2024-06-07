# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hmParser import hmParser
else:
    from hmParser import hmParser

# This class defines a complete generic visitor for a parse tree produced by hmParser.

class hmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#definicio.
    def visitDefinicio(self, ctx:hmParser.DefinicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#tipusBase.
    def visitTipusBase(self, ctx:hmParser.TipusBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#tipusFuncio.
    def visitTipusFuncio(self, ctx:hmParser.TipusFuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#termeAbstraccio.
    def visitTermeAbstraccio(self, ctx:hmParser.TermeAbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parentesi.
    def visitParentesi(self, ctx:hmParser.ParentesiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#termeOperador.
    def visitTermeOperador(self, ctx:hmParser.TermeOperadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#paraula.
    def visitParaula(self, ctx:hmParser.ParaulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#termeAplicacio.
    def visitTermeAplicacio(self, ctx:hmParser.TermeAplicacioContext):
        return self.visitChildren(ctx)



del hmParser