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
        4,1,32,381,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,5,0,78,8,0,10,0,
        12,0,81,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,107,8,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,140,8,
        9,1,10,1,10,1,10,1,10,1,10,3,10,147,8,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,3,11,156,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,
        165,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,5,14,179,8,14,10,14,12,14,182,9,14,1,15,1,15,1,15,1,15,1,15,
        5,15,189,8,15,10,15,12,15,192,9,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,3,16,201,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,221,8,17,1,18,
        1,18,1,18,1,18,1,18,3,18,228,8,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,3,19,237,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,246,8,
        20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,21,255,8,21,1,21,1,21,1,
        22,1,22,1,22,1,22,1,22,3,22,264,8,22,1,22,1,22,1,23,1,23,1,23,1,
        23,1,23,3,23,273,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,282,
        8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,291,8,25,1,25,1,25,
        1,26,1,26,1,26,1,26,1,26,3,26,300,8,26,1,26,1,26,1,27,1,27,1,27,
        1,27,1,27,3,27,309,8,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,3,28,320,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        3,29,331,8,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,37,
        0,0,38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,0,2,1,0,1,3,1,
        0,30,31,390,0,79,1,0,0,0,2,91,1,0,0,0,4,93,1,0,0,0,6,101,1,0,0,0,
        8,110,1,0,0,0,10,115,1,0,0,0,12,120,1,0,0,0,14,125,1,0,0,0,16,130,
        1,0,0,0,18,139,1,0,0,0,20,141,1,0,0,0,22,150,1,0,0,0,24,159,1,0,
        0,0,26,168,1,0,0,0,28,175,1,0,0,0,30,183,1,0,0,0,32,200,1,0,0,0,
        34,220,1,0,0,0,36,222,1,0,0,0,38,231,1,0,0,0,40,240,1,0,0,0,42,249,
        1,0,0,0,44,258,1,0,0,0,46,267,1,0,0,0,48,276,1,0,0,0,50,285,1,0,
        0,0,52,294,1,0,0,0,54,303,1,0,0,0,56,312,1,0,0,0,58,323,1,0,0,0,
        60,334,1,0,0,0,62,341,1,0,0,0,64,348,1,0,0,0,66,355,1,0,0,0,68,362,
        1,0,0,0,70,369,1,0,0,0,72,376,1,0,0,0,74,378,1,0,0,0,76,78,3,2,1,
        0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,1,1,
        0,0,0,81,79,1,0,0,0,82,92,3,4,2,0,83,92,3,6,3,0,84,92,3,10,5,0,85,
        92,3,12,6,0,86,92,3,14,7,0,87,92,3,8,4,0,88,92,3,16,8,0,89,92,3,
        30,15,0,90,92,3,32,16,0,91,82,1,0,0,0,91,83,1,0,0,0,91,84,1,0,0,
        0,91,85,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,
        1,0,0,0,91,90,1,0,0,0,92,3,1,0,0,0,93,94,5,22,0,0,94,95,5,26,0,0,
        95,96,5,21,0,0,96,97,5,25,0,0,97,98,5,23,0,0,98,99,5,27,0,0,99,100,
        5,17,0,0,100,5,1,0,0,0,101,102,5,19,0,0,102,106,5,22,0,0,103,104,
        5,25,0,0,104,105,5,31,0,0,105,107,5,27,0,0,106,103,1,0,0,0,106,107,
        1,0,0,0,107,108,1,0,0,0,108,109,5,17,0,0,109,7,1,0,0,0,110,111,5,
        22,0,0,111,112,5,26,0,0,112,113,3,26,13,0,113,114,5,17,0,0,114,9,
        1,0,0,0,115,116,5,22,0,0,116,117,5,26,0,0,117,118,3,20,10,0,118,
        119,5,17,0,0,119,11,1,0,0,0,120,121,5,22,0,0,121,122,5,26,0,0,122,
        123,3,22,11,0,123,124,5,17,0,0,124,13,1,0,0,0,125,126,5,22,0,0,126,
        127,5,26,0,0,127,128,3,24,12,0,128,129,5,17,0,0,129,15,1,0,0,0,130,
        131,5,22,0,0,131,132,5,26,0,0,132,133,3,34,17,0,133,134,5,17,0,0,
        134,17,1,0,0,0,135,140,3,20,10,0,136,140,3,22,11,0,137,140,3,24,
        12,0,138,140,3,26,13,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,
        0,0,0,139,138,1,0,0,0,140,19,1,0,0,0,141,142,5,18,0,0,142,143,5,
        25,0,0,143,146,5,23,0,0,144,145,5,16,0,0,145,147,3,28,14,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,5,27,0,0,149,21,
        1,0,0,0,150,151,5,13,0,0,151,152,5,25,0,0,152,155,5,23,0,0,153,154,
        5,16,0,0,154,156,3,28,14,0,155,153,1,0,0,0,155,156,1,0,0,0,156,157,
        1,0,0,0,157,158,5,27,0,0,158,23,1,0,0,0,159,160,5,15,0,0,160,161,
        5,25,0,0,161,164,5,23,0,0,162,163,5,16,0,0,163,165,3,28,14,0,164,
        162,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,5,27,0,0,167,
        25,1,0,0,0,168,169,5,14,0,0,169,170,5,25,0,0,170,171,3,74,37,0,171,
        172,5,16,0,0,172,173,3,74,37,0,173,174,5,27,0,0,174,27,1,0,0,0,175,
        180,5,30,0,0,176,177,5,16,0,0,177,179,5,30,0,0,178,176,1,0,0,0,179,
        182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,29,1,0,0,0,182,180,
        1,0,0,0,183,184,5,22,0,0,184,185,5,26,0,0,185,186,5,20,0,0,186,190,
        5,28,0,0,187,189,3,2,1,0,188,187,1,0,0,0,189,192,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,190,1,0,0,0,193,194,
        5,29,0,0,194,31,1,0,0,0,195,196,3,34,17,0,196,197,5,17,0,0,197,201,
        1,0,0,0,198,199,5,22,0,0,199,201,5,17,0,0,200,195,1,0,0,0,200,198,
        1,0,0,0,201,33,1,0,0,0,202,221,3,36,18,0,203,221,3,38,19,0,204,221,
        3,40,20,0,205,221,3,42,21,0,206,221,3,54,27,0,207,221,3,44,22,0,
        208,221,3,46,23,0,209,221,3,48,24,0,210,221,3,50,25,0,211,221,3,
        52,26,0,212,221,3,56,28,0,213,221,3,58,29,0,214,221,3,60,30,0,215,
        221,3,62,31,0,216,221,3,64,32,0,217,221,3,66,33,0,218,221,3,68,34,
        0,219,221,3,70,35,0,220,202,1,0,0,0,220,203,1,0,0,0,220,204,1,0,
        0,0,220,205,1,0,0,0,220,206,1,0,0,0,220,207,1,0,0,0,220,208,1,0,
        0,0,220,209,1,0,0,0,220,210,1,0,0,0,220,211,1,0,0,0,220,212,1,0,
        0,0,220,213,1,0,0,0,220,214,1,0,0,0,220,215,1,0,0,0,220,216,1,0,
        0,0,220,217,1,0,0,0,220,218,1,0,0,0,220,219,1,0,0,0,221,35,1,0,0,
        0,222,223,5,12,0,0,223,224,5,25,0,0,224,227,5,22,0,0,225,226,5,16,
        0,0,226,228,5,30,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,229,1,0,
        0,0,229,230,5,27,0,0,230,37,1,0,0,0,231,232,5,12,0,0,232,233,5,25,
        0,0,233,236,3,18,9,0,234,235,5,16,0,0,235,237,5,30,0,0,236,234,1,
        0,0,0,236,237,1,0,0,0,237,238,1,0,0,0,238,239,5,27,0,0,239,39,1,
        0,0,0,240,241,5,9,0,0,241,242,5,25,0,0,242,245,5,22,0,0,243,244,
        5,16,0,0,244,246,3,72,36,0,245,243,1,0,0,0,245,246,1,0,0,0,246,247,
        1,0,0,0,247,248,5,27,0,0,248,41,1,0,0,0,249,250,5,9,0,0,250,251,
        5,25,0,0,251,254,3,18,9,0,252,253,5,16,0,0,253,255,3,72,36,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,256,1,0,0,0,256,257,5,27,0,0,257,
        43,1,0,0,0,258,259,5,7,0,0,259,260,5,25,0,0,260,263,5,22,0,0,261,
        262,5,16,0,0,262,264,3,72,36,0,263,261,1,0,0,0,263,264,1,0,0,0,264,
        265,1,0,0,0,265,266,5,27,0,0,266,45,1,0,0,0,267,268,5,7,0,0,268,
        269,5,25,0,0,269,272,3,18,9,0,270,271,5,16,0,0,271,273,3,72,36,0,
        272,270,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,275,5,27,0,0,
        275,47,1,0,0,0,276,277,5,8,0,0,277,278,5,25,0,0,278,281,5,22,0,0,
        279,280,5,16,0,0,280,282,3,72,36,0,281,279,1,0,0,0,281,282,1,0,0,
        0,282,283,1,0,0,0,283,284,5,27,0,0,284,49,1,0,0,0,285,286,5,8,0,
        0,286,287,5,25,0,0,287,290,3,18,9,0,288,289,5,16,0,0,289,291,3,72,
        36,0,290,288,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,293,5,27,
        0,0,293,51,1,0,0,0,294,295,5,10,0,0,295,296,5,25,0,0,296,299,5,22,
        0,0,297,298,5,16,0,0,298,300,3,72,36,0,299,297,1,0,0,0,299,300,1,
        0,0,0,300,301,1,0,0,0,301,302,5,27,0,0,302,53,1,0,0,0,303,304,5,
        10,0,0,304,305,5,25,0,0,305,308,3,18,9,0,306,307,5,16,0,0,307,309,
        3,72,36,0,308,306,1,0,0,0,308,309,1,0,0,0,309,310,1,0,0,0,310,311,
        5,27,0,0,311,55,1,0,0,0,312,313,5,11,0,0,313,314,5,25,0,0,314,315,
        5,22,0,0,315,316,5,16,0,0,316,319,5,30,0,0,317,318,5,16,0,0,318,
        320,5,30,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,321,1,0,0,0,321,
        322,5,27,0,0,322,57,1,0,0,0,323,324,5,11,0,0,324,325,5,25,0,0,325,
        326,3,18,9,0,326,327,5,16,0,0,327,330,5,30,0,0,328,329,5,16,0,0,
        329,331,5,30,0,0,330,328,1,0,0,0,330,331,1,0,0,0,331,332,1,0,0,0,
        332,333,5,27,0,0,333,59,1,0,0,0,334,335,5,4,0,0,335,336,5,25,0,0,
        336,337,5,22,0,0,337,338,5,16,0,0,338,339,5,23,0,0,339,340,5,27,
        0,0,340,61,1,0,0,0,341,342,5,6,0,0,342,343,5,25,0,0,343,344,5,22,
        0,0,344,345,5,16,0,0,345,346,5,23,0,0,346,347,5,27,0,0,347,63,1,
        0,0,0,348,349,5,5,0,0,349,350,5,25,0,0,350,351,5,22,0,0,351,352,
        5,16,0,0,352,353,5,23,0,0,353,354,5,27,0,0,354,65,1,0,0,0,355,356,
        5,4,0,0,356,357,5,25,0,0,357,358,3,18,9,0,358,359,5,16,0,0,359,360,
        5,23,0,0,360,361,5,27,0,0,361,67,1,0,0,0,362,363,5,6,0,0,363,364,
        5,25,0,0,364,365,3,18,9,0,365,366,5,16,0,0,366,367,5,23,0,0,367,
        368,5,27,0,0,368,69,1,0,0,0,369,370,5,5,0,0,370,371,5,25,0,0,371,
        372,3,18,9,0,372,373,5,16,0,0,373,374,5,23,0,0,374,375,5,27,0,0,
        375,71,1,0,0,0,376,377,7,0,0,0,377,73,1,0,0,0,378,379,7,1,0,0,379,
        75,1,0,0,0,23,79,91,106,139,146,155,164,180,190,200,220,227,236,
        245,254,263,272,281,290,299,308,319,330
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'left'", "'right'", "'middle'", "'keyPress'", 
                     "'keyType'", "'keyRelease'", "'mouseClick'", "'mouseDoubleClick'", 
                     "'mousePress'", "'mouseRelease'", "'mouseScroll'", 
                     "'wait'", "'text'", "'position'", "'regex'", "','", 
                     "';'", "'label'", "'use'", "'sequence'", "'detector'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "'='", 
                     "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", 
                      "KEY_TYPE", "KEY_RELEASE", "MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", 
                      "MOUSE_PRESS", "MOUSE_RELEASE", "MOUSE_SCROLL", "WAIT", 
                      "TEXT", "POSITION", "REGEX", "COMMA", "DCOMMA", "LABEL", 
                      "USE", "SEQUENCE", "DETECTOR", "ID", "STRING", "ESC", 
                      "ORPAR", "EQ", "CRPAR", "OCPAR", "CCPAR", "INT", "FLOAT", 
                      "WS" ]

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
    RULE_mouseScrollSelector = 29
    RULE_keyPress = 30
    RULE_keyRelease = 31
    RULE_keyType = 32
    RULE_keyPressSelector = 33
    RULE_keyReleaseSelector = 34
    RULE_keyTypeSelector = 35
    RULE_mouseButton = 36
    RULE_number = 37

    ruleNames =  [ "root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
                   "createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
                   "createOperation", "selector", "selectorByLabel", "selectorByText", 
                   "selectorByRegex", "selectorByPosition", "selectorOrder", 
                   "createSequence", "runOperation", "operation", "wait", 
                   "waitSelector", "mousePress", "mousePressSelector", "mouseClick", 
                   "mouseClickSelector", "mouseDoubleClick", "mouseDoubleClickSelector", 
                   "mouseRelease", "mouseReleaseSelector", "mouseScroll", 
                   "mouseScrollSelector", "keyPress", "keyRelease", "keyType", 
                   "keyPressSelector", "keyReleaseSelector", "keyTypeSelector", 
                   "mouseButton", "number" ]

    EOF = Token.EOF
    LEFT=1
    RIGHT=2
    MIDDLE=3
    KEY_PRESS=4
    KEY_TYPE=5
    KEY_RELEASE=6
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
    DCOMMA=17
    LABEL=18
    USE=19
    SEQUENCE=20
    DETECTOR=21
    ID=22
    STRING=23
    ESC=24
    ORPAR=25
    EQ=26
    CRPAR=27
    OCPAR=28
    CCPAR=29
    INT=30
    FLOAT=31
    WS=32

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
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4726768) != 0):
                self.state = 76
                self.stmt()
                self.state = 81
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.createDetector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.useDetector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.createSelectorByLabel()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.createSelectorByText()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.createSelectorByRegex()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.createSelectorByPosition()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.createOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 89
                self.createSequence()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 90
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

        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 93
            self.match(GrammarParser.ID)
            self.state = 94
            self.match(GrammarParser.EQ)
            self.state = 95
            self.match(GrammarParser.DETECTOR)
            self.state = 96
            self.match(GrammarParser.ORPAR)
            self.state = 97
            self.match(GrammarParser.STRING)
            self.state = 98
            self.match(GrammarParser.CRPAR)
            self.state = 99
            self.match(GrammarParser.DCOMMA)
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

        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 101
            self.match(GrammarParser.USE)
            self.state = 102
            self.match(GrammarParser.ID)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 103
                self.match(GrammarParser.ORPAR)
                self.state = 104
                self.match(GrammarParser.FLOAT)
                self.state = 105
                self.match(GrammarParser.CRPAR)


            self.state = 108
            self.match(GrammarParser.DCOMMA)
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


        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 110
            self.match(GrammarParser.ID)
            self.state = 111
            self.match(GrammarParser.EQ)
            self.state = 112
            self.selectorByPosition()
            self.state = 113
            self.match(GrammarParser.DCOMMA)
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


        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 115
            self.match(GrammarParser.ID)
            self.state = 116
            self.match(GrammarParser.EQ)
            self.state = 117
            self.selectorByLabel()
            self.state = 118
            self.match(GrammarParser.DCOMMA)
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


        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 120
            self.match(GrammarParser.ID)
            self.state = 121
            self.match(GrammarParser.EQ)
            self.state = 122
            self.selectorByText()
            self.state = 123
            self.match(GrammarParser.DCOMMA)
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


        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 125
            self.match(GrammarParser.ID)
            self.state = 126
            self.match(GrammarParser.EQ)
            self.state = 127
            self.selectorByRegex()
            self.state = 128
            self.match(GrammarParser.DCOMMA)
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


        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 130
            self.match(GrammarParser.ID)
            self.state = 131
            self.match(GrammarParser.EQ)
            self.state = 132
            self.operation()
            self.state = 133
            self.match(GrammarParser.DCOMMA)
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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.selectorByLabel()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.selectorByText()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.selectorByRegex()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
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
            self.state = 141
            self.match(GrammarParser.LABEL)
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
            self.state = 150
            self.match(GrammarParser.TEXT)
            self.state = 151
            self.match(GrammarParser.ORPAR)
            self.state = 152
            self.match(GrammarParser.STRING)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 153
                self.match(GrammarParser.COMMA)
                self.state = 154
                self.selectorOrder()


            self.state = 157
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
            self.state = 159
            self.match(GrammarParser.REGEX)
            self.state = 160
            self.match(GrammarParser.ORPAR)
            self.state = 161
            self.match(GrammarParser.STRING)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 162
                self.match(GrammarParser.COMMA)
                self.state = 163
                self.selectorOrder()


            self.state = 166
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
            self.state = 168
            self.match(GrammarParser.POSITION)
            self.state = 169
            self.match(GrammarParser.ORPAR)
            self.state = 170
            self.number()
            self.state = 171
            self.match(GrammarParser.COMMA)
            self.state = 172
            self.number()
            self.state = 173
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
            self.state = 175
            self.match(GrammarParser.INT)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 176
                self.match(GrammarParser.COMMA)
                self.state = 177
                self.match(GrammarParser.INT)
                self.state = 182
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

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def SEQUENCE(self):
            return self.getToken(GrammarParser.SEQUENCE, 0)

        def OCPAR(self):
            return self.getToken(GrammarParser.OCPAR, 0)

        def CCPAR(self):
            return self.getToken(GrammarParser.CCPAR, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


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
            self.state = 183
            self.match(GrammarParser.ID)
            self.state = 184
            self.match(GrammarParser.EQ)
            self.state = 185
            self.match(GrammarParser.SEQUENCE)
            self.state = 186
            self.match(GrammarParser.OCPAR)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4726768) != 0):
                self.state = 187
                self.stmt()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
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


        def DCOMMA(self):
            return self.getToken(GrammarParser.DCOMMA, 0)

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
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.operation()
                self.state = 196
                self.match(GrammarParser.DCOMMA)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(GrammarParser.ID)
                self.state = 199
                self.match(GrammarParser.DCOMMA)
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


        def mouseScrollSelector(self):
            return self.getTypedRuleContext(GrammarParser.MouseScrollSelectorContext,0)


        def keyPress(self):
            return self.getTypedRuleContext(GrammarParser.KeyPressContext,0)


        def keyRelease(self):
            return self.getTypedRuleContext(GrammarParser.KeyReleaseContext,0)


        def keyType(self):
            return self.getTypedRuleContext(GrammarParser.KeyTypeContext,0)


        def keyPressSelector(self):
            return self.getTypedRuleContext(GrammarParser.KeyPressSelectorContext,0)


        def keyReleaseSelector(self):
            return self.getTypedRuleContext(GrammarParser.KeyReleaseSelectorContext,0)


        def keyTypeSelector(self):
            return self.getTypedRuleContext(GrammarParser.KeyTypeSelectorContext,0)


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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.wait()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.waitSelector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.mousePress()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.mousePressSelector()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.mouseReleaseSelector()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.mouseClick()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 208
                self.mouseClickSelector()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 209
                self.mouseDoubleClick()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 210
                self.mouseDoubleClickSelector()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 211
                self.mouseRelease()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 212
                self.mouseScroll()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 213
                self.mouseScrollSelector()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 214
                self.keyPress()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 215
                self.keyRelease()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 216
                self.keyType()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 217
                self.keyPressSelector()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 218
                self.keyReleaseSelector()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 219
                self.keyTypeSelector()
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
            self.state = 222
            self.match(GrammarParser.WAIT)
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
                self.match(GrammarParser.INT)


            self.state = 229
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
            self.state = 231
            self.match(GrammarParser.WAIT)
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
                self.match(GrammarParser.INT)


            self.state = 238
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
            self.state = 240
            self.match(GrammarParser.MOUSE_PRESS)
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
            self.state = 249
            self.match(GrammarParser.MOUSE_PRESS)
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
            self.state = 258
            self.match(GrammarParser.MOUSE_CLICK)
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
            self.state = 267
            self.match(GrammarParser.MOUSE_CLICK)
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
            self.state = 276
            self.match(GrammarParser.MOUSE_DOUBLE_CLICK)
            self.state = 277
            self.match(GrammarParser.ORPAR)
            self.state = 278
            self.match(GrammarParser.ID)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 279
                self.match(GrammarParser.COMMA)
                self.state = 280
                self.mouseButton()


            self.state = 283
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
            self.state = 285
            self.match(GrammarParser.MOUSE_DOUBLE_CLICK)
            self.state = 286
            self.match(GrammarParser.ORPAR)
            self.state = 287
            self.selector()
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 288
                self.match(GrammarParser.COMMA)
                self.state = 289
                self.mouseButton()


            self.state = 292
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
            self.state = 294
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 295
            self.match(GrammarParser.ORPAR)
            self.state = 296
            self.match(GrammarParser.ID)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 297
                self.match(GrammarParser.COMMA)
                self.state = 298
                self.mouseButton()


            self.state = 301
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
            self.state = 303
            self.match(GrammarParser.MOUSE_RELEASE)
            self.state = 304
            self.match(GrammarParser.ORPAR)
            self.state = 305
            self.selector()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 306
                self.match(GrammarParser.COMMA)
                self.state = 307
                self.mouseButton()


            self.state = 310
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
            self.state = 312
            self.match(GrammarParser.MOUSE_SCROLL)
            self.state = 313
            self.match(GrammarParser.ORPAR)
            self.state = 314
            self.match(GrammarParser.ID)
            self.state = 315
            self.match(GrammarParser.COMMA)
            self.state = 316
            self.match(GrammarParser.INT)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 317
                self.match(GrammarParser.COMMA)
                self.state = 318
                self.match(GrammarParser.INT)


            self.state = 321
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MouseScrollSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOUSE_SCROLL(self):
            return self.getToken(GrammarParser.MOUSE_SCROLL, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


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
            return GrammarParser.RULE_mouseScrollSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMouseScrollSelector" ):
                listener.enterMouseScrollSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMouseScrollSelector" ):
                listener.exitMouseScrollSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMouseScrollSelector" ):
                return visitor.visitMouseScrollSelector(self)
            else:
                return visitor.visitChildren(self)




    def mouseScrollSelector(self):

        localctx = GrammarParser.MouseScrollSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_mouseScrollSelector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(GrammarParser.MOUSE_SCROLL)
            self.state = 324
            self.match(GrammarParser.ORPAR)
            self.state = 325
            self.selector()
            self.state = 326
            self.match(GrammarParser.COMMA)
            self.state = 327
            self.match(GrammarParser.INT)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 328
                self.match(GrammarParser.COMMA)
                self.state = 329
                self.match(GrammarParser.INT)


            self.state = 332
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

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

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
        self.enterRule(localctx, 60, self.RULE_keyPress)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(GrammarParser.KEY_PRESS)
            self.state = 335
            self.match(GrammarParser.ORPAR)
            self.state = 336
            self.match(GrammarParser.ID)
            self.state = 337
            self.match(GrammarParser.COMMA)
            self.state = 338
            self.match(GrammarParser.STRING)
            self.state = 339
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

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

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
        self.enterRule(localctx, 62, self.RULE_keyRelease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(GrammarParser.KEY_RELEASE)
            self.state = 342
            self.match(GrammarParser.ORPAR)
            self.state = 343
            self.match(GrammarParser.ID)
            self.state = 344
            self.match(GrammarParser.COMMA)
            self.state = 345
            self.match(GrammarParser.STRING)
            self.state = 346
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_TYPE(self):
            return self.getToken(GrammarParser.KEY_TYPE, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_keyType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyType" ):
                listener.enterKeyType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyType" ):
                listener.exitKeyType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyType" ):
                return visitor.visitKeyType(self)
            else:
                return visitor.visitChildren(self)




    def keyType(self):

        localctx = GrammarParser.KeyTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_keyType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(GrammarParser.KEY_TYPE)
            self.state = 349
            self.match(GrammarParser.ORPAR)
            self.state = 350
            self.match(GrammarParser.ID)
            self.state = 351
            self.match(GrammarParser.COMMA)
            self.state = 352
            self.match(GrammarParser.STRING)
            self.state = 353
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyPressSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_PRESS(self):
            return self.getToken(GrammarParser.KEY_PRESS, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_keyPressSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyPressSelector" ):
                listener.enterKeyPressSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyPressSelector" ):
                listener.exitKeyPressSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyPressSelector" ):
                return visitor.visitKeyPressSelector(self)
            else:
                return visitor.visitChildren(self)




    def keyPressSelector(self):

        localctx = GrammarParser.KeyPressSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_keyPressSelector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(GrammarParser.KEY_PRESS)
            self.state = 356
            self.match(GrammarParser.ORPAR)
            self.state = 357
            self.selector()
            self.state = 358
            self.match(GrammarParser.COMMA)
            self.state = 359
            self.match(GrammarParser.STRING)
            self.state = 360
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyReleaseSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_RELEASE(self):
            return self.getToken(GrammarParser.KEY_RELEASE, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_keyReleaseSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyReleaseSelector" ):
                listener.enterKeyReleaseSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyReleaseSelector" ):
                listener.exitKeyReleaseSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyReleaseSelector" ):
                return visitor.visitKeyReleaseSelector(self)
            else:
                return visitor.visitChildren(self)




    def keyReleaseSelector(self):

        localctx = GrammarParser.KeyReleaseSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_keyReleaseSelector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(GrammarParser.KEY_RELEASE)
            self.state = 363
            self.match(GrammarParser.ORPAR)
            self.state = 364
            self.selector()
            self.state = 365
            self.match(GrammarParser.COMMA)
            self.state = 366
            self.match(GrammarParser.STRING)
            self.state = 367
            self.match(GrammarParser.CRPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyTypeSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_TYPE(self):
            return self.getToken(GrammarParser.KEY_TYPE, 0)

        def ORPAR(self):
            return self.getToken(GrammarParser.ORPAR, 0)

        def selector(self):
            return self.getTypedRuleContext(GrammarParser.SelectorContext,0)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def CRPAR(self):
            return self.getToken(GrammarParser.CRPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_keyTypeSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyTypeSelector" ):
                listener.enterKeyTypeSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyTypeSelector" ):
                listener.exitKeyTypeSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyTypeSelector" ):
                return visitor.visitKeyTypeSelector(self)
            else:
                return visitor.visitChildren(self)




    def keyTypeSelector(self):

        localctx = GrammarParser.KeyTypeSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_keyTypeSelector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(GrammarParser.KEY_TYPE)
            self.state = 370
            self.match(GrammarParser.ORPAR)
            self.state = 371
            self.selector()
            self.state = 372
            self.match(GrammarParser.COMMA)
            self.state = 373
            self.match(GrammarParser.STRING)
            self.state = 374
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
        self.enterRule(localctx, 72, self.RULE_mouseButton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
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
        self.enterRule(localctx, 74, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
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





