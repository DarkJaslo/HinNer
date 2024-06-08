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
        4,1,12,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,3,0,11,8,0,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,25,8,2,1,2,1,2,1,
        2,5,2,30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,47,8,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,1,3,
        0,2,4,6,4,0,2,4,6,0,1,2,0,7,8,11,11,59,0,10,1,0,0,0,2,12,1,0,0,0,
        4,24,1,0,0,0,6,46,1,0,0,0,8,11,3,6,3,0,9,11,3,2,1,0,10,8,1,0,0,0,
        10,9,1,0,0,0,11,1,1,0,0,0,12,13,7,0,0,0,13,14,5,1,0,0,14,15,3,4,
        2,0,15,3,1,0,0,0,16,17,6,2,-1,0,17,25,5,10,0,0,18,19,5,2,0,0,19,
        20,3,4,2,0,20,21,5,3,0,0,21,22,3,4,2,0,22,23,5,4,0,0,23,25,1,0,0,
        0,24,16,1,0,0,0,24,18,1,0,0,0,25,31,1,0,0,0,26,27,10,1,0,0,27,28,
        5,3,0,0,28,30,3,4,2,1,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,
        31,32,1,0,0,0,32,5,1,0,0,0,33,31,1,0,0,0,34,35,6,3,-1,0,35,47,5,
        11,0,0,36,47,5,8,0,0,37,38,5,2,0,0,38,39,3,6,3,0,39,40,5,4,0,0,40,
        47,1,0,0,0,41,42,5,5,0,0,42,43,5,11,0,0,43,44,5,3,0,0,44,47,3,6,
        3,2,45,47,5,7,0,0,46,34,1,0,0,0,46,36,1,0,0,0,46,37,1,0,0,0,46,41,
        1,0,0,0,46,45,1,0,0,0,47,52,1,0,0,0,48,49,10,3,0,0,49,51,3,6,3,4,
        50,48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,7,1,0,
        0,0,54,52,1,0,0,0,5,10,24,31,46,52
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'('", "'->'", "')'", "'\\'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OP", "OPPAR", "NUM", "WS", 
                      "TYPEID", "ID", "PARAULA" ]

    RULE_root = 0
    RULE_def = 1
    RULE_tipus = 2
    RULE_terme = 3

    ruleNames =  [ "root", "def", "tipus", "terme" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    OP=6
    OPPAR=7
    NUM=8
    WS=9
    TYPEID=10
    ID=11
    PARAULA=12

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
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.terme(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
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

        def tipus(self):
            return self.getTypedRuleContext(hmParser.TipusContext,0)

        def ID(self):
            return self.getToken(hmParser.ID, 0)
        def NUM(self):
            return self.getToken(hmParser.NUM, 0)
        def OPPAR(self):
            return self.getToken(hmParser.OPPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicio" ):
                return visitor.visitDefinicio(self)
            else:
                return visitor.visitChildren(self)



    def def_(self):

        localctx = hmParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_def)
        self._la = 0 # Token type
        try:
            localctx = hmParser.DefinicioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 13
            self.match(hmParser.T__0)
            self.state = 14
            self.tipus(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_tipus

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TipusCompostContext(TipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipus(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TipusContext)
            else:
                return self.getTypedRuleContext(hmParser.TipusContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipusCompost" ):
                return visitor.visitTipusCompost(self)
            else:
                return visitor.visitChildren(self)


    class TipusBaseContext(TipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPEID(self):
            return self.getToken(hmParser.TYPEID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipusBase" ):
                return visitor.visitTipusBase(self)
            else:
                return visitor.visitChildren(self)


    class TipusFuncioContext(TipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipus(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TipusContext)
            else:
                return self.getTypedRuleContext(hmParser.TipusContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipusFuncio" ):
                return visitor.visitTipusFuncio(self)
            else:
                return visitor.visitChildren(self)



    def tipus(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.TipusContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_tipus, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = hmParser.TipusBaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(hmParser.TYPEID)
                pass
            elif token in [2]:
                localctx = hmParser.TipusCompostContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(hmParser.T__1)
                self.state = 19
                self.tipus(0)
                self.state = 20
                self.match(hmParser.T__2)
                self.state = 21
                self.tipus(0)
                self.state = 22
                self.match(hmParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.TipusFuncioContext(self, hmParser.TipusContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_tipus)
                    self.state = 26
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 27
                    self.match(hmParser.T__2)
                    self.state = 28
                    self.tipus(1) 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def OPPAR(self):
            return self.getToken(hmParser.OPPAR, 0)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_terme, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = hmParser.ParaulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 35
                self.match(hmParser.ID)
                pass
            elif token in [8]:
                localctx = hmParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(hmParser.NUM)
                pass
            elif token in [2]:
                localctx = hmParser.ParentesiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(hmParser.T__1)
                self.state = 38
                self.terme(0)
                self.state = 39
                self.match(hmParser.T__3)
                pass
            elif token in [5]:
                localctx = hmParser.TermeAbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(hmParser.T__4)
                self.state = 42
                self.match(hmParser.ID)
                self.state = 43
                self.match(hmParser.T__2)
                self.state = 44
                self.terme(2)
                pass
            elif token in [7]:
                localctx = hmParser.TermeOperadorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(hmParser.OPPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.TermeAplicacioContext(self, hmParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 48
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 49
                    self.terme(4) 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self._predicates[2] = self.tipus_sempred
        self._predicates[3] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def tipus_sempred(self, localctx:TipusContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




