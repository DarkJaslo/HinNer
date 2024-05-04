from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor

class TreeVisitor(hmVisitor):
    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))

    # Visit a parse tree produced by hmParser#potencia.
    def visitPotencia(self, ctx:hmParser.PotenciaContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) ** self.visit(expressio2)

    # Visit a parse tree produced by hmParser#numero.
    def visitNumero(self, ctx:hmParser.NumeroContext):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())

    # Visit a parse tree produced by hmParser#parentesi.
    def visitParentesi(self, ctx:hmParser.ParentesiContext):
        [obrir, expressio, tancar] = list(ctx.getChildren())
        return self.visit(expressio)


    # Visit a parse tree produced by hmParser#resta.
    def visitSumaResta(self, ctx:hmParser.SumaRestaContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == "+":
            return self.visit(expressio1) + self.visit(expressio2)
        elif operador.getText() == "-":
            return self.visit(expressio1) - self.visit(expressio2)
    
    # Visit a parse tree produced by hmParser#producte.
    def visitDivisioProducte(self, ctx:hmParser.DivisioProducteContext):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == "/":
            return self.visit(expressio1) / self.visit(expressio2)
        elif operador.getText() == "*":
            return self.visit(expressio1) * self.visit(expressio2)

input_stream = InputStream(input('? '))
lexer = hmLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = hmParser(token_stream)
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
  visitor = TreeVisitor()
  visitor.visit(tree)
else:
  print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
  print(tree.toStringTree(recog=parser))