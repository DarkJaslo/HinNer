# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,86,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,52,8,6,1,7,4,7,55,8,7,11,7,12,7,56,
        1,8,4,8,60,8,8,11,8,12,8,61,1,8,1,8,1,9,1,9,5,9,68,8,9,10,9,12,9,
        71,9,9,1,10,1,10,1,10,1,10,5,10,77,8,10,10,10,12,10,80,9,10,1,11,
        4,11,83,8,11,11,11,12,11,84,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,23,12,1,0,4,3,0,42,43,45,45,47,47,1,0,48,57,
        3,0,9,10,13,13,32,32,2,0,65,90,97,122,95,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,
        25,1,0,0,0,3,28,1,0,0,0,5,30,1,0,0,0,7,33,1,0,0,0,9,35,1,0,0,0,11,
        37,1,0,0,0,13,51,1,0,0,0,15,54,1,0,0,0,17,59,1,0,0,0,19,65,1,0,0,
        0,21,72,1,0,0,0,23,82,1,0,0,0,25,26,5,58,0,0,26,27,5,58,0,0,27,2,
        1,0,0,0,28,29,5,40,0,0,29,4,1,0,0,0,30,31,5,45,0,0,31,32,5,62,0,
        0,32,6,1,0,0,0,33,34,5,41,0,0,34,8,1,0,0,0,35,36,5,92,0,0,36,10,
        1,0,0,0,37,38,7,0,0,0,38,12,1,0,0,0,39,40,5,40,0,0,40,41,5,43,0,
        0,41,52,5,41,0,0,42,43,5,40,0,0,43,44,5,45,0,0,44,52,5,41,0,0,45,
        46,5,40,0,0,46,47,5,42,0,0,47,52,5,41,0,0,48,49,5,40,0,0,49,50,5,
        47,0,0,50,52,5,41,0,0,51,39,1,0,0,0,51,42,1,0,0,0,51,45,1,0,0,0,
        51,48,1,0,0,0,52,14,1,0,0,0,53,55,7,1,0,0,54,53,1,0,0,0,55,56,1,
        0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,16,1,0,0,0,58,60,7,2,0,0,59,
        58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,
        0,63,64,6,8,0,0,64,18,1,0,0,0,65,69,2,65,90,0,66,68,7,3,0,0,67,66,
        1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,20,1,0,0,0,
        71,69,1,0,0,0,72,78,2,97,122,0,73,77,3,15,7,0,74,77,5,95,0,0,75,
        77,3,23,11,0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,80,1,0,
        0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,22,1,0,0,0,80,78,1,0,0,0,81,83,
        7,3,0,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,
        85,24,1,0,0,0,8,0,51,56,61,69,76,78,84,1,6,0,0
    ]

class hmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    OP = 6
    OPPAR = 7
    NUM = 8
    WS = 9
    TYPEID = 10
    ID = 11
    PARAULA = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::'", "'('", "'->'", "')'", "'\\'" ]

    symbolicNames = [ "<INVALID>",
            "OP", "OPPAR", "NUM", "WS", "TYPEID", "ID", "PARAULA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "OP", "OPPAR", 
                  "NUM", "WS", "TYPEID", "ID", "PARAULA" ]

    grammarFileName = "hm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


