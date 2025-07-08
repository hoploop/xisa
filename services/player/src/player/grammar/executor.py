# PYTHON IMPORTS
import logging
from typing import List

# LIBRARY IMPORTS
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from ultralytics import YOLO

# LOCAL IMPORTS
from player.grammar.GrammarLexer import GrammarLexer
from player.grammar.GrammarParser import GrammarParser
from player.grammar.analyzer import PlayerAnalyzer
from player.models import Statement

# INITIALIZATION
log = logging.getLogger(__name__)


class ValidationErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))
        
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

        
class Executor():
    
    def loadScript(self,source:str) -> List[Statement]:
        try:
            error_listener = ValidationErrorListener()
            lexer = GrammarLexer(InputStream(source))
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            stream = CommonTokenStream(lexer)
            parser = GrammarParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            tree = parser.root()
            visitor = PlayerAnalyzer()
            stmts:List[Statement] = visitor.visitRoot(tree)
            return stmts
            
        except Exception as e:
            log.warning(str(e))
            return []
        
          