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
        4,1,27,188,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,102,
        8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,122,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,136,8,11,1,12,1,12,1,12,1,12,1,12,3,12,143,
        8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,152,8,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,3,14,161,8,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,172,8,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,0,0,19,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,1,0,1,3,189,0,41,1,0,
        0,0,2,53,1,0,0,0,4,55,1,0,0,0,6,62,1,0,0,0,8,65,1,0,0,0,10,72,1,
        0,0,0,12,85,1,0,0,0,14,92,1,0,0,0,16,105,1,0,0,0,18,112,1,0,0,0,
        20,125,1,0,0,0,22,135,1,0,0,0,24,137,1,0,0,0,26,146,1,0,0,0,28,155,
        1,0,0,0,30,164,1,0,0,0,32,175,1,0,0,0,34,180,1,0,0,0,36,185,1,0,
        0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,1,1,0,0,0,43,41,1,0,0,0,44,54,3,4,2,0,45,54,3,6,3,0,46,
        54,3,8,4,0,47,54,3,10,5,0,48,54,3,12,6,0,49,54,3,14,7,0,50,54,3,
        16,8,0,51,54,3,18,9,0,52,54,3,20,10,0,53,44,1,0,0,0,53,45,1,0,0,
        0,53,46,1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,53,50,
        1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,0,55,56,5,20,0,0,
        56,57,5,24,0,0,57,58,5,19,0,0,58,59,5,23,0,0,59,60,5,21,0,0,60,61,
        5,25,0,0,61,5,1,0,0,0,62,63,5,18,0,0,63,64,5,20,0,0,64,7,1,0,0,0,
        65,66,5,20,0,0,66,67,5,24,0,0,67,68,5,17,0,0,68,69,5,23,0,0,69,70,
        5,21,0,0,70,71,5,25,0,0,71,9,1,0,0,0,72,73,5,20,0,0,73,74,5,24,0,
        0,74,75,5,16,0,0,75,76,5,23,0,0,76,77,5,21,0,0,77,78,5,15,0,0,78,
        81,5,26,0,0,79,80,5,15,0,0,80,82,5,26,0,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,83,1,0,0,0,83,84,5,25,0,0,84,11,1,0,0,0,85,86,5,20,0,0,
        86,87,5,24,0,0,87,88,5,11,0,0,88,89,5,23,0,0,89,90,5,21,0,0,90,91,
        5,25,0,0,91,13,1,0,0,0,92,93,5,20,0,0,93,94,5,24,0,0,94,95,5,14,
        0,0,95,96,5,23,0,0,96,97,5,21,0,0,97,98,5,15,0,0,98,101,5,26,0,0,
        99,100,5,15,0,0,100,102,5,26,0,0,101,99,1,0,0,0,101,102,1,0,0,0,
        102,103,1,0,0,0,103,104,5,25,0,0,104,15,1,0,0,0,105,106,5,20,0,0,
        106,107,5,24,0,0,107,108,5,12,0,0,108,109,5,23,0,0,109,110,5,21,
        0,0,110,111,5,25,0,0,111,17,1,0,0,0,112,113,5,20,0,0,113,114,5,24,
        0,0,114,115,5,13,0,0,115,116,5,23,0,0,116,117,5,21,0,0,117,118,5,
        15,0,0,118,121,5,26,0,0,119,120,5,15,0,0,120,122,5,26,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,5,25,0,0,124,19,
        1,0,0,0,125,126,5,20,0,0,126,127,5,24,0,0,127,128,3,22,11,0,128,
        21,1,0,0,0,129,136,3,24,12,0,130,136,3,26,13,0,131,136,3,28,14,0,
        132,136,3,30,15,0,133,136,3,32,16,0,134,136,3,34,17,0,135,129,1,
        0,0,0,135,130,1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,135,133,1,
        0,0,0,135,134,1,0,0,0,136,23,1,0,0,0,137,138,5,10,0,0,138,139,5,
        23,0,0,139,142,5,20,0,0,140,141,5,15,0,0,141,143,5,26,0,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,5,25,0,0,145,25,
        1,0,0,0,146,147,5,7,0,0,147,148,5,23,0,0,148,151,5,20,0,0,149,150,
        5,15,0,0,150,152,3,36,18,0,151,149,1,0,0,0,151,152,1,0,0,0,152,153,
        1,0,0,0,153,154,5,25,0,0,154,27,1,0,0,0,155,156,5,8,0,0,156,157,
        5,23,0,0,157,160,5,20,0,0,158,159,5,15,0,0,159,161,3,36,18,0,160,
        158,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,163,5,25,0,0,163,
        29,1,0,0,0,164,165,5,9,0,0,165,166,5,23,0,0,166,167,5,20,0,0,167,
        168,5,15,0,0,168,171,5,26,0,0,169,170,5,15,0,0,170,172,5,26,0,0,
        171,169,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,25,0,0,
        174,31,1,0,0,0,175,176,5,4,0,0,176,177,5,23,0,0,177,178,5,21,0,0,
        178,179,5,25,0,0,179,33,1,0,0,0,180,181,5,5,0,0,181,182,5,23,0,0,
        182,183,5,21,0,0,183,184,5,25,0,0,184,35,1,0,0,0,185,186,7,0,0,0,
        186,37,1,0,0,0,10,41,53,81,101,121,135,142,151,160,171
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'left'", "'right'", "'middle'", "'keyPress'", 
                     "'keyRelease'", "'keyType'", "'mousePress'", "'mouseRelease'", 
                     "'mouseScroll'", "'wait'", "'text'", "'regex'", "'regexes'", 
                     "'texts'", "','", "'labels'", "'label'", "'use'", "'detector'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "'='", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", 
                      "KEY_RELEASE", "KEY_TYPE", "MOUSE_PRESS", "MOUSE_RELEASE", 
                      "MOUSE_SCROLL", "WAIT", "TEXT", "REGEX", "REGEXES", 
                      "TEXTS", "COMMA", "LABELS", "LABEL", "USE", "DETECTOR", 
                      "ID", "STRING", "ESC", "ORPAR", "EQ", "CRPAR", "INT", 
                      "WS" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_createDetector = 2
    RULE_useDetector = 3
    RULE_createSelectorByLabel = 4
    RULE_createSelectorByLabels = 5
    RULE_createSelectorByText = 6
    RULE_createSelectorByTexts = 7
    RULE_createSelectorByRegex = 8
    RULE_createSelectorByRegexes = 9
    RULE_createStep = 10
    RULE_action = 11
    RULE_waitSelector = 12
    RULE_mousePress = 13
    RULE_mouseRelease = 14
    RULE_mouseScroll = 15
    RULE_keyPress = 16
    RULE_keyRelease = 17
    RULE_mouseButton = 18

    ruleNames =  [ "root", "stmt", "createDetector", "useDetector", "createSelectorByLabel", 
                   "createSelectorByLabels", "createSelectorByText", "createSelectorByTexts", 
                   "createSelectorByRegex", "createSelectorByRegexes", "createStep", 
                   "action", "waitSelector", "mousePress", "mouseRelease", 
                   "mouseScroll", "keyPress", "keyRelease", "mouseButton" ]

    EOF = Token.EOF
    LEFT=1
    RIGHT=2
    MIDDLE=3
    KEY_PRESS=4
    KEY_RELEASE=5
    KEY_TYPE=6
    MOUSE_PRESS=7
    MOUSE_RELEASE=8
    MOUSE_SCROLL=9
    WAIT=10
    TEXT=11
    REGEX=12
    REGEXES=13
    TEXTS=14
    COMMA=15
    LABELS=16
    LABEL=17
    USE=18
    DETECTOR=19
    ID=20
    STRING=21
    ESC=22
    ORPAR=23
    EQ=24
    CRPAR=25
    INT=26
    WS=27

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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==20:
                self.state = 38
                self.stmt()
                self.state = 43
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


        def createSelectorByLabels(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByLabelsContext,0)


        def createSelectorByText(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByTextContext,0)


        def createSelectorByTexts(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByTextsContext,0)


        def createSelectorByRegex(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByRegexContext,0)


        def createSelectorByRegexes(self):
            return self.getTypedRuleContext(GrammarParser.CreateSelectorByRegexesContext,0)


        def createStep(self):
            return self.getTypedRuleContext(GrammarParser.CreateStepContext,0)


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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.createDetector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.useDetector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.createSelectorByLabel()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.createSelectorByLabels()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.createSelectorByText()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.createSelectorByTexts()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.createSelectorByRegex()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 51
                self.createSelectorByRegexes()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 52
                self.createStep()
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
            self.state = 55
            self.match(GrammarParser.ID)
            self.state = 56
            self.match(GrammarParser.EQ)
            self.state = 57
            self.match(GrammarParser.DETECTOR)
            self.state = 58
            self.match(GrammarParser.ORPAR)
            self.state = 59
            self.match(GrammarParser.STRING)
            self.state = 60
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
            self.state = 62
            self.match(GrammarParser.USE)
            self.state = 63
            self.match(GrammarParser.ID)
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

        def LABEL(self):
            return self.getToken(GrammarParser.LABEL, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

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
        self.enterRule(localctx, 8, self.RULE_createSelectorByLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(GrammarParser.ID)
            self.state = 66
            self.match(GrammarParser.EQ)
            self.state = 67
            self.match(GrammarParser.LABEL)
            self.state = 68
            self.match(GrammarParser.ORPAR)
            self.state = 69
            self.match(GrammarParser.STRING)
            self.state = 70
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByLabelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def LABELS(self):
            return self.getToken(GrammarParser.LABELS, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

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
            return GrammarParser.RULE_createSelectorByLabels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByLabels" ):
                listener.enterCreateSelectorByLabels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByLabels" ):
                listener.exitCreateSelectorByLabels(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByLabels" ):
                return visitor.visitCreateSelectorByLabels(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByLabels(self):

        localctx = GrammarParser.CreateSelectorByLabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_createSelectorByLabels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(GrammarParser.ID)
            self.state = 73
            self.match(GrammarParser.EQ)
            self.state = 74
            self.match(GrammarParser.LABELS)
            self.state = 75
            self.match(GrammarParser.ORPAR)
            self.state = 76
            self.match(GrammarParser.STRING)
            self.state = 77
            self.match(GrammarParser.COMMA)
            self.state = 78
            self.match(GrammarParser.INT)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 79
                self.match(GrammarParser.COMMA)
                self.state = 80
                self.match(GrammarParser.INT)


            self.state = 83
            self.match(GrammarParser.CRPAR)
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

        def TEXT(self):
            return self.getToken(GrammarParser.TEXT, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

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
            self.state = 85
            self.match(GrammarParser.ID)
            self.state = 86
            self.match(GrammarParser.EQ)
            self.state = 87
            self.match(GrammarParser.TEXT)
            self.state = 88
            self.match(GrammarParser.ORPAR)
            self.state = 89
            self.match(GrammarParser.STRING)
            self.state = 90
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByTextsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def TEXTS(self):
            return self.getToken(GrammarParser.TEXTS, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

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
            return GrammarParser.RULE_createSelectorByTexts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByTexts" ):
                listener.enterCreateSelectorByTexts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByTexts" ):
                listener.exitCreateSelectorByTexts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByTexts" ):
                return visitor.visitCreateSelectorByTexts(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByTexts(self):

        localctx = GrammarParser.CreateSelectorByTextsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_createSelectorByTexts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(GrammarParser.ID)
            self.state = 93
            self.match(GrammarParser.EQ)
            self.state = 94
            self.match(GrammarParser.TEXTS)
            self.state = 95
            self.match(GrammarParser.ORPAR)
            self.state = 96
            self.match(GrammarParser.STRING)
            self.state = 97
            self.match(GrammarParser.COMMA)
            self.state = 98
            self.match(GrammarParser.INT)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 99
                self.match(GrammarParser.COMMA)
                self.state = 100
                self.match(GrammarParser.INT)


            self.state = 103
            self.match(GrammarParser.CRPAR)
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

        def REGEX(self):
            return self.getToken(GrammarParser.REGEX, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

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
        self.enterRule(localctx, 16, self.RULE_createSelectorByRegex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(GrammarParser.ID)
            self.state = 106
            self.match(GrammarParser.EQ)
            self.state = 107
            self.match(GrammarParser.REGEX)
            self.state = 108
            self.match(GrammarParser.ORPAR)
            self.state = 109
            self.match(GrammarParser.STRING)
            self.state = 110
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateSelectorByRegexesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def REGEXES(self):
            return self.getToken(GrammarParser.REGEXES, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

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
            return GrammarParser.RULE_createSelectorByRegexes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateSelectorByRegexes" ):
                listener.enterCreateSelectorByRegexes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateSelectorByRegexes" ):
                listener.exitCreateSelectorByRegexes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateSelectorByRegexes" ):
                return visitor.visitCreateSelectorByRegexes(self)
            else:
                return visitor.visitChildren(self)




    def createSelectorByRegexes(self):

        localctx = GrammarParser.CreateSelectorByRegexesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_createSelectorByRegexes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(GrammarParser.ID)
            self.state = 113
            self.match(GrammarParser.EQ)
            self.state = 114
            self.match(GrammarParser.REGEXES)
            self.state = 115
            self.match(GrammarParser.ORPAR)
            self.state = 116
            self.match(GrammarParser.STRING)
            self.state = 117
            self.match(GrammarParser.COMMA)
            self.state = 118
            self.match(GrammarParser.INT)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 119
                self.match(GrammarParser.COMMA)
                self.state = 120
                self.match(GrammarParser.INT)


            self.state = 123
            self.match(GrammarParser.CRPAR)
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
        self.enterRule(localctx, 20, self.RULE_createStep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(GrammarParser.ID)
            self.state = 126
            self.match(GrammarParser.EQ)
            self.state = 127
            self.action()
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

        def waitSelector(self):
            return self.getTypedRuleContext(GrammarParser.WaitSelectorContext,0)


        def mousePress(self):
            return self.getTypedRuleContext(GrammarParser.MousePressContext,0)


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
        self.enterRule(localctx, 22, self.RULE_action)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.waitSelector()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.mousePress()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.mouseRelease()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.mouseScroll()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.keyPress()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.keyRelease()
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


    class WaitSelectorContext(ParserRuleContext):
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
        self.enterRule(localctx, 24, self.RULE_waitSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(GrammarParser.WAIT)
            self.state = 138
            self.match(GrammarParser.ORPAR)
            self.state = 139
            self.match(GrammarParser.ID)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 140
                self.match(GrammarParser.COMMA)
                self.state = 141
                self.match(GrammarParser.INT)


            self.state = 144
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
        self.enterRule(localctx, 26, self.RULE_mousePress)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(GrammarParser.MOUSE_PRESS)
            self.state = 147
            self.match(GrammarParser.ORPAR)
            self.state = 148
            self.match(GrammarParser.ID)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 149
                self.match(GrammarParser.COMMA)
                self.state = 150
                self.mouseButton()


            self.state = 153
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
        self.enterRule(localctx, 28, self.RULE_mouseRelease)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 156
            self.match(GrammarParser.ORPAR)
            self.state = 157
            self.match(GrammarParser.ID)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 158
                self.match(GrammarParser.COMMA)
                self.state = 159
                self.mouseButton()


            self.state = 162
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
        self.enterRule(localctx, 30, self.RULE_mouseScroll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(GrammarParser.MOUSE_SCROLL)
            self.state = 165
            self.match(GrammarParser.ORPAR)
            self.state = 166
            self.match(GrammarParser.ID)
            self.state = 167
            self.match(GrammarParser.COMMA)
            self.state = 168
            self.match(GrammarParser.INT)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 169
                self.match(GrammarParser.COMMA)
                self.state = 170
                self.match(GrammarParser.INT)


            self.state = 173
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
        self.enterRule(localctx, 32, self.RULE_keyPress)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(GrammarParser.KEY_PRESS)
            self.state = 176
            self.match(GrammarParser.ORPAR)
            self.state = 177
            self.match(GrammarParser.STRING)
            self.state = 178
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
        self.enterRule(localctx, 34, self.RULE_keyRelease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(GrammarParser.KEY_RELEASE)
            self.state = 181
            self.match(GrammarParser.ORPAR)
            self.state = 182
            self.match(GrammarParser.STRING)
            self.state = 183
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
        self.enterRule(localctx, 36, self.RULE_mouseButton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
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





