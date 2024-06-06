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
        4,1,11,43,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,17,8,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,9,2,
        1,2,0,1,4,3,0,2,4,0,0,48,0,8,1,0,0,0,2,16,1,0,0,0,4,33,1,0,0,0,6,
        9,3,4,2,0,7,9,3,2,1,0,8,6,1,0,0,0,8,7,1,0,0,0,9,1,1,0,0,0,10,17,
        5,10,0,0,11,17,5,9,0,0,12,17,5,7,0,0,13,14,5,1,0,0,14,15,5,6,0,0,
        15,17,5,2,0,0,16,10,1,0,0,0,16,11,1,0,0,0,16,12,1,0,0,0,16,13,1,
        0,0,0,17,18,1,0,0,0,18,19,5,3,0,0,19,20,5,9,0,0,20,3,1,0,0,0,21,
        22,6,2,-1,0,22,34,5,10,0,0,23,34,5,7,0,0,24,25,5,1,0,0,25,26,3,4,
        2,0,26,27,5,2,0,0,27,34,1,0,0,0,28,29,5,4,0,0,29,30,5,10,0,0,30,
        31,5,5,0,0,31,34,3,4,2,2,32,34,5,6,0,0,33,21,1,0,0,0,33,23,1,0,0,
        0,33,24,1,0,0,0,33,28,1,0,0,0,33,32,1,0,0,0,34,39,1,0,0,0,35,36,
        10,3,0,0,36,38,3,4,2,4,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,5,1,0,0,0,41,39,1,0,0,0,4,8,16,33,39
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'::'", "'\\'", "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OP", "NUM", "WS", "TYPEID", 
                      "ID", "PARAULA" ]

    RULE_root = 0
    RULE_def = 1
    RULE_terme = 2

    ruleNames =  [ "root", "def", "terme" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    OP=6
    NUM=7
    WS=8
    TYPEID=9
    ID=10
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


        def def_(self):
            return self.getTypedRuleContext(hmParser.DefContext,0)


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
            self.state = 8
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.terme(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.def_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_def

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefinicioContext(DefContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.DefContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPEID(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.TYPEID)
            else:
                return self.getToken(hmParser.TYPEID, i)
        def ID(self):
            return self.getToken(hmParser.ID, 0)
        def NUM(self):
            return self.getToken(hmParser.NUM, 0)
        def OP(self):
            return self.getToken(hmParser.OP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicio" ):
                return visitor.visitDefinicio(self)
            else:
                return visitor.visitChildren(self)



    def def_(self):

        localctx = hmParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_def)
        try:
            localctx = hmParser.DefinicioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 10
                self.match(hmParser.ID)
                pass
            elif token in [9]:
                self.state = 11
                self.match(hmParser.TYPEID)
                pass
            elif token in [7]:
                self.state = 12
                self.match(hmParser.NUM)
                pass
            elif token in [1]:
                self.state = 13
                self.match(hmParser.T__0)
                self.state = 14
                self.match(hmParser.OP)
                self.state = 15
                self.match(hmParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 18
            self.match(hmParser.T__2)
            self.state = 19
            self.match(hmParser.TYPEID)
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

        def ID(self):
            return self.getToken(hmParser.ID, 0)
        def terme(self):
            return self.getTypedRuleContext(hmParser.TermeContext,0)


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

        def OP(self):
            return self.getToken(hmParser.OP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermeOperador" ):
                return visitor.visitTermeOperador(self)
            else:
                return visitor.visitChildren(self)


    class ParaulaContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hmParser.ID, 0)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_terme, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = hmParser.ParaulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 22
                self.match(hmParser.ID)
                pass
            elif token in [7]:
                localctx = hmParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(hmParser.NUM)
                pass
            elif token in [1]:
                localctx = hmParser.ParentesiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(hmParser.T__0)
                self.state = 25
                self.terme(0)
                self.state = 26
                self.match(hmParser.T__1)
                pass
            elif token in [4]:
                localctx = hmParser.TermeAbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(hmParser.T__3)
                self.state = 29
                self.match(hmParser.ID)
                self.state = 30
                self.match(hmParser.T__4)
                self.state = 31
                self.terme(2)
                pass
            elif token in [6]:
                localctx = hmParser.TermeOperadorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(hmParser.OP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.TermeAplicacioContext(self, hmParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 35
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 36
                    self.terme(4) 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




