from player.grammar.GrammarVisitor import GrammarVisitor
from player.grammar.GrammarParser import GrammarParser


class PlayerAnalyser(GrammarVisitor):
        
            
    # Visit a parse tree produced by GrammarParser#root.
    def visitRoot(self, ctx:GrammarParser.RootContext):
        for stmt in ctx.stmt():
            self.visitStmt(stmt)


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx:GrammarParser.StmtContext):
        if ctx.createDetector():
            self.visitCreateDetector(ctx.createDetector())
        elif ctx.useDetector():
            self.visitUseDetector(ctx.useDetector())
            


    # Visit a parse tree produced by GrammarParser#createDetector.
    def visitCreateDetector(self, ctx:GrammarParser.CreateDetectorContext):
        id = str(ctx.ID())
        source = str(ctx.STRING())[1:-1]


    # Visit a parse tree produced by GrammarParser#useDetector.
    def visitUseDetector(self, ctx:GrammarParser.UseDetectorContext):
        return self.visitChildren(ctx)

        
        