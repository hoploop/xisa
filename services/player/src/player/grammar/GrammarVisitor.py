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


    # Visit a parse tree produced by GrammarParser#createSelectorByPosition.
    def visitCreateSelectorByPosition(self, ctx:GrammarParser.CreateSelectorByPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByLabel.
    def visitCreateSelectorByLabel(self, ctx:GrammarParser.CreateSelectorByLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByText.
    def visitCreateSelectorByText(self, ctx:GrammarParser.CreateSelectorByTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSelectorByRegex.
    def visitCreateSelectorByRegex(self, ctx:GrammarParser.CreateSelectorByRegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createOperation.
    def visitCreateOperation(self, ctx:GrammarParser.CreateOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#selector.
    def visitSelector(self, ctx:GrammarParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#selectorByLabel.
    def visitSelectorByLabel(self, ctx:GrammarParser.SelectorByLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#selectorByText.
    def visitSelectorByText(self, ctx:GrammarParser.SelectorByTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#selectorByRegex.
    def visitSelectorByRegex(self, ctx:GrammarParser.SelectorByRegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#selectorByPosition.
    def visitSelectorByPosition(self, ctx:GrammarParser.SelectorByPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#selectorOrder.
    def visitSelectorOrder(self, ctx:GrammarParser.SelectorOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#createSequence.
    def visitCreateSequence(self, ctx:GrammarParser.CreateSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#runOperation.
    def visitRunOperation(self, ctx:GrammarParser.RunOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#operation.
    def visitOperation(self, ctx:GrammarParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#wait.
    def visitWait(self, ctx:GrammarParser.WaitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#waitSelector.
    def visitWaitSelector(self, ctx:GrammarParser.WaitSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mousePress.
    def visitMousePress(self, ctx:GrammarParser.MousePressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mousePressSelector.
    def visitMousePressSelector(self, ctx:GrammarParser.MousePressSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseClick.
    def visitMouseClick(self, ctx:GrammarParser.MouseClickContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseClickSelector.
    def visitMouseClickSelector(self, ctx:GrammarParser.MouseClickSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseDoubleClick.
    def visitMouseDoubleClick(self, ctx:GrammarParser.MouseDoubleClickContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseDoubleClickSelector.
    def visitMouseDoubleClickSelector(self, ctx:GrammarParser.MouseDoubleClickSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseRelease.
    def visitMouseRelease(self, ctx:GrammarParser.MouseReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseReleaseSelector.
    def visitMouseReleaseSelector(self, ctx:GrammarParser.MouseReleaseSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseScroll.
    def visitMouseScroll(self, ctx:GrammarParser.MouseScrollContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseScrollSelector.
    def visitMouseScrollSelector(self, ctx:GrammarParser.MouseScrollSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyPress.
    def visitKeyPress(self, ctx:GrammarParser.KeyPressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyRelease.
    def visitKeyRelease(self, ctx:GrammarParser.KeyReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyType.
    def visitKeyType(self, ctx:GrammarParser.KeyTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyPressSelector.
    def visitKeyPressSelector(self, ctx:GrammarParser.KeyPressSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyReleaseSelector.
    def visitKeyReleaseSelector(self, ctx:GrammarParser.KeyReleaseSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#keyTypeSelector.
    def visitKeyTypeSelector(self, ctx:GrammarParser.KeyTypeSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mouseButton.
    def visitMouseButton(self, ctx:GrammarParser.MouseButtonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#number.
    def visitNumber(self, ctx:GrammarParser.NumberContext):
        return self.visitChildren(ctx)



del GrammarParser