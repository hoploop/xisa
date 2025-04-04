# LIBRARY IMPORTS
from antlr4 import *

# LOCAL IMPORTS
from player.grammar.GrammarLexer import GrammarLexer
from player.grammar.GrammarParser import GrammarParser
from player.grammar.PlayerAnalyser import PlayerAnalyser

class GrammarInterpreter:
    
    async def analyseString(source:str):
        # Read the input expression
         # Read the input expression
        input_stream = InputStream(input("Enter expression: "))

        # Create a lexer and a parser
        lexer = GrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = GrammarParser(token_stream)

        # Parse the expression (it expects an 'expr' rule)
        tree = parser.expr()

        # Visit the parse tree using the ArithmeticEvalVisitor
        visitor = PlayerAnalyser()
        result = visitor.visit(tree)