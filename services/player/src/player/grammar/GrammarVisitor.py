# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#root.
    def visitRoot(self, ctx:GrammarParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx:GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createDetector.
    def visitCreateDetector(self, ctx:GrammarParser.CreateDetectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#useDetector.
    def visitUseDetector(self, ctx:GrammarParser.UseDetectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByLabel.
    def visitCreateSelectorByLabel(self, ctx:GrammarParser.CreateSelectorByLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByLabels.
    def visitCreateSelectorByLabels(self, ctx:GrammarParser.CreateSelectorByLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByText.
    def visitCreateSelectorByText(self, ctx:GrammarParser.CreateSelectorByTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByTexts.
    def visitCreateSelectorByTexts(self, ctx:GrammarParser.CreateSelectorByTextsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByRegex.
    def visitCreateSelectorByRegex(self, ctx:GrammarParser.CreateSelectorByRegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByRegexes.
    def visitCreateSelectorByRegexes(self, ctx:GrammarParser.CreateSelectorByRegexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createStep.
    def visitCreateStep(self, ctx:GrammarParser.CreateStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#action.
    def visitAction(self, ctx:GrammarParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#waitSelector.
    def visitWaitSelector(self, ctx:GrammarParser.WaitSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mousePress.
    def visitMousePress(self, ctx:GrammarParser.MousePressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseRelease.
    def visitMouseRelease(self, ctx:GrammarParser.MouseReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseScroll.
    def visitMouseScroll(self, ctx:GrammarParser.MouseScrollContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyPress.
    def visitKeyPress(self, ctx:GrammarParser.KeyPressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyRelease.
    def visitKeyRelease(self, ctx:GrammarParser.KeyReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseButton.
    def visitMouseButton(self, ctx:GrammarParser.MouseButtonContext):
        return self.visitChildren(ctx)



del GrammarParser