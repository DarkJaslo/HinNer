# Generated from exprs.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#sumaResta.
    def visitSumaResta(self, ctx:exprsParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#potencia.
    def visitPotencia(self, ctx:exprsParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#parentesi.
    def visitParentesi(self, ctx:exprsParser.ParentesiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#divisioProducte.
    def visitDivisioProducte(self, ctx:exprsParser.DivisioProducteContext):
        return self.visitChildren(ctx)



del exprsParser