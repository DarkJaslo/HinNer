from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))

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
    def visitSumaResta(self, ctx:exprsParser.SumaRestaContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == "+":
            return self.visit(expressio1) + self.visit(expressio2)
        elif operador.getText() == "-":
            return self.visit(expressio1) - self.visit(expressio2)
    
    # Visit a parse tree produced by exprsParser#producte.
    def visitDivisioProducte(self, ctx:exprsParser.DivisioProducteContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == "/":
            return self.visit(expressio1) / self.visit(expressio2)
        elif operador.getText() == "*":
            return self.visit(expressio1) * self.visit(expressio2)

input_stream = InputStream(input('? '))
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
  visitor = TreeVisitor()
  visitor.visit(tree)
else:
  print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
  print(tree.toStringTree(recog=parser))