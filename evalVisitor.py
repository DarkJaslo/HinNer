import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#suma.
    def visitSuma(self, ctx:exprsParser.SumaContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) + self.visit(expressio2)


    # Visit a parse tree produced by exprsParser#potencia.
    def visitPotencia(self, ctx:exprsParser.PotenciaContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) ** self.visit(expressio2)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())


    # Visit a parse tree produced by exprsParser#parentesi.
    def visitParentesi(self, ctx:exprsParser.ParentesiContext):
        [obrir, expressio, tancar] = list(ctx.getChildren())
        return self.visit(expressio)


    # Visit a parse tree produced by exprsParser#resta.
    def visitResta(self, ctx:exprsParser.RestaContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) - self.visit(expressio2)


    # Visit a parse tree produced by exprsParser#divisio.
    def visitDivisio(self, ctx:exprsParser.DivisioContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) / self.visit(expressio2)


    # Visit a parse tree produced by exprsParser#producte.
    def visitProducte(self, ctx:exprsParser.ProducteContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) * self.visit(expressio2)