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


    # Enter a parse tree produced by GrammarParser#createSelectorByPosition.
    def enterCreateSelectorByPosition(self, ctx:GrammarParser.CreateSelectorByPositionContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByPosition.
    def exitCreateSelectorByPosition(self, ctx:GrammarParser.CreateSelectorByPositionContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByLabel.
    def enterCreateSelectorByLabel(self, ctx:GrammarParser.CreateSelectorByLabelContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByLabel.
    def exitCreateSelectorByLabel(self, ctx:GrammarParser.CreateSelectorByLabelContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByText.
    def enterCreateSelectorByText(self, ctx:GrammarParser.CreateSelectorByTextContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByText.
    def exitCreateSelectorByText(self, ctx:GrammarParser.CreateSelectorByTextContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSelectorByRegex.
    def enterCreateSelectorByRegex(self, ctx:GrammarParser.CreateSelectorByRegexContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSelectorByRegex.
    def exitCreateSelectorByRegex(self, ctx:GrammarParser.CreateSelectorByRegexContext):
        pass


    # Enter a parse tree produced by GrammarParser#createOperation.
    def enterCreateOperation(self, ctx:GrammarParser.CreateOperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#createOperation.
    def exitCreateOperation(self, ctx:GrammarParser.CreateOperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#selector.
    def enterSelector(self, ctx:GrammarParser.SelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#selector.
    def exitSelector(self, ctx:GrammarParser.SelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#selectorByLabel.
    def enterSelectorByLabel(self, ctx:GrammarParser.SelectorByLabelContext):
        pass

    # Exit a parse tree produced by GrammarParser#selectorByLabel.
    def exitSelectorByLabel(self, ctx:GrammarParser.SelectorByLabelContext):
        pass


    # Enter a parse tree produced by GrammarParser#selectorByText.
    def enterSelectorByText(self, ctx:GrammarParser.SelectorByTextContext):
        pass

    # Exit a parse tree produced by GrammarParser#selectorByText.
    def exitSelectorByText(self, ctx:GrammarParser.SelectorByTextContext):
        pass


    # Enter a parse tree produced by GrammarParser#selectorByRegex.
    def enterSelectorByRegex(self, ctx:GrammarParser.SelectorByRegexContext):
        pass

    # Exit a parse tree produced by GrammarParser#selectorByRegex.
    def exitSelectorByRegex(self, ctx:GrammarParser.SelectorByRegexContext):
        pass


    # Enter a parse tree produced by GrammarParser#selectorByPosition.
    def enterSelectorByPosition(self, ctx:GrammarParser.SelectorByPositionContext):
        pass

    # Exit a parse tree produced by GrammarParser#selectorByPosition.
    def exitSelectorByPosition(self, ctx:GrammarParser.SelectorByPositionContext):
        pass


    # Enter a parse tree produced by GrammarParser#selectorOrder.
    def enterSelectorOrder(self, ctx:GrammarParser.SelectorOrderContext):
        pass

    # Exit a parse tree produced by GrammarParser#selectorOrder.
    def exitSelectorOrder(self, ctx:GrammarParser.SelectorOrderContext):
        pass


    # Enter a parse tree produced by GrammarParser#createSequence.
    def enterCreateSequence(self, ctx:GrammarParser.CreateSequenceContext):
        pass

    # Exit a parse tree produced by GrammarParser#createSequence.
    def exitCreateSequence(self, ctx:GrammarParser.CreateSequenceContext):
        pass


    # Enter a parse tree produced by GrammarParser#runOperation.
    def enterRunOperation(self, ctx:GrammarParser.RunOperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#runOperation.
    def exitRunOperation(self, ctx:GrammarParser.RunOperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#operation.
    def enterOperation(self, ctx:GrammarParser.OperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#operation.
    def exitOperation(self, ctx:GrammarParser.OperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#wait.
    def enterWait(self, ctx:GrammarParser.WaitContext):
        pass

    # Exit a parse tree produced by GrammarParser#wait.
    def exitWait(self, ctx:GrammarParser.WaitContext):
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


    # Enter a parse tree produced by GrammarParser#mousePressSelector.
    def enterMousePressSelector(self, ctx:GrammarParser.MousePressSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#mousePressSelector.
    def exitMousePressSelector(self, ctx:GrammarParser.MousePressSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseClick.
    def enterMouseClick(self, ctx:GrammarParser.MouseClickContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseClick.
    def exitMouseClick(self, ctx:GrammarParser.MouseClickContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseClickSelector.
    def enterMouseClickSelector(self, ctx:GrammarParser.MouseClickSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseClickSelector.
    def exitMouseClickSelector(self, ctx:GrammarParser.MouseClickSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseDoubleClick.
    def enterMouseDoubleClick(self, ctx:GrammarParser.MouseDoubleClickContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseDoubleClick.
    def exitMouseDoubleClick(self, ctx:GrammarParser.MouseDoubleClickContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseDoubleClickSelector.
    def enterMouseDoubleClickSelector(self, ctx:GrammarParser.MouseDoubleClickSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseDoubleClickSelector.
    def exitMouseDoubleClickSelector(self, ctx:GrammarParser.MouseDoubleClickSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseRelease.
    def enterMouseRelease(self, ctx:GrammarParser.MouseReleaseContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseRelease.
    def exitMouseRelease(self, ctx:GrammarParser.MouseReleaseContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseReleaseSelector.
    def enterMouseReleaseSelector(self, ctx:GrammarParser.MouseReleaseSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseReleaseSelector.
    def exitMouseReleaseSelector(self, ctx:GrammarParser.MouseReleaseSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseScroll.
    def enterMouseScroll(self, ctx:GrammarParser.MouseScrollContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseScroll.
    def exitMouseScroll(self, ctx:GrammarParser.MouseScrollContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseScrollSelector.
    def enterMouseScrollSelector(self, ctx:GrammarParser.MouseScrollSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseScrollSelector.
    def exitMouseScrollSelector(self, ctx:GrammarParser.MouseScrollSelectorContext):
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


    # Enter a parse tree produced by GrammarParser#keyType.
    def enterKeyType(self, ctx:GrammarParser.KeyTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyType.
    def exitKeyType(self, ctx:GrammarParser.KeyTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#keyPressSelector.
    def enterKeyPressSelector(self, ctx:GrammarParser.KeyPressSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyPressSelector.
    def exitKeyPressSelector(self, ctx:GrammarParser.KeyPressSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#keyReleaseSelector.
    def enterKeyReleaseSelector(self, ctx:GrammarParser.KeyReleaseSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyReleaseSelector.
    def exitKeyReleaseSelector(self, ctx:GrammarParser.KeyReleaseSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#keyTypeSelector.
    def enterKeyTypeSelector(self, ctx:GrammarParser.KeyTypeSelectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#keyTypeSelector.
    def exitKeyTypeSelector(self, ctx:GrammarParser.KeyTypeSelectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#mouseButton.
    def enterMouseButton(self, ctx:GrammarParser.MouseButtonContext):
        pass

    # Exit a parse tree produced by GrammarParser#mouseButton.
    def exitMouseButton(self, ctx:GrammarParser.MouseButtonContext):
        pass


    # Enter a parse tree produced by GrammarParser#number.
    def enterNumber(self, ctx:GrammarParser.NumberContext):
        pass

    # Exit a parse tree produced by GrammarParser#number.
    def exitNumber(self, ctx:GrammarParser.NumberContext):
        pass



del GrammarParser