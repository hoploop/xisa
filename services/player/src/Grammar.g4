grammar Grammar;

root: stmt*;

stmt: createDetector
    | useDetector
    | createSelectorByLabel
    | createSelectorByLabels
    | createSelectorByText
    | createSelectorByTexts
    | createSelectorByRegex
    | createSelectorByRegexes
    | createStep
    | createScenario
    ;

createDetector: ID EQ DETECTOR ORPAR STRING CRPAR;
useDetector: USE ID;
createSelectorByLabel: ID EQ LABEL ORPAR STRING CRPAR;
createSelectorByLabels: ID EQ LABELS ORPAR STRING COMMA INT (COMMA INT)? CRPAR;
createSelectorByText: ID EQ TEXT ORPAR STRING CRPAR;
createSelectorByTexts: ID EQ TEXTS ORPAR STRING COMMA INT (COMMA INT)? CRPAR;
createSelectorByRegex: ID EQ REGEX ORPAR STRING CRPAR;
createSelectorByRegexes: ID EQ REGEXES ORPAR STRING COMMA INT (COMMA INT)? CRPAR;
createStep: ID EQ action;

createScenario: ID EQ SCENARIO OCPAR action  CCPAR;

action  : waitSelector
        | mousePress
        | mouseRelease
        | mouseScroll
        | keyPress
        | keyRelease
        ;
waitSelector: WAIT ORPAR ID (COMMA INT)? CRPAR;
mousePress: MOUSE_PRESS ORPAR ID (COMMA mouseButton)? CRPAR;
mouseRelease: MOUSE_RELEASE ORPAR ID (COMMA mouseButton)? CRPAR;
mouseScroll: MOUSE_SCROLL ORPAR ID COMMA INT (COMMA INT)? CRPAR;
keyPress: KEY_PRESS ORPAR STRING CRPAR;
keyRelease: KEY_RELEASE ORPAR STRING CRPAR;

mouseButton: LEFT|MIDDLE|RIGHT;

LEFT: 'left';
RIGHT: 'right';
MIDDLE: 'middle';
KEY_PRESS: 'keyPress';
KEY_RELEASE: 'keyRelease';
KEY_TYPE: 'keyType';
MOUSE_PRESS: 'mousePress';
MOUSE_RELEASE: 'mouseRelease';
MOUSE_SCROLL: 'mouseScroll';
WAIT: 'wait';
TEXT: 'text';
REGEX: 'regex';
REGEXES: 'regexes';
TEXTS: 'texts';
COMMA: ',';
LABELS: 'labels';
LABEL: 'label';
USE: 'use';
SCENARIO: 'scenario';
DETECTOR: 'detector';
ID: [a-zA-Z]+[a-zA-Z0-9]*; 
STRING: '"' (ESC | ~["\\\r\n]) * '"';  // Match strings with escape sequences
ESC: '\\' [bfnrt"\\]; // Define escape sequences for the string
ORPAR: '(';
EQ: '=';
CRPAR: ')';
OCPAR: '{';
CCPAR: '}';
INT:     [0-9]+;
WS : [ \t\n\r]+ -> skip ;