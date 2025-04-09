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
        4,1,31,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,82,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,96,
        8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,122,8,9,1,10,1,10,1,10,1,
        10,1,10,3,10,129,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,138,
        8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,147,8,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,161,8,14,
        10,14,12,14,164,9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,172,8,15,
        10,15,12,15,175,9,15,1,15,1,15,1,16,1,16,3,16,181,8,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,196,
        8,17,1,18,1,18,1,18,1,18,1,18,3,18,203,8,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,3,19,212,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,
        3,20,221,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,21,230,8,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,239,8,22,1,22,1,22,1,23,1,
        23,1,23,1,23,1,23,3,23,248,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,
        24,3,24,257,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,266,8,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,3,26,275,8,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,3,27,284,8,27,1,27,1,27,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,3,28,295,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,
        1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,32,1,32,1,32,0,0,33,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,0,2,1,0,1,3,1,0,29,30,322,0,69,1,0,0,0,2,81,
        1,0,0,0,4,83,1,0,0,0,6,90,1,0,0,0,8,97,1,0,0,0,10,101,1,0,0,0,12,
        105,1,0,0,0,14,109,1,0,0,0,16,113,1,0,0,0,18,121,1,0,0,0,20,123,
        1,0,0,0,22,132,1,0,0,0,24,141,1,0,0,0,26,150,1,0,0,0,28,157,1,0,
        0,0,30,165,1,0,0,0,32,180,1,0,0,0,34,195,1,0,0,0,36,197,1,0,0,0,
        38,206,1,0,0,0,40,215,1,0,0,0,42,224,1,0,0,0,44,233,1,0,0,0,46,242,
        1,0,0,0,48,251,1,0,0,0,50,260,1,0,0,0,52,269,1,0,0,0,54,278,1,0,
        0,0,56,287,1,0,0,0,58,298,1,0,0,0,60,303,1,0,0,0,62,308,1,0,0,0,
        64,310,1,0,0,0,66,68,3,2,1,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,
        0,0,0,69,70,1,0,0,0,70,1,1,0,0,0,71,69,1,0,0,0,72,82,3,4,2,0,73,
        82,3,6,3,0,74,82,3,10,5,0,75,82,3,12,6,0,76,82,3,14,7,0,77,82,3,
        8,4,0,78,82,3,16,8,0,79,82,3,30,15,0,80,82,3,32,16,0,81,72,1,0,0,
        0,81,73,1,0,0,0,81,74,1,0,0,0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,
        1,0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,
        84,5,21,0,0,84,85,5,25,0,0,85,86,5,20,0,0,86,87,5,24,0,0,87,88,5,
        22,0,0,88,89,5,26,0,0,89,5,1,0,0,0,90,91,5,18,0,0,91,95,5,21,0,0,
        92,93,5,24,0,0,93,94,5,30,0,0,94,96,5,26,0,0,95,92,1,0,0,0,95,96,
        1,0,0,0,96,7,1,0,0,0,97,98,5,21,0,0,98,99,5,25,0,0,99,100,3,26,13,
        0,100,9,1,0,0,0,101,102,5,21,0,0,102,103,5,25,0,0,103,104,3,20,10,
        0,104,11,1,0,0,0,105,106,5,21,0,0,106,107,5,25,0,0,107,108,3,22,
        11,0,108,13,1,0,0,0,109,110,5,21,0,0,110,111,5,25,0,0,111,112,3,
        24,12,0,112,15,1,0,0,0,113,114,5,21,0,0,114,115,5,25,0,0,115,116,
        3,34,17,0,116,17,1,0,0,0,117,122,3,20,10,0,118,122,3,22,11,0,119,
        122,3,24,12,0,120,122,3,26,13,0,121,117,1,0,0,0,121,118,1,0,0,0,
        121,119,1,0,0,0,121,120,1,0,0,0,122,19,1,0,0,0,123,124,5,17,0,0,
        124,125,5,24,0,0,125,128,5,22,0,0,126,127,5,16,0,0,127,129,3,28,
        14,0,128,126,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,5,26,
        0,0,131,21,1,0,0,0,132,133,5,13,0,0,133,134,5,24,0,0,134,137,5,22,
        0,0,135,136,5,16,0,0,136,138,3,28,14,0,137,135,1,0,0,0,137,138,1,
        0,0,0,138,139,1,0,0,0,139,140,5,26,0,0,140,23,1,0,0,0,141,142,5,
        15,0,0,142,143,5,24,0,0,143,146,5,22,0,0,144,145,5,16,0,0,145,147,
        3,28,14,0,146,144,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,
        5,26,0,0,149,25,1,0,0,0,150,151,5,14,0,0,151,152,5,24,0,0,152,153,
        3,64,32,0,153,154,5,16,0,0,154,155,3,64,32,0,155,156,5,26,0,0,156,
        27,1,0,0,0,157,162,5,29,0,0,158,159,5,16,0,0,159,161,5,29,0,0,160,
        158,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,
        29,1,0,0,0,164,162,1,0,0,0,165,166,5,21,0,0,166,167,5,25,0,0,167,
        168,5,19,0,0,168,173,5,27,0,0,169,172,3,34,17,0,170,172,5,21,0,0,
        171,169,1,0,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,
        173,174,1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,177,5,28,0,0,
        177,31,1,0,0,0,178,181,3,34,17,0,179,181,5,21,0,0,180,178,1,0,0,
        0,180,179,1,0,0,0,181,33,1,0,0,0,182,196,3,36,18,0,183,196,3,38,
        19,0,184,196,3,40,20,0,185,196,3,42,21,0,186,196,3,54,27,0,187,196,
        3,44,22,0,188,196,3,46,23,0,189,196,3,48,24,0,190,196,3,50,25,0,
        191,196,3,52,26,0,192,196,3,56,28,0,193,196,3,58,29,0,194,196,3,
        60,30,0,195,182,1,0,0,0,195,183,1,0,0,0,195,184,1,0,0,0,195,185,
        1,0,0,0,195,186,1,0,0,0,195,187,1,0,0,0,195,188,1,0,0,0,195,189,
        1,0,0,0,195,190,1,0,0,0,195,191,1,0,0,0,195,192,1,0,0,0,195,193,
        1,0,0,0,195,194,1,0,0,0,196,35,1,0,0,0,197,198,5,12,0,0,198,199,
        5,24,0,0,199,202,5,21,0,0,200,201,5,16,0,0,201,203,5,29,0,0,202,
        200,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,5,26,0,0,205,
        37,1,0,0,0,206,207,5,12,0,0,207,208,5,24,0,0,208,211,3,18,9,0,209,
        210,5,16,0,0,210,212,5,29,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,
        213,1,0,0,0,213,214,5,26,0,0,214,39,1,0,0,0,215,216,5,9,0,0,216,
        217,5,24,0,0,217,220,5,21,0,0,218,219,5,16,0,0,219,221,3,62,31,0,
        220,218,1,0,0,0,220,221,1,0,0,0,221,222,1,0,0,0,222,223,5,26,0,0,
        223,41,1,0,0,0,224,225,5,9,0,0,225,226,5,24,0,0,226,229,3,18,9,0,
        227,228,5,16,0,0,228,230,3,62,31,0,229,227,1,0,0,0,229,230,1,0,0,
        0,230,231,1,0,0,0,231,232,5,26,0,0,232,43,1,0,0,0,233,234,5,7,0,
        0,234,235,5,24,0,0,235,238,5,21,0,0,236,237,5,16,0,0,237,239,3,62,
        31,0,238,236,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,26,
        0,0,241,45,1,0,0,0,242,243,5,7,0,0,243,244,5,24,0,0,244,247,3,18,
        9,0,245,246,5,16,0,0,246,248,3,62,31,0,247,245,1,0,0,0,247,248,1,
        0,0,0,248,249,1,0,0,0,249,250,5,26,0,0,250,47,1,0,0,0,251,252,5,
        8,0,0,252,253,5,24,0,0,253,256,5,21,0,0,254,255,5,16,0,0,255,257,
        3,62,31,0,256,254,1,0,0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,259,
        5,26,0,0,259,49,1,0,0,0,260,261,5,8,0,0,261,262,5,24,0,0,262,265,
        3,18,9,0,263,264,5,16,0,0,264,266,3,62,31,0,265,263,1,0,0,0,265,
        266,1,0,0,0,266,267,1,0,0,0,267,268,5,26,0,0,268,51,1,0,0,0,269,
        270,5,10,0,0,270,271,5,24,0,0,271,274,5,21,0,0,272,273,5,16,0,0,
        273,275,3,62,31,0,274,272,1,0,0,0,274,275,1,0,0,0,275,276,1,0,0,
        0,276,277,5,26,0,0,277,53,1,0,0,0,278,279,5,10,0,0,279,280,5,24,
        0,0,280,283,3,18,9,0,281,282,5,16,0,0,282,284,3,62,31,0,283,281,
        1,0,0,0,283,284,1,0,0,0,284,285,1,0,0,0,285,286,5,26,0,0,286,55,
        1,0,0,0,287,288,5,11,0,0,288,289,5,24,0,0,289,290,5,21,0,0,290,291,
        5,16,0,0,291,294,5,29,0,0,292,293,5,16,0,0,293,295,5,29,0,0,294,
        292,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,297,5,26,0,0,297,
        57,1,0,0,0,298,299,5,4,0,0,299,300,5,24,0,0,300,301,5,22,0,0,301,
        302,5,26,0,0,302,59,1,0,0,0,303,304,5,5,0,0,304,305,5,24,0,0,305,
        306,5,22,0,0,306,307,5,26,0,0,307,61,1,0,0,0,308,309,7,0,0,0,309,
        63,1,0,0,0,310,311,7,1,0,0,311,65,1,0,0,0,23,69,81,95,121,128,137,
        146,162,171,173,180,195,202,211,220,229,238,247,256,265,274,283,
        294
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
                     "'label'", "'use'", "'sequence'", "'detector'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "'='", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", 
                      "KEY_RELEASE", "KEY_TYPE", "MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", 
                      "MOUSE_PRESS", "MOUSE_RELEASE", "MOUSE_SCROLL", "WAIT", 
                      "TEXT", "POSITION", "REGEX", "COMMA", "LABEL", "USE", 
                      "SEQUENCE", "DETECTOR", "ID", "STRING", "ESC", "ORPAR", 
                      "EQ", "CRPAR", "OCPAR", "CCPAR", "INT", "FLOAT", "WS" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_createDetector = 2
    RULE_useDetector = 3
    RULE_createSelectorByPosition = 4
    RULE_createSelectorByLabel = 5
    RULE_createSelectorByText = 6
    RULE_createSelectorByRegex = 7
    RULE_createOperation = 8
    RULE_selector = 9
    RULE_selectorByLabel = 10
    RULE_selectorByText = 11
    RULE_selectorByRegex = 12
    RULE_selectorByPosition = 13
    RULE_selectorOrder = 14
    RULE_createSequence = 15
    RULE_runOperation = 16
    RULE_operation = 17
    RULE_wait = 18
    RULE_waitSelector = 19
    RULE_mousePress = 20
    RULE_mousePressSelector = 21
    RULE_mouseClick = 22
    RULE_mouseClickSelector = 23
    RULE_mouseDoubleClick = 24
    RULE_mouseDoubleClickSelector = 25
    RULE_mouseRelease = 26
    RULE_mouseReleaseSelector = 27
    RULE_mouseScroll = 28
    RULE_keyPress = 29
    RULE_keyRelease = 30
    RULE_mouseButton = 31
    RULE_number = 32

    ruleNames =  [ "root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
                   "createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
                   "createOperation", "selector", "selectorByLabel", "selectorByText", 
                   "selectorByRegex", "selectorByPosition", "selectorOrder", 
                   "createSequence", "runOperation", "operation", "wait", 
                   "waitSelector", "mousePress", "mousePressSelector", "mouseClick", 
                   "mouseClickSelector", "mouseDoubleClick", "mouseDoubleClickSelector", 
                   "mouseRelease", "mouseReleaseSelector", "mouseScroll", 
                   "keyPress", "keyRelease", "mouseButton", "number" ]

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
    SEQUENCE=19
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
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2367408) != 0):
                self.state = 66
                self.stmt()
                self.state = 71
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


        def createOperation(self):
            return self.getTypedRuleContext(GrammarParser.CreateOperationContext,0)


        def createSequence(self):
            return self.getTypedRuleContext(GrammarParser.CreateSequenceContext,0)


        def runOperation(self):
            return self.getTypedRuleContext(GrammarParser.RunOperationContext,0)


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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.createDetector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.useDetector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.createSelectorByLabel()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.createSelectorByText()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.createSelectorByRegex()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.createSelectorByPosition()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.createOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.createSequence()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 80
                self.runOperation()
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
            self.state = 83
            self.match(GrammarParser.ID)
            self.state = 84
            self.match(GrammarParser.EQ)
            self.state = 85
            self.match(GrammarParser.DETECTOR)
            self.state = 86
            self.match(GrammarParser.ORPAR)
            self.state = 87
            self.match(GrammarParser.STRING)
            self.state = 88
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

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(GrammarParser.USE)
            self.state = 91
            self.match(GrammarParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 92
                self.match(GrammarParser.ORPAR)
                self.state = 93
                self.match(GrammarParser.FLOAT)
                self.state = 94
                self.match(GrammarParser.CRPAR)


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
            self.state = 97
            self.match(GrammarParser.ID)
            self.state = 98
            self.match(GrammarParser.EQ)
            self.state = 99
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
            self.state = 101
            self.match(GrammarParser.ID)
            self.state = 102
            self.match(GrammarParser.EQ)
            self.state = 103
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
            self.state = 105
            self.match(GrammarParser.ID)
            self.state = 106
            self.match(GrammarParser.EQ)
            self.state = 107
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
            self.state = 109
            self.match(GrammarParser.ID)
            self.state = 110
            self.match(GrammarParser.EQ)
            self.state = 111
            self.selectorByRegex()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def operation(self):
            return self.getTypedRuleContext(GrammarParser.OperationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_createOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateOperation" ):
                listener.enterCreateOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateOperation" ):
                listener.exitCreateOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateOperation" ):
                return visitor.visitCreateOperation(self)
            else:
                return visitor.visitChildren(self)




    def createOperation(self):

        localctx = GrammarParser.CreateOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_createOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(GrammarParser.ID)
            self.state = 114
            self.match(GrammarParser.EQ)
            self.state = 115
            self.operation()
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.selectorByLabel()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.selectorByText()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.selectorByRegex()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
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
            self.state = 123
            self.match(GrammarParser.LABEL)
            self.state = 124
            self.match(GrammarParser.ORPAR)
            self.state = 125
            self.match(GrammarParser.STRING)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 126
                self.match(GrammarParser.COMMA)
                self.state = 127
                self.selectorOrder()


            self.state = 130
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
            self.state = 132
            self.match(GrammarParser.TEXT)
            self.state = 133
            self.match(GrammarParser.ORPAR)
            self.state = 134
            self.match(GrammarParser.STRING)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 135
                self.match(GrammarParser.COMMA)
                self.state = 136
                self.selectorOrder()


            self.state = 139
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
            self.state = 141
            self.match(GrammarParser.REGEX)
            self.state = 142
            self.match(GrammarParser.ORPAR)
            self.state = 143
            self.match(GrammarParser.STRING)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 144
                self.match(GrammarParser.COMMA)
                self.state = 145
                self.selectorOrder()


            self.state = 148
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
            self.state = 150
            self.match(GrammarParser.POSITION)
            self.state = 151
            self.match(GrammarParser.ORPAR)
            self.state = 152
            self.number()
            self.state = 153
            self.match(GrammarParser.COMMA)
            self.state = 154
            self.number()
            self.state = 155
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
            self.state = 157
            self.match(GrammarParser.INT)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 158
                self.match(GrammarParser.COMMA)
                self.state = 159
                self.match(GrammarParser.INT)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSequenceContext(ParserRuleContext):
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

        def SEQUENCE(self):
            return self.getToken(GrammarParser.SEQUENCE, 0)

        def OCPAR(self):
            return self.getToken(GrammarParser.OCPAR, 0)

        def CCPAR(self):
            return self.getToken(GrammarParser.CCPAR, 0)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.OperationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.OperationContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_createSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSequence" ):
                listener.enterCreateSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSequence" ):
                listener.exitCreateSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSequence" ):
                return visitor.visitCreateSequence(self)
            else:
                return visitor.visitChildren(self)




    def createSequence(self):

        localctx = GrammarParser.CreateSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_createSequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(GrammarParser.ID)
            self.state = 166
            self.match(GrammarParser.EQ)
            self.state = 167
            self.match(GrammarParser.SEQUENCE)
            self.state = 168
            self.match(GrammarParser.OCPAR)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2105264) != 0):
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 7, 8, 9, 10, 11, 12]:
                    self.state = 169
                    self.operation()
                    pass
                elif token in [21]:
                    self.state = 170
                    self.match(GrammarParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(GrammarParser.CCPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(GrammarParser.OperationContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_runOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRunOperation" ):
                listener.enterRunOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRunOperation" ):
                listener.exitRunOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRunOperation" ):
                return visitor.visitRunOperation(self)
            else:
                return visitor.visitChildren(self)




    def runOperation(self):

        localctx = GrammarParser.RunOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_runOperation)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 7, 8, 9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.operation()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(GrammarParser.ID)
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


    class OperationContext(ParserRuleContext):
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
            return GrammarParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = GrammarParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operation)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.wait()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.waitSelector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.mousePress()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.mousePressSelector()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.mouseReleaseSelector()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 187
                self.mouseClick()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 188
                self.mouseClickSelector()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.mouseDoubleClick()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 190
                self.mouseDoubleClickSelector()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 191
                self.mouseRelease()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 192
                self.mouseScroll()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 193
                self.keyPress()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 194
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
        self.enterRule(localctx, 36, self.RULE_wait)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(GrammarParser.WAIT)
            self.state = 198
            self.match(GrammarParser.ORPAR)
            self.state = 199
            self.match(GrammarParser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 200
                self.match(GrammarParser.COMMA)
                self.state = 201
                self.match(GrammarParser.INT)


            self.state = 204
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
        self.enterRule(localctx, 38, self.RULE_waitSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(GrammarParser.WAIT)
            self.state = 207
            self.match(GrammarParser.ORPAR)
            self.state = 208
            self.selector()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 209
                self.match(GrammarParser.COMMA)
                self.state = 210
                self.match(GrammarParser.INT)


            self.state = 213
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
        self.enterRule(localctx, 40, self.RULE_mousePress)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(GrammarParser.MOUSE_PRESS)
            self.state = 216
            self.match(GrammarParser.ORPAR)
            self.state = 217
            self.match(GrammarParser.ID)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 218
                self.match(GrammarParser.COMMA)
                self.state = 219
                self.mouseButton()


            self.state = 222
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
        self.enterRule(localctx, 42, self.RULE_mousePressSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(GrammarParser.MOUSE_PRESS)
            self.state = 225
            self.match(GrammarParser.ORPAR)
            self.state = 226
            self.selector()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 227
                self.match(GrammarParser.COMMA)
                self.state = 228
                self.mouseButton()


            self.state = 231
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
        self.enterRule(localctx, 44, self.RULE_mouseClick)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(GrammarParser.MOUSE_CLICK)
            self.state = 234
            self.match(GrammarParser.ORPAR)
            self.state = 235
            self.match(GrammarParser.ID)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 236
                self.match(GrammarParser.COMMA)
                self.state = 237
                self.mouseButton()


            self.state = 240
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
        self.enterRule(localctx, 46, self.RULE_mouseClickSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(GrammarParser.MOUSE_CLICK)
            self.state = 243
            self.match(GrammarParser.ORPAR)
            self.state = 244
            self.selector()
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 245
                self.match(GrammarParser.COMMA)
                self.state = 246
                self.mouseButton()


            self.state = 249
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
        self.enterRule(localctx, 48, self.RULE_mouseDoubleClick)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(GrammarParser.MOUSE_DOUBLE_CLICK)
            self.state = 252
            self.match(GrammarParser.ORPAR)
            self.state = 253
            self.match(GrammarParser.ID)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 254
                self.match(GrammarParser.COMMA)
                self.state = 255
                self.mouseButton()


            self.state = 258
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
        self.enterRule(localctx, 50, self.RULE_mouseDoubleClickSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(GrammarParser.MOUSE_DOUBLE_CLICK)
            self.state = 261
            self.match(GrammarParser.ORPAR)
            self.state = 262
            self.selector()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 263
                self.match(GrammarParser.COMMA)
                self.state = 264
                self.mouseButton()


            self.state = 267
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
        self.enterRule(localctx, 52, self.RULE_mouseRelease)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 270
            self.match(GrammarParser.ORPAR)
            self.state = 271
            self.match(GrammarParser.ID)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 272
                self.match(GrammarParser.COMMA)
                self.state = 273
                self.mouseButton()


            self.state = 276
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
        self.enterRule(localctx, 54, self.RULE_mouseReleaseSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 279
            self.match(GrammarParser.ORPAR)
            self.state = 280
            self.selector()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 281
                self.match(GrammarParser.COMMA)
                self.state = 282
                self.mouseButton()


            self.state = 285
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
        self.enterRule(localctx, 56, self.RULE_mouseScroll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(GrammarParser.MOUSE_SCROLL)
            self.state = 288
            self.match(GrammarParser.ORPAR)
            self.state = 289
            self.match(GrammarParser.ID)
            self.state = 290
            self.match(GrammarParser.COMMA)
            self.state = 291
            self.match(GrammarParser.INT)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 292
                self.match(GrammarParser.COMMA)
                self.state = 293
                self.match(GrammarParser.INT)


            self.state = 296
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
        self.enterRule(localctx, 58, self.RULE_keyPress)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(GrammarParser.KEY_PRESS)
            self.state = 299
            self.match(GrammarParser.ORPAR)
            self.state = 300
            self.match(GrammarParser.STRING)
            self.state = 301
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
        self.enterRule(localctx, 60, self.RULE_keyRelease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(GrammarParser.KEY_RELEASE)
            self.state = 304
            self.match(GrammarParser.ORPAR)
            self.state = 305
            self.match(GrammarParser.STRING)
            self.state = 306
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
        self.enterRule(localctx, 62, self.RULE_mouseButton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
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
        self.enterRule(localctx, 64, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
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





