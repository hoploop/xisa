# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#root.
    def enterRoot(self, ctx:GrammarParser.RootContext):
        pass

    # Exit a parse tree produced by GrammarParser#root.
    def exitRoot(self, ctx:GrammarParser.RootContext):
        pass


    # Enter a parse tree produced by GrammarParser#stmt.
    def enterStmt(self, ctx:GrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#stmt.
    def exitStmt(self, ctx:GrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#createDetector.
    def enterCreateDetector(self, ctx:GrammarParser.CreateDetectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#createDetector.
    def exitCreateDetector(self, ctx:GrammarParser.CreateDetectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#useDetector.
    def enterUseDetector(self, ctx:GrammarParser.UseDetectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#useDetector.
    def exitUseDetector(self, ctx:GrammarParser.UseDetectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByLabel.
    def enterCreateSelectorByLabel(self, ctx:GrammarParser.CreateSelectorByLabelContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByLabel.
    def exitCreateSelectorByLabel(self, ctx:GrammarParser.CreateSelectorByLabelContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByLabels.
    def enterCreateSelectorByLabels(self, ctx:GrammarParser.CreateSelectorByLabelsContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByLabels.
    def exitCreateSelectorByLabels(self, ctx:GrammarParser.CreateSelectorByLabelsContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByText.
    def enterCreateSelectorByText(self, ctx:GrammarParser.CreateSelectorByTextContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByText.
    def exitCreateSelectorByText(self, ctx:GrammarParser.CreateSelectorByTextContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByTexts.
    def enterCreateSelectorByTexts(self, ctx:GrammarParser.CreateSelectorByTextsContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByTexts.
    def exitCreateSelectorByTexts(self, ctx:GrammarParser.CreateSelectorByTextsContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByRegex.
    def enterCreateSelectorByRegex(self, ctx:GrammarParser.CreateSelectorByRegexContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByRegex.
    def exitCreateSelectorByRegex(self, ctx:GrammarParser.CreateSelectorByRegexContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByRegexes.
    def enterCreateSelectorByRegexes(self, ctx:GrammarParser.CreateSelectorByRegexesContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByRegexes.
    def exitCreateSelectorByRegexes(self, ctx:GrammarParser.CreateSelectorByRegexesContext):
        pass


    # Enter a parse tree produced by GrammarParser#createStep.
    def enterCreateStep(self, ctx:GrammarParser.CreateStepContext):
        pass

    # Exit a parse tree produced by GrammarParser#createStep.
    def exitCreateStep(self, ctx:GrammarParser.CreateStepContext):
        pass


    # Enter a parse tree produced by GrammarParser#action.
    def enterAction(self, ctx:GrammarParser.ActionContext):
        pass

    # Exit a parse tree produced by GrammarParser#action.
    def exitAction(self, ctx:GrammarParser.ActionContext):
        pass


    # Enter a parse tree produced by GrammarParser#waitSelector.
    def enterWaitSelector(self, ctx:GrammarParser.WaitSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#waitSelector.
    def exitWaitSelector(self, ctx:GrammarParser.WaitSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#mousePress.
    def enterMousePress(self, ctx:GrammarParser.MousePressContext):
        pass

    # Exit a parse tree produced by GrammarParser#mousePress.
    def exitMousePress(self, ctx:GrammarParser.MousePressContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseRelease.
    def enterMouseRelease(self, ctx:GrammarParser.MouseReleaseContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseRelease.
    def exitMouseRelease(self, ctx:GrammarParser.MouseReleaseContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseScroll.
    def enterMouseScroll(self, ctx:GrammarParser.MouseScrollContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseScroll.
    def exitMouseScroll(self, ctx:GrammarParser.MouseScrollContext):
        pass


    # Enter a parse tree produced by GrammarParser#keyPress.
    def enterKeyPress(self, ctx:GrammarParser.KeyPressContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyPress.
    def exitKeyPress(self, ctx:GrammarParser.KeyPressContext):
        pass


    # Enter a parse tree produced by GrammarParser#keyRelease.
    def enterKeyRelease(self, ctx:GrammarParser.KeyReleaseContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyRelease.
    def exitKeyRelease(self, ctx:GrammarParser.KeyReleaseContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseButton.
    def enterMouseButton(self, ctx:GrammarParser.MouseButtonContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseButton.
    def exitMouseButton(self, ctx:GrammarParser.MouseButtonContext):
        pass



del GrammarParser