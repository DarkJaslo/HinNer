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


    # Visit a parse tree produced by hmParser#sumaResta.
    def visitSumaResta(self, ctx:hmParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#potencia.
    def visitPotencia(self, ctx:hmParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parentesi.
    def visitParentesi(self, ctx:hmParser.ParentesiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#divisioProducte.
    def visitDivisioProducte(self, ctx:hmParser.DivisioProducteContext):
        return self.visitChildren(ctx)



del hmParser