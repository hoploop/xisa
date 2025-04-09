# Generated from Grammar.g4 by ANTLR 4.13.2
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
        4,1,31,302,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,5,0,66,8,0,
        10,0,12,0,69,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,79,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,3,9,115,8,9,1,10,1,10,1,10,1,10,1,10,3,10,122,8,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,3,11,131,8,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,3,12,140,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,5,14,154,8,14,10,14,12,14,157,9,14,1,15,1,15,
        1,15,1,15,1,15,1,15,5,15,165,8,15,10,15,12,15,168,9,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        3,16,185,8,16,1,17,1,17,1,17,1,17,1,17,3,17,192,8,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,3,18,201,8,18,1,18,1,18,1,19,1,19,1,19,1,
        19,1,19,3,19,210,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,219,
        8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,21,228,8,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,22,3,22,237,8,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,3,23,246,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,
        255,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,264,8,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,26,3,26,273,8,26,1,26,1,26,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,3,27,284,8,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,31,0,0,32,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,0,2,1,0,1,3,1,0,29,30,309,0,67,1,0,0,
        0,2,78,1,0,0,0,4,80,1,0,0,0,6,87,1,0,0,0,8,90,1,0,0,0,10,94,1,0,
        0,0,12,98,1,0,0,0,14,102,1,0,0,0,16,106,1,0,0,0,18,114,1,0,0,0,20,
        116,1,0,0,0,22,125,1,0,0,0,24,134,1,0,0,0,26,143,1,0,0,0,28,150,
        1,0,0,0,30,158,1,0,0,0,32,184,1,0,0,0,34,186,1,0,0,0,36,195,1,0,
        0,0,38,204,1,0,0,0,40,213,1,0,0,0,42,222,1,0,0,0,44,231,1,0,0,0,
        46,240,1,0,0,0,48,249,1,0,0,0,50,258,1,0,0,0,52,267,1,0,0,0,54,276,
        1,0,0,0,56,287,1,0,0,0,58,292,1,0,0,0,60,297,1,0,0,0,62,299,1,0,
        0,0,64,66,3,2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,1,1,0,0,0,69,67,1,0,0,0,70,79,3,4,2,0,71,79,3,6,3,0,72,
        79,3,10,5,0,73,79,3,12,6,0,74,79,3,14,7,0,75,79,3,8,4,0,76,79,3,
        16,8,0,77,79,3,30,15,0,78,70,1,0,0,0,78,71,1,0,0,0,78,72,1,0,0,0,
        78,73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,
        0,0,0,79,3,1,0,0,0,80,81,5,21,0,0,81,82,5,25,0,0,82,83,5,20,0,0,
        83,84,5,24,0,0,84,85,5,22,0,0,85,86,5,26,0,0,86,5,1,0,0,0,87,88,
        5,18,0,0,88,89,5,21,0,0,89,7,1,0,0,0,90,91,5,21,0,0,91,92,5,25,0,
        0,92,93,3,26,13,0,93,9,1,0,0,0,94,95,5,21,0,0,95,96,5,25,0,0,96,
        97,3,20,10,0,97,11,1,0,0,0,98,99,5,21,0,0,99,100,5,25,0,0,100,101,
        3,22,11,0,101,13,1,0,0,0,102,103,5,21,0,0,103,104,5,25,0,0,104,105,
        3,24,12,0,105,15,1,0,0,0,106,107,5,21,0,0,107,108,5,25,0,0,108,109,
        3,32,16,0,109,17,1,0,0,0,110,115,3,20,10,0,111,115,3,22,11,0,112,
        115,3,24,12,0,113,115,3,26,13,0,114,110,1,0,0,0,114,111,1,0,0,0,
        114,112,1,0,0,0,114,113,1,0,0,0,115,19,1,0,0,0,116,117,5,17,0,0,
        117,118,5,24,0,0,118,121,5,22,0,0,119,120,5,16,0,0,120,122,3,28,
        14,0,121,119,1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,5,26,
        0,0,124,21,1,0,0,0,125,126,5,13,0,0,126,127,5,24,0,0,127,130,5,22,
        0,0,128,129,5,16,0,0,129,131,3,28,14,0,130,128,1,0,0,0,130,131,1,
        0,0,0,131,132,1,0,0,0,132,133,5,26,0,0,133,23,1,0,0,0,134,135,5,
        15,0,0,135,136,5,24,0,0,136,139,5,22,0,0,137,138,5,16,0,0,138,140,
        3,28,14,0,139,137,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,
        5,26,0,0,142,25,1,0,0,0,143,144,5,14,0,0,144,145,5,24,0,0,145,146,
        3,62,31,0,146,147,5,16,0,0,147,148,3,62,31,0,148,149,5,26,0,0,149,
        27,1,0,0,0,150,155,5,29,0,0,151,152,5,16,0,0,152,154,5,29,0,0,153,
        151,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,
        29,1,0,0,0,157,155,1,0,0,0,158,159,5,21,0,0,159,160,5,25,0,0,160,
        161,5,19,0,0,161,166,5,27,0,0,162,165,3,32,16,0,163,165,5,21,0,0,
        164,162,1,0,0,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,
        166,167,1,0,0,0,167,169,1,0,0,0,168,166,1,0,0,0,169,170,5,28,0,0,
        170,31,1,0,0,0,171,185,3,34,17,0,172,185,3,36,18,0,173,185,3,38,
        19,0,174,185,3,40,20,0,175,185,3,52,26,0,176,185,3,42,21,0,177,185,
        3,44,22,0,178,185,3,46,23,0,179,185,3,48,24,0,180,185,3,50,25,0,
        181,185,3,54,27,0,182,185,3,56,28,0,183,185,3,58,29,0,184,171,1,
        0,0,0,184,172,1,0,0,0,184,173,1,0,0,0,184,174,1,0,0,0,184,175,1,
        0,0,0,184,176,1,0,0,0,184,177,1,0,0,0,184,178,1,0,0,0,184,179,1,
        0,0,0,184,180,1,0,0,0,184,181,1,0,0,0,184,182,1,0,0,0,184,183,1,
        0,0,0,185,33,1,0,0,0,186,187,5,12,0,0,187,188,5,24,0,0,188,191,5,
        21,0,0,189,190,5,16,0,0,190,192,5,29,0,0,191,189,1,0,0,0,191,192,
        1,0,0,0,192,193,1,0,0,0,193,194,5,26,0,0,194,35,1,0,0,0,195,196,
        5,12,0,0,196,197,5,24,0,0,197,200,3,18,9,0,198,199,5,16,0,0,199,
        201,5,29,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,
        203,5,26,0,0,203,37,1,0,0,0,204,205,5,9,0,0,205,206,5,24,0,0,206,
        209,5,21,0,0,207,208,5,16,0,0,208,210,3,60,30,0,209,207,1,0,0,0,
        209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,26,0,0,212,39,1,0,0,0,
        213,214,5,9,0,0,214,215,5,24,0,0,215,218,3,18,9,0,216,217,5,16,0,
        0,217,219,3,60,30,0,218,216,1,0,0,0,218,219,1,0,0,0,219,220,1,0,
        0,0,220,221,5,26,0,0,221,41,1,0,0,0,222,223,5,7,0,0,223,224,5,24,
        0,0,224,227,5,21,0,0,225,226,5,16,0,0,226,228,3,60,30,0,227,225,
        1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,5,26,0,0,230,43,
        1,0,0,0,231,232,5,7,0,0,232,233,5,24,0,0,233,236,3,18,9,0,234,235,
        5,16,0,0,235,237,3,60,30,0,236,234,1,0,0,0,236,237,1,0,0,0,237,238,
        1,0,0,0,238,239,5,26,0,0,239,45,1,0,0,0,240,241,5,8,0,0,241,242,
        5,24,0,0,242,245,5,21,0,0,243,244,5,16,0,0,244,246,3,60,30,0,245,
        243,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,248,5,26,0,0,248,
        47,1,0,0,0,249,250,5,8,0,0,250,251,5,24,0,0,251,254,3,18,9,0,252,
        253,5,16,0,0,253,255,3,60,30,0,254,252,1,0,0,0,254,255,1,0,0,0,255,
        256,1,0,0,0,256,257,5,26,0,0,257,49,1,0,0,0,258,259,5,10,0,0,259,
        260,5,24,0,0,260,263,5,21,0,0,261,262,5,16,0,0,262,264,3,60,30,0,
        263,261,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,26,0,0,
        266,51,1,0,0,0,267,268,5,10,0,0,268,269,5,24,0,0,269,272,3,18,9,
        0,270,271,5,16,0,0,271,273,3,60,30,0,272,270,1,0,0,0,272,273,1,0,
        0,0,273,274,1,0,0,0,274,275,5,26,0,0,275,53,1,0,0,0,276,277,5,11,
        0,0,277,278,5,24,0,0,278,279,5,21,0,0,279,280,5,16,0,0,280,283,5,
        29,0,0,281,282,5,16,0,0,282,284,5,29,0,0,283,281,1,0,0,0,283,284,
        1,0,0,0,284,285,1,0,0,0,285,286,5,26,0,0,286,55,1,0,0,0,287,288,
        5,4,0,0,288,289,5,24,0,0,289,290,5,22,0,0,290,291,5,26,0,0,291,57,
        1,0,0,0,292,293,5,5,0,0,293,294,5,24,0,0,294,295,5,22,0,0,295,296,
        5,26,0,0,296,59,1,0,0,0,297,298,7,0,0,0,298,61,1,0,0,0,299,300,7,
        1,0,0,300,63,1,0,0,0,21,67,78,114,121,130,139,155,164,166,184,191,
        200,209,218,227,236,245,254,263,272,283
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'left'", "'right'", "'middle'", "'keyPress'", 
                     "'keyRelease'", "'keyType'", "'mouseClick'", "'mouseDoubleClick'", 
                     "'mousePress'", "'mouseRelease'", "'mouseScroll'", 
                     "'wait'", "'text'", "'position'", "'regex'", "','", 
                     "'label'", "'use'", "'scenario'", "'detector'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "'='", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", 
                      "KEY_RELEASE", "KEY_TYPE", "MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", 
                      "MOUSE_PRESS", "MOUSE_RELEASE", "MOUSE_SCROLL", "WAIT", 
                      "TEXT", "POSITION", "REGEX", "COMMA", "LABEL", "USE", 
                      "SCENARIO", "DETECTOR", "ID", "STRING", "ESC", "ORPAR", 
                      "EQ", "CRPAR", "OCPAR", "CCPAR", "INT", "FLOAT", "WS" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_createDetector = 2
    RULE_useDetector = 3
    RULE_createSelectorByPosition = 4
    RULE_createSelectorByLabel = 5
    RULE_createSelectorByText = 6
    RULE_createSelectorByRegex = 7
    RULE_createStep = 8
    RULE_selector = 9
    RULE_selectorByLabel = 10
    RULE_selectorByText = 11
    RULE_selectorByRegex = 12
    RULE_selectorByPosition = 13
    RULE_selectorOrder = 14
    RULE_createScenario = 15
    RULE_action = 16
    RULE_wait = 17
    RULE_waitSelector = 18
    RULE_mousePress = 19
    RULE_mousePressSelector = 20
    RULE_mouseClick = 21
    RULE_mouseClickSelector = 22
    RULE_mouseDoubleClick = 23
    RULE_mouseDoubleClickSelector = 24
    RULE_mouseRelease = 25
    RULE_mouseReleaseSelector = 26
    RULE_mouseScroll = 27
    RULE_keyPress = 28
    RULE_keyRelease = 29
    RULE_mouseButton = 30
    RULE_number = 31

    ruleNames =  [ "root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
                   "createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
                   "createStep", "selector", "selectorByLabel", "selectorByText", 
                   "selectorByRegex", "selectorByPosition", "selectorOrder", 
                   "createScenario", "action", "wait", "waitSelector", "mousePress", 
                   "mousePressSelector", "mouseClick", "mouseClickSelector", 
                   "mouseDoubleClick", "mouseDoubleClickSelector", "mouseRelease", 
                   "mouseReleaseSelector", "mouseScroll", "keyPress", "keyRelease", 
                   "mouseButton", "number" ]

    EOF = Token.EOF
    LEFT=1
    RIGHT=2
    MIDDLE=3
    KEY_PRESS=4
    KEY_RELEASE=5
    KEY_TYPE=6
    MOUSE_CLICK=7
    MOUSE_DOUBLE_CLICK=8
    MOUSE_PRESS=9
    MOUSE_RELEASE=10
    MOUSE_SCROLL=11
    WAIT=12
    TEXT=13
    POSITION=14
    REGEX=15
    COMMA=16
    LABEL=17
    USE=18
    SCENARIO=19
    DETECTOR=20
    ID=21
    STRING=22
    ESC=23
    ORPAR=24
    EQ=25
    CRPAR=26
    OCPAR=27
    CCPAR=28
    INT=29
    FLOAT=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = GrammarParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==21:
                self.state = 64
                self.stmt()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createDetector(self):
            return self.getTypedRuleContext(GrammarParser.CreateDetectorContext,0)


        def useDetector(self):
            return self.getTypedRuleContext(GrammarParser.UseDetectorContext,0)


        def createSelectorByLabel(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByLabelContext,0)


        def createSelectorByText(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByTextContext,0)


        def createSelectorByRegex(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByRegexContext,0)


        def createSelectorByPosition(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByPositionContext,0)


        def createStep(self):
            return self.getTypedRuleContext(GrammarParser.CreateStepContext,0)


        def createScenario(self):
            return self.getTypedRuleContext(GrammarParser.CreateScenarioContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = GrammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.createDetector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.useDetector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.createSelectorByLabel()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.createSelectorByText()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.createSelectorByRegex()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.createSelectorByPosition()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.createStep()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.createScenario()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateDetectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def DETECTOR(self):
            return self.getToken(GrammarParser.DETECTOR, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_createDetector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateDetector" ):
                listener.enterCreateDetector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateDetector" ):
                listener.exitCreateDetector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateDetector" ):
                return visitor.visitCreateDetector(self)
            else:
                return visitor.visitChildren(self)




    def createDetector(self):

        localctx = GrammarParser.CreateDetectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createDetector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(GrammarParser.ID)
            self.state = 81
            self.match(GrammarParser.EQ)
            self.state = 82
            self.match(GrammarParser.DETECTOR)
            self.state = 83
            self.match(GrammarParser.ORPAR)
            self.state = 84
            self.match(GrammarParser.STRING)
            self.state = 85
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseDetectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(GrammarParser.USE, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_useDetector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseDetector" ):
                listener.enterUseDetector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseDetector" ):
                listener.exitUseDetector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseDetector" ):
                return visitor.visitUseDetector(self)
            else:
                return visitor.visitChildren(self)




    def useDetector(self):

        localctx = GrammarParser.UseDetectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_useDetector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(GrammarParser.USE)
            self.state = 88
            self.match(GrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByPositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def selectorByPosition(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByPositionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_createSelectorByPosition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByPosition" ):
                listener.enterCreateSelectorByPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByPosition" ):
                listener.exitCreateSelectorByPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByPosition" ):
                return visitor.visitCreateSelectorByPosition(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByPosition(self):

        localctx = GrammarParser.CreateSelectorByPositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_createSelectorByPosition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(GrammarParser.ID)
            self.state = 91
            self.match(GrammarParser.EQ)
            self.state = 92
            self.selectorByPosition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def selectorByLabel(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByLabelContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_createSelectorByLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByLabel" ):
                listener.enterCreateSelectorByLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByLabel" ):
                listener.exitCreateSelectorByLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByLabel" ):
                return visitor.visitCreateSelectorByLabel(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByLabel(self):

        localctx = GrammarParser.CreateSelectorByLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_createSelectorByLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GrammarParser.ID)
            self.state = 95
            self.match(GrammarParser.EQ)
            self.state = 96
            self.selectorByLabel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def selectorByText(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByTextContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_createSelectorByText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByText" ):
                listener.enterCreateSelectorByText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByText" ):
                listener.exitCreateSelectorByText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByText" ):
                return visitor.visitCreateSelectorByText(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByText(self):

        localctx = GrammarParser.CreateSelectorByTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_createSelectorByText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(GrammarParser.ID)
            self.state = 99
            self.match(GrammarParser.EQ)
            self.state = 100
            self.selectorByText()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByRegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def selectorByRegex(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByRegexContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_createSelectorByRegex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByRegex" ):
                listener.enterCreateSelectorByRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByRegex" ):
                listener.exitCreateSelectorByRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByRegex" ):
                return visitor.visitCreateSelectorByRegex(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByRegex(self):

        localctx = GrammarParser.CreateSelectorByRegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_createSelectorByRegex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(GrammarParser.ID)
            self.state = 103
            self.match(GrammarParser.EQ)
            self.state = 104
            self.selectorByRegex()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateStepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def action(self):
            return self.getTypedRuleContext(GrammarParser.ActionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_createStep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStep" ):
                listener.enterCreateStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStep" ):
                listener.exitCreateStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateStep" ):
                return visitor.visitCreateStep(self)
            else:
                return visitor.visitChildren(self)




    def createStep(self):

        localctx = GrammarParser.CreateStepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_createStep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(GrammarParser.ID)
            self.state = 107
            self.match(GrammarParser.EQ)
            self.state = 108
            self.action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectorByLabel(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByLabelContext,0)


        def selectorByText(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByTextContext,0)


        def selectorByRegex(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByRegexContext,0)


        def selectorByPosition(self):
            return self.getTypedRuleContext(GrammarParser.SelectorByPositionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelector" ):
                listener.enterSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelector" ):
                listener.exitSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelector" ):
                return visitor.visitSelector(self)
            else:
                return visitor.visitChildren(self)




    def selector(self):

        localctx = GrammarParser.SelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selector)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.selectorByLabel()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.selectorByText()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.selectorByRegex()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.selectorByPosition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorByLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(GrammarParser.LABEL, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def selectorOrder(self):
            return self.getTypedRuleContext(GrammarParser.SelectorOrderContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_selectorByLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorByLabel" ):
                listener.enterSelectorByLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorByLabel" ):
                listener.exitSelectorByLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorByLabel" ):
                return visitor.visitSelectorByLabel(self)
            else:
                return visitor.visitChildren(self)




    def selectorByLabel(self):

        localctx = GrammarParser.SelectorByLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_selectorByLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GrammarParser.LABEL)
            self.state = 117
            self.match(GrammarParser.ORPAR)
            self.state = 118
            self.match(GrammarParser.STRING)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 119
                self.match(GrammarParser.COMMA)
                self.state = 120
                self.selectorOrder()


            self.state = 123
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorByTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(GrammarParser.TEXT, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def selectorOrder(self):
            return self.getTypedRuleContext(GrammarParser.SelectorOrderContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_selectorByText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorByText" ):
                listener.enterSelectorByText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorByText" ):
                listener.exitSelectorByText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorByText" ):
                return visitor.visitSelectorByText(self)
            else:
                return visitor.visitChildren(self)




    def selectorByText(self):

        localctx = GrammarParser.SelectorByTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_selectorByText)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(GrammarParser.TEXT)
            self.state = 126
            self.match(GrammarParser.ORPAR)
            self.state = 127
            self.match(GrammarParser.STRING)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 128
                self.match(GrammarParser.COMMA)
                self.state = 129
                self.selectorOrder()


            self.state = 132
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorByRegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGEX(self):
            return self.getToken(GrammarParser.REGEX, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def selectorOrder(self):
            return self.getTypedRuleContext(GrammarParser.SelectorOrderContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_selectorByRegex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorByRegex" ):
                listener.enterSelectorByRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorByRegex" ):
                listener.exitSelectorByRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorByRegex" ):
                return visitor.visitSelectorByRegex(self)
            else:
                return visitor.visitChildren(self)




    def selectorByRegex(self):

        localctx = GrammarParser.SelectorByRegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_selectorByRegex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(GrammarParser.REGEX)
            self.state = 135
            self.match(GrammarParser.ORPAR)
            self.state = 136
            self.match(GrammarParser.STRING)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 137
                self.match(GrammarParser.COMMA)
                self.state = 138
                self.selectorOrder()


            self.state = 141
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorByPositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITION(self):
            return self.getToken(GrammarParser.POSITION, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.NumberContext)
            else:
                return self.getTypedRuleContext(GrammarParser.NumberContext,i)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_selectorByPosition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorByPosition" ):
                listener.enterSelectorByPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorByPosition" ):
                listener.exitSelectorByPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorByPosition" ):
                return visitor.visitSelectorByPosition(self)
            else:
                return visitor.visitChildren(self)




    def selectorByPosition(self):

        localctx = GrammarParser.SelectorByPositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_selectorByPosition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(GrammarParser.POSITION)
            self.state = 144
            self.match(GrammarParser.ORPAR)
            self.state = 145
            self.number()
            self.state = 146
            self.match(GrammarParser.COMMA)
            self.state = 147
            self.number()
            self.state = 148
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorOrderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_selectorOrder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorOrder" ):
                listener.enterSelectorOrder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorOrder" ):
                listener.exitSelectorOrder(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorOrder" ):
                return visitor.visitSelectorOrder(self)
            else:
                return visitor.visitChildren(self)




    def selectorOrder(self):

        localctx = GrammarParser.SelectorOrderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_selectorOrder)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GrammarParser.INT)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 151
                self.match(GrammarParser.COMMA)
                self.state = 152
                self.match(GrammarParser.INT)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateScenarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.ID)
            else:
                return self.getToken(GrammarParser.ID, i)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def SCENARIO(self):
            return self.getToken(GrammarParser.SCENARIO, 0)

        def OCPAR(self):
            return self.getToken(GrammarParser.OCPAR, 0)

        def CCPAR(self):
            return self.getToken(GrammarParser.CCPAR, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ActionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ActionContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_createScenario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateScenario" ):
                listener.enterCreateScenario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateScenario" ):
                listener.exitCreateScenario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateScenario" ):
                return visitor.visitCreateScenario(self)
            else:
                return visitor.visitChildren(self)




    def createScenario(self):

        localctx = GrammarParser.CreateScenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_createScenario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(GrammarParser.ID)
            self.state = 159
            self.match(GrammarParser.EQ)
            self.state = 160
            self.match(GrammarParser.SCENARIO)
            self.state = 161
            self.match(GrammarParser.OCPAR)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2105264) != 0):
                self.state = 164
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 7, 8, 9, 10, 11, 12]:
                    self.state = 162
                    self.action()
                    pass
                elif token in [21]:
                    self.state = 163
                    self.match(GrammarParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(GrammarParser.CCPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wait(self):
            return self.getTypedRuleContext(GrammarParser.WaitContext,0)


        def waitSelector(self):
            return self.getTypedRuleContext(GrammarParser.WaitSelectorContext,0)


        def mousePress(self):
            return self.getTypedRuleContext(GrammarParser.MousePressContext,0)


        def mousePressSelector(self):
            return self.getTypedRuleContext(GrammarParser.MousePressSelectorContext,0)


        def mouseReleaseSelector(self):
            return self.getTypedRuleContext(GrammarParser.MouseReleaseSelectorContext,0)


        def mouseClick(self):
            return self.getTypedRuleContext(GrammarParser.MouseClickContext,0)


        def mouseClickSelector(self):
            return self.getTypedRuleContext(GrammarParser.MouseClickSelectorContext,0)


        def mouseDoubleClick(self):
            return self.getTypedRuleContext(GrammarParser.MouseDoubleClickContext,0)


        def mouseDoubleClickSelector(self):
            return self.getTypedRuleContext(GrammarParser.MouseDoubleClickSelectorContext,0)


        def mouseRelease(self):
            return self.getTypedRuleContext(GrammarParser.MouseReleaseContext,0)


        def mouseScroll(self):
            return self.getTypedRuleContext(GrammarParser.MouseScrollContext,0)


        def keyPress(self):
            return self.getTypedRuleContext(GrammarParser.KeyPressContext,0)


        def keyRelease(self):
            return self.getTypedRuleContext(GrammarParser.KeyReleaseContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = GrammarParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_action)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.wait()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.waitSelector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.mousePress()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.mousePressSelector()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.mouseReleaseSelector()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.mouseClick()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 177
                self.mouseClickSelector()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 178
                self.mouseDoubleClick()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 179
                self.mouseDoubleClickSelector()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 180
                self.mouseRelease()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 181
                self.mouseScroll()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 182
                self.keyPress()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 183
                self.keyRelease()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(GrammarParser.WAIT, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_wait

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWait" ):
                listener.enterWait(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWait" ):
                listener.exitWait(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWait" ):
                return visitor.visitWait(self)
            else:
                return visitor.visitChildren(self)




    def wait(self):

        localctx = GrammarParser.WaitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_wait)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(GrammarParser.WAIT)
            self.state = 187
            self.match(GrammarParser.ORPAR)
            self.state = 188
            self.match(GrammarParser.ID)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 189
                self.match(GrammarParser.COMMA)
                self.state = 190
                self.match(GrammarParser.INT)


            self.state = 193
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(GrammarParser.WAIT, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_waitSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitSelector" ):
                listener.enterWaitSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitSelector" ):
                listener.exitWaitSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitSelector" ):
                return visitor.visitWaitSelector(self)
            else:
                return visitor.visitChildren(self)




    def waitSelector(self):

        localctx = GrammarParser.WaitSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_waitSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(GrammarParser.WAIT)
            self.state = 196
            self.match(GrammarParser.ORPAR)
            self.state = 197
            self.selector()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 198
                self.match(GrammarParser.COMMA)
                self.state = 199
                self.match(GrammarParser.INT)


            self.state = 202
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MousePressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_PRESS(self):
            return self.getToken(GrammarParser.MOUSE_PRESS, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mousePress

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMousePress" ):
                listener.enterMousePress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMousePress" ):
                listener.exitMousePress(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMousePress" ):
                return visitor.visitMousePress(self)
            else:
                return visitor.visitChildren(self)




    def mousePress(self):

        localctx = GrammarParser.MousePressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_mousePress)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(GrammarParser.MOUSE_PRESS)
            self.state = 205
            self.match(GrammarParser.ORPAR)
            self.state = 206
            self.match(GrammarParser.ID)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 207
                self.match(GrammarParser.COMMA)
                self.state = 208
                self.mouseButton()


            self.state = 211
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MousePressSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_PRESS(self):
            return self.getToken(GrammarParser.MOUSE_PRESS, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mousePressSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMousePressSelector" ):
                listener.enterMousePressSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMousePressSelector" ):
                listener.exitMousePressSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMousePressSelector" ):
                return visitor.visitMousePressSelector(self)
            else:
                return visitor.visitChildren(self)




    def mousePressSelector(self):

        localctx = GrammarParser.MousePressSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mousePressSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(GrammarParser.MOUSE_PRESS)
            self.state = 214
            self.match(GrammarParser.ORPAR)
            self.state = 215
            self.selector()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 216
                self.match(GrammarParser.COMMA)
                self.state = 217
                self.mouseButton()


            self.state = 220
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseClickContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_CLICK(self):
            return self.getToken(GrammarParser.MOUSE_CLICK, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mouseClick

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseClick" ):
                listener.enterMouseClick(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseClick" ):
                listener.exitMouseClick(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseClick" ):
                return visitor.visitMouseClick(self)
            else:
                return visitor.visitChildren(self)




    def mouseClick(self):

        localctx = GrammarParser.MouseClickContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mouseClick)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(GrammarParser.MOUSE_CLICK)
            self.state = 223
            self.match(GrammarParser.ORPAR)
            self.state = 224
            self.match(GrammarParser.ID)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 225
                self.match(GrammarParser.COMMA)
                self.state = 226
                self.mouseButton()


            self.state = 229
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseClickSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_CLICK(self):
            return self.getToken(GrammarParser.MOUSE_CLICK, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mouseClickSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseClickSelector" ):
                listener.enterMouseClickSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseClickSelector" ):
                listener.exitMouseClickSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseClickSelector" ):
                return visitor.visitMouseClickSelector(self)
            else:
                return visitor.visitChildren(self)




    def mouseClickSelector(self):

        localctx = GrammarParser.MouseClickSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mouseClickSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(GrammarParser.MOUSE_CLICK)
            self.state = 232
            self.match(GrammarParser.ORPAR)
            self.state = 233
            self.selector()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 234
                self.match(GrammarParser.COMMA)
                self.state = 235
                self.mouseButton()


            self.state = 238
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseDoubleClickContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_DOUBLE_CLICK(self):
            return self.getToken(GrammarParser.MOUSE_DOUBLE_CLICK, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mouseDoubleClick

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseDoubleClick" ):
                listener.enterMouseDoubleClick(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseDoubleClick" ):
                listener.exitMouseDoubleClick(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseDoubleClick" ):
                return visitor.visitMouseDoubleClick(self)
            else:
                return visitor.visitChildren(self)




    def mouseDoubleClick(self):

        localctx = GrammarParser.MouseDoubleClickContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_mouseDoubleClick)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(GrammarParser.MOUSE_DOUBLE_CLICK)
            self.state = 241
            self.match(GrammarParser.ORPAR)
            self.state = 242
            self.match(GrammarParser.ID)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 243
                self.match(GrammarParser.COMMA)
                self.state = 244
                self.mouseButton()


            self.state = 247
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseDoubleClickSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_DOUBLE_CLICK(self):
            return self.getToken(GrammarParser.MOUSE_DOUBLE_CLICK, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mouseDoubleClickSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseDoubleClickSelector" ):
                listener.enterMouseDoubleClickSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseDoubleClickSelector" ):
                listener.exitMouseDoubleClickSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseDoubleClickSelector" ):
                return visitor.visitMouseDoubleClickSelector(self)
            else:
                return visitor.visitChildren(self)




    def mouseDoubleClickSelector(self):

        localctx = GrammarParser.MouseDoubleClickSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mouseDoubleClickSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GrammarParser.MOUSE_DOUBLE_CLICK)
            self.state = 250
            self.match(GrammarParser.ORPAR)
            self.state = 251
            self.selector()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 252
                self.match(GrammarParser.COMMA)
                self.state = 253
                self.mouseButton()


            self.state = 256
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseReleaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_RELEASE(self):
            return self.getToken(GrammarParser.MOUSE_RELEASE, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mouseRelease

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseRelease" ):
                listener.enterMouseRelease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseRelease" ):
                listener.exitMouseRelease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseRelease" ):
                return visitor.visitMouseRelease(self)
            else:
                return visitor.visitChildren(self)




    def mouseRelease(self):

        localctx = GrammarParser.MouseReleaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mouseRelease)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 259
            self.match(GrammarParser.ORPAR)
            self.state = 260
            self.match(GrammarParser.ID)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 261
                self.match(GrammarParser.COMMA)
                self.state = 262
                self.mouseButton()


            self.state = 265
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseReleaseSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_RELEASE(self):
            return self.getToken(GrammarParser.MOUSE_RELEASE, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def mouseButton(self):
            return self.getTypedRuleContext(GrammarParser.MouseButtonContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mouseReleaseSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseReleaseSelector" ):
                listener.enterMouseReleaseSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseReleaseSelector" ):
                listener.exitMouseReleaseSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseReleaseSelector" ):
                return visitor.visitMouseReleaseSelector(self)
            else:
                return visitor.visitChildren(self)




    def mouseReleaseSelector(self):

        localctx = GrammarParser.MouseReleaseSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_mouseReleaseSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 268
            self.match(GrammarParser.ORPAR)
            self.state = 269
            self.selector()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 270
                self.match(GrammarParser.COMMA)
                self.state = 271
                self.mouseButton()


            self.state = 274
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseScrollContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_SCROLL(self):
            return self.getToken(GrammarParser.MOUSE_SCROLL, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_mouseScroll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseScroll" ):
                listener.enterMouseScroll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseScroll" ):
                listener.exitMouseScroll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseScroll" ):
                return visitor.visitMouseScroll(self)
            else:
                return visitor.visitChildren(self)




    def mouseScroll(self):

        localctx = GrammarParser.MouseScrollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_mouseScroll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(GrammarParser.MOUSE_SCROLL)
            self.state = 277
            self.match(GrammarParser.ORPAR)
            self.state = 278
            self.match(GrammarParser.ID)
            self.state = 279
            self.match(GrammarParser.COMMA)
            self.state = 280
            self.match(GrammarParser.INT)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 281
                self.match(GrammarParser.COMMA)
                self.state = 282
                self.match(GrammarParser.INT)


            self.state = 285
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyPressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_PRESS(self):
            return self.getToken(GrammarParser.KEY_PRESS, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_keyPress

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyPress" ):
                listener.enterKeyPress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyPress" ):
                listener.exitKeyPress(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyPress" ):
                return visitor.visitKeyPress(self)
            else:
                return visitor.visitChildren(self)




    def keyPress(self):

        localctx = GrammarParser.KeyPressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_keyPress)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(GrammarParser.KEY_PRESS)
            self.state = 288
            self.match(GrammarParser.ORPAR)
            self.state = 289
            self.match(GrammarParser.STRING)
            self.state = 290
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyReleaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_RELEASE(self):
            return self.getToken(GrammarParser.KEY_RELEASE, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_keyRelease

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyRelease" ):
                listener.enterKeyRelease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyRelease" ):
                listener.exitKeyRelease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyRelease" ):
                return visitor.visitKeyRelease(self)
            else:
                return visitor.visitChildren(self)




    def keyRelease(self):

        localctx = GrammarParser.KeyReleaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_keyRelease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(GrammarParser.KEY_RELEASE)
            self.state = 293
            self.match(GrammarParser.ORPAR)
            self.state = 294
            self.match(GrammarParser.STRING)
            self.state = 295
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseButtonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(GrammarParser.LEFT, 0)

        def MIDDLE(self):
            return self.getToken(GrammarParser.MIDDLE, 0)

        def RIGHT(self):
            return self.getToken(GrammarParser.RIGHT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_mouseButton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseButton" ):
                listener.enterMouseButton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseButton" ):
                listener.exitMouseButton(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseButton" ):
                return visitor.visitMouseButton(self)
            else:
                return visitor.visitChildren(self)




    def mouseButton(self):

        localctx = GrammarParser.MouseButtonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_mouseButton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = GrammarParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





