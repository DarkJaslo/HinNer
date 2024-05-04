# Generated from hm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,32,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,18,8,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,2,
        1,2,1,2,1,2,1,2,1,2,0,1,2,3,0,2,4,0,1,1,0,3,6,33,0,6,1,0,0,0,2,17,
        1,0,0,0,4,26,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,9,6,1,-1,0,9,18,5,
        11,0,0,10,18,5,9,0,0,11,12,5,1,0,0,12,13,3,2,1,0,13,14,5,2,0,0,14,
        18,1,0,0,0,15,18,3,4,2,0,16,18,7,0,0,0,17,8,1,0,0,0,17,10,1,0,0,
        0,17,11,1,0,0,0,17,15,1,0,0,0,17,16,1,0,0,0,18,23,1,0,0,0,19,20,
        10,2,0,0,20,22,3,2,1,3,21,19,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,
        23,24,1,0,0,0,24,3,1,0,0,0,25,23,1,0,0,0,26,27,5,7,0,0,27,28,5,11,
        0,0,28,29,5,8,0,0,29,30,3,2,1,0,30,5,1,0,0,0,2,17,23
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'\\'", "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "WS", "PARAULA" ]

    RULE_root = 0
    RULE_terme = 1
    RULE_abstraccio = 2

    ruleNames =  [ "root", "terme", "abstraccio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUM=9
    WS=10
    PARAULA=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terme(self):
            return self.getTypedRuleContext(hmParser.TermeContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermeAbstraccioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def abstraccio(self):
            return self.getTypedRuleContext(hmParser.AbstraccioContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermeAbstraccio" ):
                return visitor.visitTermeAbstraccio(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class ParentesiContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(hmParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesi" ):
                return visitor.visitParentesi(self)
            else:
                return visitor.visitChildren(self)


    class TermeOperadorContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermeOperador" ):
                return visitor.visitTermeOperador(self)
            else:
                return visitor.visitChildren(self)


    class ParaulaContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARAULA(self):
            return self.getToken(hmParser.PARAULA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaula" ):
                return visitor.visitParaula(self)
            else:
                return visitor.visitChildren(self)


    class TermeAplicacioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TermeContext)
            else:
                return self.getTypedRuleContext(hmParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermeAplicacio" ):
                return visitor.visitTermeAplicacio(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = hmParser.ParaulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(hmParser.PARAULA)
                pass
            elif token in [9]:
                localctx = hmParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(hmParser.NUM)
                pass
            elif token in [1]:
                localctx = hmParser.ParentesiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(hmParser.T__0)
                self.state = 12
                self.terme(0)
                self.state = 13
                self.match(hmParser.T__1)
                pass
            elif token in [7]:
                localctx = hmParser.TermeAbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.abstraccio()
                pass
            elif token in [3, 4, 5, 6]:
                localctx = hmParser.TermeOperadorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.TermeAplicacioContext(self, hmParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 19
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 20
                    self.terme(3) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AbstraccioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAULA(self):
            return self.getToken(hmParser.PARAULA, 0)

        def terme(self):
            return self.getTypedRuleContext(hmParser.TermeContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_abstraccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccio" ):
                return visitor.visitAbstraccio(self)
            else:
                return visitor.visitChildren(self)




    def abstraccio(self):

        localctx = hmParser.AbstraccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_abstraccio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(hmParser.T__6)
            self.state = 27
            self.match(hmParser.PARAULA)
            self.state = 28
            self.match(hmParser.T__7)
            self.state = 29
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




