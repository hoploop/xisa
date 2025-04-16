from typing import List


from player.models import (
    CreateDetectorStatement,
    CreateOperationStatement,
    CreateSelectorStatement,
    CreateSequenceStatement,
    GrammarContext,
    ImageSelector,
    KeyComboOperation,
    KeyPressOperation,
    KeyReleaseOperation,
    KeyTypeOperation,
    LabelSelector,
    MouseClickOperation,
    MouseDoubleClickOperation,
    MouseOperationButton,
    MousePressOperation,
    MouseReleaseOperation,
    MouseScrollOperation,
    Operation,
    PositionSelector,
    RegexSelector,
    RunOperationStatement,
    Selector,
    SelectorReference,
    Statement,
    TextSelector,
    UseDetectorStatement,
    WaitOperation,
)
from player.grammar.GrammarVisitor import GrammarVisitor
from player.grammar.GrammarParser import GrammarParser


class PlayerAnalyzer(GrammarVisitor):
    
    def buildGrammarCtx(self,ctx) -> GrammarContext:
        return GrammarContext(line=ctx.start.line,column=ctx.start.column)

    # Visit a parse tree produced by GrammarParser#root.
    def visitRoot(self, ctx: GrammarParser.RootContext) -> List[Statement]:
        ret = []
        for stmt in ctx.stmt():
            ret.append(self.visitStmt(stmt))
        return ret

    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx: GrammarParser.StmtContext) -> Statement:
        if ctx.createDetector():
            return self.visitCreateDetector(ctx.createDetector())
        elif ctx.useDetector():
            return self.visitUseDetector(ctx.useDetector())
        elif ctx.createOperation():
            return self.visitCreateOperation(ctx.createOperation())
        elif ctx.createSelectorByLabel():
            return self.visitCreateSelectorByLabel(ctx.createSelectorByLabel())
        elif ctx.createSelectorByText():
            return self.visitCreateSelectorByText(ctx.createSelectorByText())
        elif ctx.createSelectorByRegex():
            return self.visitCreateSelectorByRegex(ctx.createSelectorByRegex())
        elif ctx.createSelectorByPosition():
            return self.visitCreateSelectorByPosition(ctx.createSelectorByPosition())
        elif ctx.runOperation():
            return self.visitRunOperation(ctx.runOperation())
        elif ctx.createSequence():
            return self.visitCreateSequence(ctx.createSequence())

    # Visit a parse tree produced by GrammarParser#createDetector.
    def visitCreateDetector(
        self, ctx: GrammarParser.CreateDetectorContext
    ) -> CreateDetectorStatement:
        id = str(ctx.ID().getText())
        source = str(ctx.STRING().getText())[1:-1]
        return CreateDetectorStatement(id=id, value=source,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#useDetector.
    def visitUseDetector(
        self, ctx: GrammarParser.UseDetectorContext
    ) -> UseDetectorStatement:
        id = str(ctx.ID().getText())
        conf = 0.1
        if ctx.FLOAT():
            conf = float(str(ctx.FLOAT().getText()))

        return UseDetectorStatement(id=id, confidence=conf,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#createSelectorByPosition.
    def visitCreateSelectorByPosition(
        self, ctx: GrammarParser.CreateSelectorByPositionContext
    ) -> CreateSelectorStatement:
        id = str(ctx.ID().getText())
        sel = self.visitSelectorByPosition(ctx.selectorByPosition())
        return CreateSelectorStatement(id=id, selector=sel,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#createSelectorByLabel.
    def visitCreateSelectorByLabel(
        self, ctx: GrammarParser.CreateSelectorByLabelContext
    ) -> CreateSelectorStatement:
        id = str(ctx.ID().getText())
        sel = self.visitSelectorByLabel(ctx.selectorByLabel())
        return CreateSelectorStatement(id=id, selector=sel,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#createSelectorByText.
    def visitCreateSelectorByText(
        self, ctx: GrammarParser.CreateSelectorByTextContext
    ) -> CreateSelectorStatement:
        id = str(ctx.ID().getText())
        sel = self.visitSelectorByText(ctx.selectorByText())
        return CreateSelectorStatement(id=id, selector=sel,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#createSelectorByRegex.
    def visitCreateSelectorByRegex(
        self, ctx: GrammarParser.CreateSelectorByRegexContext
    ) -> CreateSelectorStatement:
        id = str(ctx.ID().getText())
        sel = self.visitSelectorByRegex(ctx.selectorByRegex())
        return CreateSelectorStatement(id=id, selector=sel,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#createOperation.
    def visitCreateOperation(
        self, ctx: GrammarParser.CreateOperationContext
    ) -> CreateOperationStatement:
        id = str(ctx.ID().getText())
        op = self.visitOperation(ctx.operation())
        return CreateOperationStatement(id=id, operation=op,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#selector.
    def visitSelector(self, ctx: GrammarParser.SelectorContext) -> Selector:
        if ctx.selectorByLabel():
            return self.visitSelectorByLabel(ctx.selectorByLabel())
        elif ctx.selectorByText():
            return self.visitSelectorByText(ctx.selectorByText())
        elif ctx.selectorByPosition():
            return self.visitSelectorByPosition(ctx.selectorByPosition())
        elif ctx.selectorByRegex():
            return self.visitSelectorByRegex(ctx.selectorByRegex())
        elif ctx.selectorByImage():
            return self.visitSelectorByImage(ctx.selectorByImage())

      # Visit a parse tree produced by GrammarParser#selectorByLabel.
    def visitSelectorByImage(
        self, ctx: GrammarParser.SelectorByImageContext
    ) -> ImageSelector:

        order = []
        if ctx.selectorOrder():
            order = self.visitSelectorOrder(ctx.selectorOrder())
        value = str(ctx.STRING().getText())[1:-1]
        gray=False
        if ctx.GRAY():
            gray=True
        conf = 0.9
        if ctx.FLOAT():
            conf =float(str(ctx.FLOAT().getText()))
        return ImageSelector(value=value, order=order,gray=gray,confidence=conf,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#selectorByLabel.
    def visitSelectorByLabel(
        self, ctx: GrammarParser.SelectorByLabelContext
    ) -> LabelSelector:

        order = []
        if ctx.selectorOrder():
            order = self.visitSelectorOrder(ctx.selectorOrder())
        value = str(ctx.STRING().getText())[1:-1]
        return LabelSelector(value=value, order=order,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#selectorByText.
    def visitSelectorByText(
        self, ctx: GrammarParser.SelectorByTextContext
    ) -> TextSelector:
        order = []
        if ctx.selectorOrder():
            order = self.visitSelectorOrder(ctx.selectorOrder())
        value = str(ctx.STRING().getText())[1:-1]
        return TextSelector(value=value, order=order,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#selectorByRegex.
    def visitSelectorByRegex(
        self, ctx: GrammarParser.SelectorByRegexContext
    ) -> RegexSelector:
        order = []
        if ctx.selectorOrder():
            order = self.visitSelectorOrder(ctx.selectorOrder())
        value = str(ctx.STRING().getText())[1:-1]
        return RegexSelector(value=value, order=order,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#selectorByPosition.
    def visitSelectorByPosition(
        self, ctx: GrammarParser.SelectorByPositionContext
    ) -> PositionSelector:
        x = float(str(ctx.number(0).getText()))
        y = float(str(ctx.number(1).getText()))
        return PositionSelector(x=x, y=y,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#selectorOrder.
    def visitSelectorOrder(self, ctx: GrammarParser.SelectorOrderContext) -> List[int]:
        ret = []
        for el in ctx.INT():
            ret.append(int(str(el.getText())))
        return ret

    # Visit a parse tree produced by GrammarParser#createSequence.
    def visitCreateSequence(
        self, ctx: GrammarParser.CreateSequenceContext
    ) -> CreateSequenceStatement:
        id = str(ctx.ID().getText())
        stmts = []
        for stmt in ctx.stmt():
            stmts.append(self.visitStmt(stmt))
        return CreateSequenceStatement(id=id, statements=stmts,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#runOperation.
    def visitRunOperation(
        self, ctx: GrammarParser.RunOperationContext
    ) -> RunOperationStatement:
        op = self.visitOperation(ctx.operation())
        print(op)
        return RunOperationStatement(operation=op,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#operation.
    def visitOperation(self, ctx: GrammarParser.OperationContext) -> Operation:
        if ctx.keyPress():
            return self.visitKeyPress(ctx.keyPress())
        elif ctx.keyRelease():
            return self.visitKeyRelease(ctx.keyRelease())
        elif ctx.keyType():
            return self.visitKeyType(ctx.keyType())
        elif ctx.keyPressSelector():
            return self.visitKeyPressSelector(ctx.keyPressSelector())
        elif ctx.keyCombo():
            return self.visitKeyCombo(ctx.keyCombo())
        elif ctx.keyComboSelector():
            return self.visitKeyComboSelector(ctx.keyComboSelector())
        elif ctx.keyReleaseSelector():
            return self.visitKeyReleaseSelector(ctx.keyReleaseSelector())
        elif ctx.keyTypeSelector():
            return self.visitKeyTypeSelector(ctx.keyTypeSelector())
        elif ctx.mouseClick():
            return self.visitMouseClick(ctx.mouseClick())
        elif ctx.mouseClickSelector():
            return self.visitMouseClickSelector(ctx.mouseClickSelector())
        elif ctx.mouseDoubleClick():
            return self.visitMouseDoubleClick(ctx.mouseDoubleClick())
        elif ctx.mouseDoubleClickSelector():
            return self.visitMouseDoubleClickSelector(ctx.mouseDoubleClickSelector())
        elif ctx.mousePress():
            return self.visitMousePress(ctx.mousePress())
        elif ctx.mousePressSelector():
            return self.visitMousePressSelector(ctx.mousePressSelector())
        elif ctx.mouseReleaseSelector():
            return self.visitMousePressSelector(ctx.mouseReleaseSelector())
        elif ctx.mouseRelease():
            return self.visitMouseRelease(ctx.mouseRelease())
        elif ctx.mouseReleaseSelector():
            return self.visitMouseReleaseSelector(ctx.mouseReleaseSelector())
        elif ctx.mouseScroll():
            return self.visitMouseScroll(ctx.mouseScroll())
        elif ctx.mouseScrollSelector():
            return self.visitMouseScrollSelector(ctx.mouseScrollSelector())

    # Visit a parse tree produced by GrammarParser#wait.
    def visitWait(self, ctx: GrammarParser.WaitContext) -> WaitOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        t = 1000
        if ctx.INT():
            t = int(str(ctx.INT().getText()))
        return WaitOperation(selector=sel, value=t,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#keyType.
    def visitKeyType(self, ctx: GrammarParser.KeyTypeContext) -> KeyTypeOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        value = str(ctx.STRING().getText())[1:-1]
        return KeyTypeOperation(value=value,ctx=self.buildGrammarCtx(ctx),selector=sel)

    # Visit a parse tree produced by GrammarParser#waitSelector.
    def visitWaitSelector(
        self, ctx: GrammarParser.WaitSelectorContext
    ) -> WaitOperation:
        sel = self.visitSelector(ctx.selector())
        t = 1000
        if ctx.INT():
            t = int(str(ctx.INT().getText()))
        return WaitOperation(selector=sel, value=t,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mousePress.
    def visitMousePress(
        self, ctx: GrammarParser.MousePressContext
    ) -> MousePressOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())
        
        return MousePressOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mousePressSelector.
    def visitMousePressSelector(
        self, ctx: GrammarParser.MousePressSelectorContext
    ) -> MousePressOperation:
        sel = self.visitSelector(ctx.selector())
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())
        return MousePressOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseClick.
    def visitMouseClick(
        self, ctx: GrammarParser.MouseClickContext
    ) -> MouseClickOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())

        return MouseClickOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseClickSelector.
    def visitMouseClickSelector(
        self, ctx: GrammarParser.MouseClickSelectorContext
    ) -> MouseClickOperation:
        sel = self.visitSelector(ctx.selector())
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())
        return MouseClickOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseDoubleClick.
    def visitMouseDoubleClick(
        self, ctx: GrammarParser.MouseDoubleClickContext
    ) -> MouseDoubleClickOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())

        return MouseDoubleClickOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseDoubleClickSelector.
    def visitMouseDoubleClickSelector(
        self, ctx: GrammarParser.MouseDoubleClickSelectorContext
    ) -> MouseDoubleClickOperation:
        sel = self.visitSelector(ctx.selector())
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())
        return MouseDoubleClickOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseRelease.
    def visitMouseRelease(
        self, ctx: GrammarParser.MouseReleaseContext
    ) -> MouseReleaseOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())

        return MouseReleaseOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseReleaseSelector.
    def visitMouseReleaseSelector(
        self, ctx: GrammarParser.MouseReleaseSelectorContext
    ) -> MouseReleaseOperation:
        sel = self.visitSelector(ctx.selector())
        but = MouseOperationButton.LEFT
        if ctx.mouseButton():
            but = self.visitMouseButton(ctx.mouseButton())
        return MouseReleaseOperation(selector=sel, button=but,ctx=self.buildGrammarCtx(ctx))

    # Visit a parse tree produced by GrammarParser#mouseScroll.
    def visitMouseScroll(
        self, ctx: GrammarParser.MouseScrollContext
    ) -> MouseScrollOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        dx = int(str(ctx.INT(0).getText()))
        dy = int(str(ctx.INT(1).getText()))
        return MouseScrollOperation(selector=sel,dx=dx, dy=dy,ctx=self.buildGrammarCtx(ctx))


     # Visit a parse tree produced by GrammarParser#mouseScroll.
    def visitMouseScrollSelector(
        self, ctx: GrammarParser.MouseScrollSelectorContext
    ) -> MouseScrollOperation:
        sel = self.visitSelector(ctx.selector())
        dx = int(str(ctx.INT(0).getText()))
        dy = int(str(ctx.INT(1).getText()))
        return MouseScrollOperation(selector=sel,dx=dx, dy=dy,ctx=self.buildGrammarCtx(ctx))


    # Visit a parse tree produced by GrammarParser#keyPress.
    def visitKeyPress(self, ctx: GrammarParser.KeyPressContext) -> KeyPressOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        value = str(ctx.STRING().getText())[1:-1]
        return KeyPressOperation(value=value,ctx=self.buildGrammarCtx(ctx),selector=sel)

    # Visit a parse tree produced by GrammarParser#keyRelease.
    def visitKeyRelease(
        self, ctx: GrammarParser.KeyReleaseContext
    ) -> KeyReleaseOperation:
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        value = str(ctx.STRING().getText())[1:-1]
        return KeyReleaseOperation(value=value,ctx=self.buildGrammarCtx(ctx),selector=sel)
    
     # Visit a parse tree produced by GrammarParser#keyPressSelector.
    def visitKeyCombo(self, ctx:GrammarParser.KeyComboContext):
        sel = self.visitSelector(ctx.selector)
        values = []
        for strCtx in ctx.STRING():
            values.append(str(strCtx.getText())[1:-1])
        return KeyComboOperation(values=values,ctx=self.buildGrammarCtx(ctx),selector=sel)


    # Visit a parse tree produced by GrammarParser#keyReleaseSelector.
    def visitKeyComboSelector(self, ctx:GrammarParser.KeyComboSelectorContext):
        id = str(ctx.ID().getText())
        sel = SelectorReference(reference=id)
        values = []
        for strCtx in ctx.STRING():
            values.append(str(strCtx.getText())[1:-1])
        return KeyComboOperation(values=values,ctx=self.buildGrammarCtx(ctx),selector=sel)


    
    # Visit a parse tree produced by GrammarParser#keyPressSelector.
    def visitKeyPressSelector(self, ctx:GrammarParser.KeyPressSelectorContext):
        sel = self.visitSelector(ctx.selector)
        value = str(ctx.STRING().getText())[1:-1]
        return KeyPressOperation(value=value,ctx=self.buildGrammarCtx(ctx),selector=sel)


    # Visit a parse tree produced by GrammarParser#keyReleaseSelector.
    def visitKeyReleaseSelector(self, ctx:GrammarParser.KeyReleaseSelectorContext):
        sel = self.visitSelector(ctx.selector)
        value = str(ctx.STRING().getText())[1:-1]
        return KeyReleaseOperation(value=value,ctx=self.buildGrammarCtx(ctx),selector=sel)


    # Visit a parse tree produced by GrammarParser#keyTypeSelector.
    def visitKeyTypeSelector(self, ctx:GrammarParser.KeyTypeSelectorContext):
        sel = self.visitSelector(ctx.selector())
        value = str(ctx.STRING().getText())[1:-1]
        return KeyTypeOperation(value=value,ctx=self.buildGrammarCtx(ctx),selector=sel)



    # Visit a parse tree produced by GrammarParser#mouseButton.
    def visitMouseButton(
        self, ctx: GrammarParser.MouseButtonContext
    ) -> MouseOperationButton:
        if ctx.LEFT():
            return MouseOperationButton.LEFT
        elif ctx.MIDDLE():
            MouseOperationButton.MIDDLE
        elif ctx.RIGHT():
            MouseOperationButton.RIGHT

    # Visit a parse tree produced by GrammarParser#number.
    def visitNumber(self, ctx: GrammarParser.NumberContext) -> float:
        if ctx.INT():
            return float(str(ctx.INT().getText()))
        elif ctx.FLOAT():
            return float(str(ctx.FLOAT().getText()))
