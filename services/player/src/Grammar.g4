grammar Grammar;

root: stmt*;

stmt: createDetector
    | useDetector
    | createSelectorByLabel
    | createSelectorByText
    | createSelectorByRegex
    | createSelectorByPosition
    | createOperation
    | createSequence
    | runOperation
    ;

createDetector: ID EQ DETECTOR ORPAR STRING CRPAR;
useDetector: USE ID (ORPAR FLOAT CRPAR)?;
createSelectorByPosition: ID EQ selectorByPosition;
createSelectorByLabel: ID EQ selectorByLabel;
createSelectorByText: ID EQ selectorByText ;
createSelectorByRegex: ID EQ selectorByRegex;
createOperation: ID EQ operation;

selector: selectorByLabel 
        | selectorByText 
        | selectorByRegex
        | selectorByPosition
        ;
selectorByLabel:  LABEL ORPAR STRING (COMMA selectorOrder)? CRPAR ;
selectorByText: TEXT ORPAR STRING  (COMMA selectorOrder)? CRPAR;
selectorByRegex: REGEX ORPAR STRING  (COMMA selectorOrder)? CRPAR;
selectorByPosition: POSITION ORPAR number COMMA number CRPAR; 
selectorOrder: INT (COMMA INT)*;
createSequence: ID EQ SEQUENCE OCPAR (operation|ID)* CCPAR;


runOperation
        : operation
        | ID
        ;

operation  
        : wait
        | waitSelector
        | mousePress
        | mousePressSelector
        | mouseReleaseSelector
        | mouseClick
        | mouseClickSelector
        | mouseDoubleClick
        | mouseDoubleClickSelector
        | mouseRelease
        | mouseScroll
        | keyPress
        | keyRelease
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
keyPress: KEY_PRESS ORPAR STRING CRPAR;
keyRelease: KEY_RELEASE ORPAR STRING CRPAR;

mouseButton: LEFT|MIDDLE|RIGHT;

number: INT | FLOAT;

LEFT: 'left';
RIGHT: 'right';
MIDDLE: 'middle';
KEY_PRESS: 'keyPress';
KEY_RELEASE: 'keyRelease';
KEY_TYPE: 'keyType';
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
LABEL: 'label';
USE: 'use';
SEQUENCE: 'sequence';
DETECTOR: 'detector';
ID: [a-zA-Z]+[a-zA-Z0-9]*; 
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