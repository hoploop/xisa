grammar Grammar;

root: stmt*;

stmt: createDetector
    | createSelectorByLabel
    | createSelectorByText
    | createSelectorByRegex
    | createSelectorByPosition
    | createOperation
    | createSequence
    | runOperation
    ;

createDetector: ID EQ DETECTOR ORPAR STRING CRPAR DCOMMA;
useDetector: USE ORPAR ID (COMMA FLOAT)? CRPAR;
createAndUseDetector: USE ORPAR STRING (COMMA FLOAT)? CRPAR;
createSelectorByPosition: ID EQ selectorByPosition DCOMMA;
createSelectorByLabel: ID EQ selectorByLabel DCOMMA;
createSelectorByText: ID EQ selectorByText DCOMMA;
createSelectorByRegex: ID EQ selectorByRegex DCOMMA;
createOperation: ID EQ operation DCOMMA;

selector: selectorByLabel 
        | selectorByText 
        | selectorByRegex
        | selectorByPosition
        | selectorByImage
        ;
selectorByLabel:  LABEL ORPAR STRING (COMMA selectorOrder)? CRPAR ;
selectorByText: TEXT ORPAR STRING  (COMMA selectorOrder)? CRPAR;
selectorByRegex: REGEX ORPAR STRING  (COMMA selectorOrder)? CRPAR;
selectorByPosition: POSITION ORPAR number COMMA number CRPAR; 
selectorByImage: IMAGE ORPAR STRING COMMA FLOAT (COMMA selectorOrder)? (COMMA GRAY)?  CRPAR;
selectorOrder: INT (COMMA INT)*;
createSequence: ID EQ SEQUENCE OCPAR (stmt)* CCPAR DCOMMA;


runOperation
        : operation DCOMMA
        | ID DCOMMA
        ;

operation  
        : wait
        | waitSelector
        | useDetector
        | createAndUseDetector
        | mousePress
        | mousePressSelector
        | mouseReleaseSelector
        | mouseClick
        | mouseClickSelector
        | mouseDoubleClick
        | mouseDoubleClickSelector
        | mouseRelease
        | mouseScroll
        | mouseScrollSelector
        | keyPress
        | keyRelease
        | keyType
        | keyCombo
        | keyComboSelector
        | keyPressSelector
        | keyReleaseSelector
        | keyTypeSelector
        ;

wait: WAIT ORPAR ID (COMMA INT)? CRPAR;
waitSelector: WAIT ORPAR selector (COMMA INT)? CRPAR;
mousePress: MOUSE_PRESS ORPAR ID (COMMA mouseButton)? CRPAR;
mousePressSelector: MOUSE_PRESS ORPAR selector (COMMA mouseButton)? CRPAR;
mouseClick: MOUSE_CLICK ORPAR ID (COMMA mouseButton)? CRPAR;
mouseClickSelector: MOUSE_CLICK ORPAR selector (COMMA mouseButton)? CRPAR;
mouseDoubleClick: MOUSE_DOUBLE_CLICK ORPAR ID (COMMA mouseButton)? CRPAR;
mouseDoubleClickSelector: MOUSE_DOUBLE_CLICK ORPAR selector (COMMA mouseButton)? CRPAR;


mouseRelease: MOUSE_RELEASE ORPAR ID (COMMA mouseButton)? CRPAR;
mouseReleaseSelector: MOUSE_RELEASE ORPAR selector (COMMA mouseButton)? CRPAR;
mouseScroll: MOUSE_SCROLL ORPAR ID COMMA INT (COMMA INT)? CRPAR;
mouseScrollSelector: MOUSE_SCROLL ORPAR selector COMMA INT (COMMA INT)? CRPAR;
keyCombo: KEY_COMBO ORPAR ID STRING (COMMA STRING)+ CRPAR;
keyComboSelector: KEY_COMBO ORPAR selector STRING (COMMA STRING)+ CRPAR;
keyPress: KEY_PRESS ORPAR ID COMMA STRING CRPAR;
keyRelease: KEY_RELEASE ORPAR ID COMMA STRING CRPAR;
keyType: KEY_TYPE ORPAR ID COMMA STRING CRPAR;
keyPressSelector: KEY_PRESS ORPAR selector COMMA STRING CRPAR;
keyReleaseSelector: KEY_RELEASE ORPAR selector COMMA STRING CRPAR;
keyTypeSelector: KEY_TYPE ORPAR selector COMMA STRING CRPAR;

mouseButton: LEFT|MIDDLE|RIGHT;

number: INT | FLOAT;

CONFIDENCE: 'conf'|'confidence';
GRAY: 'gray';
LEFT: 'left';
RIGHT: 'right';
MIDDLE: 'middle';
IMAGE: 'image';
KEY_PRESS: 'keyPress';
KEY_TYPE: 'keyType';
KEY_COMBO: 'keyCombo';
KEY_RELEASE: 'keyRelease';
MOUSE_CLICK: 'mouseClick';
MOUSE_DOUBLE_CLICK: 'mouseDoubleClick';
MOUSE_PRESS: 'mousePress';
MOUSE_RELEASE: 'mouseRelease';
MOUSE_SCROLL: 'mouseScroll';
WAIT: 'wait';
TEXT: 'text';
POSITION: 'position';
REGEX: 'regex';
COMMA: ',';
DCOMMA: ';';
LABEL: 'label';
USE: 'use';
SEQUENCE: 'sequence';
DETECTOR: 'detector';
ID: [a-zA-Z_]+[a-zA-Z0-9_]*; 
STRING: '"' (ESC | ~["\\\r\n]) * '"';  // Match strings with escape sequences
ESC: '\\' [bfnrt"\\]; // Define escape sequences for the string
ORPAR: '(';
EQ: '=';
CRPAR: ')';
OCPAR: '{';
CCPAR: '}';
INT:   [0-9]+;
FLOAT: [0-9]?'.'[0-9]+;
WS : [ \t\n\r]+ -> skip ;
COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;