// Generated from Grammar.g4 by ANTLR 4.13.2

import {ParseTreeListener} from "antlr4";


import { RootContext } from "./GrammarParser.js";
import { StmtContext } from "./GrammarParser.js";
import { CreateDetectorContext } from "./GrammarParser.js";
import { UseDetectorContext } from "./GrammarParser.js";
import { CreateSelectorByPositionContext } from "./GrammarParser.js";
import { CreateSelectorByLabelContext } from "./GrammarParser.js";
import { CreateSelectorByTextContext } from "./GrammarParser.js";
import { CreateSelectorByRegexContext } from "./GrammarParser.js";
import { CreateOperationContext } from "./GrammarParser.js";
import { SelectorContext } from "./GrammarParser.js";
import { SelectorByLabelContext } from "./GrammarParser.js";
import { SelectorByTextContext } from "./GrammarParser.js";
import { SelectorByRegexContext } from "./GrammarParser.js";
import { SelectorByPositionContext } from "./GrammarParser.js";
import { SelectorOrderContext } from "./GrammarParser.js";
import { CreateSequenceContext } from "./GrammarParser.js";
import { RunOperationContext } from "./GrammarParser.js";
import { OperationContext } from "./GrammarParser.js";
import { WaitContext } from "./GrammarParser.js";
import { WaitSelectorContext } from "./GrammarParser.js";
import { MousePressContext } from "./GrammarParser.js";
import { MousePressSelectorContext } from "./GrammarParser.js";
import { MouseClickContext } from "./GrammarParser.js";
import { MouseClickSelectorContext } from "./GrammarParser.js";
import { MouseDoubleClickContext } from "./GrammarParser.js";
import { MouseDoubleClickSelectorContext } from "./GrammarParser.js";
import { MouseReleaseContext } from "./GrammarParser.js";
import { MouseReleaseSelectorContext } from "./GrammarParser.js";
import { MouseScrollContext } from "./GrammarParser.js";
import { MouseScrollSelectorContext } from "./GrammarParser.js";
import { KeyPressContext } from "./GrammarParser.js";
import { KeyReleaseContext } from "./GrammarParser.js";
import { KeyTypeContext } from "./GrammarParser.js";
import { KeyPressSelectorContext } from "./GrammarParser.js";
import { KeyReleaseSelectorContext } from "./GrammarParser.js";
import { KeyTypeSelectorContext } from "./GrammarParser.js";
import { MouseButtonContext } from "./GrammarParser.js";
import { NumberContext } from "./GrammarParser.js";


/**
 * This interface defines a complete listener for a parse tree produced by
 * `GrammarParser`.
 */
export default class GrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by `GrammarParser.root`.
	 * @param ctx the parse tree
	 */
	enterRoot?: (ctx: RootContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.root`.
	 * @param ctx the parse tree
	 */
	exitRoot?: (ctx: RootContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.stmt`.
	 * @param ctx the parse tree
	 */
	enterStmt?: (ctx: StmtContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.stmt`.
	 * @param ctx the parse tree
	 */
	exitStmt?: (ctx: StmtContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createDetector`.
	 * @param ctx the parse tree
	 */
	enterCreateDetector?: (ctx: CreateDetectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createDetector`.
	 * @param ctx the parse tree
	 */
	exitCreateDetector?: (ctx: CreateDetectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.useDetector`.
	 * @param ctx the parse tree
	 */
	enterUseDetector?: (ctx: UseDetectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.useDetector`.
	 * @param ctx the parse tree
	 */
	exitUseDetector?: (ctx: UseDetectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createSelectorByPosition`.
	 * @param ctx the parse tree
	 */
	enterCreateSelectorByPosition?: (ctx: CreateSelectorByPositionContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createSelectorByPosition`.
	 * @param ctx the parse tree
	 */
	exitCreateSelectorByPosition?: (ctx: CreateSelectorByPositionContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createSelectorByLabel`.
	 * @param ctx the parse tree
	 */
	enterCreateSelectorByLabel?: (ctx: CreateSelectorByLabelContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createSelectorByLabel`.
	 * @param ctx the parse tree
	 */
	exitCreateSelectorByLabel?: (ctx: CreateSelectorByLabelContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createSelectorByText`.
	 * @param ctx the parse tree
	 */
	enterCreateSelectorByText?: (ctx: CreateSelectorByTextContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createSelectorByText`.
	 * @param ctx the parse tree
	 */
	exitCreateSelectorByText?: (ctx: CreateSelectorByTextContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createSelectorByRegex`.
	 * @param ctx the parse tree
	 */
	enterCreateSelectorByRegex?: (ctx: CreateSelectorByRegexContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createSelectorByRegex`.
	 * @param ctx the parse tree
	 */
	exitCreateSelectorByRegex?: (ctx: CreateSelectorByRegexContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createOperation`.
	 * @param ctx the parse tree
	 */
	enterCreateOperation?: (ctx: CreateOperationContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createOperation`.
	 * @param ctx the parse tree
	 */
	exitCreateOperation?: (ctx: CreateOperationContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.selector`.
	 * @param ctx the parse tree
	 */
	enterSelector?: (ctx: SelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.selector`.
	 * @param ctx the parse tree
	 */
	exitSelector?: (ctx: SelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.selectorByLabel`.
	 * @param ctx the parse tree
	 */
	enterSelectorByLabel?: (ctx: SelectorByLabelContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.selectorByLabel`.
	 * @param ctx the parse tree
	 */
	exitSelectorByLabel?: (ctx: SelectorByLabelContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.selectorByText`.
	 * @param ctx the parse tree
	 */
	enterSelectorByText?: (ctx: SelectorByTextContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.selectorByText`.
	 * @param ctx the parse tree
	 */
	exitSelectorByText?: (ctx: SelectorByTextContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.selectorByRegex`.
	 * @param ctx the parse tree
	 */
	enterSelectorByRegex?: (ctx: SelectorByRegexContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.selectorByRegex`.
	 * @param ctx the parse tree
	 */
	exitSelectorByRegex?: (ctx: SelectorByRegexContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.selectorByPosition`.
	 * @param ctx the parse tree
	 */
	enterSelectorByPosition?: (ctx: SelectorByPositionContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.selectorByPosition`.
	 * @param ctx the parse tree
	 */
	exitSelectorByPosition?: (ctx: SelectorByPositionContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.selectorOrder`.
	 * @param ctx the parse tree
	 */
	enterSelectorOrder?: (ctx: SelectorOrderContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.selectorOrder`.
	 * @param ctx the parse tree
	 */
	exitSelectorOrder?: (ctx: SelectorOrderContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.createSequence`.
	 * @param ctx the parse tree
	 */
	enterCreateSequence?: (ctx: CreateSequenceContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.createSequence`.
	 * @param ctx the parse tree
	 */
	exitCreateSequence?: (ctx: CreateSequenceContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.runOperation`.
	 * @param ctx the parse tree
	 */
	enterRunOperation?: (ctx: RunOperationContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.runOperation`.
	 * @param ctx the parse tree
	 */
	exitRunOperation?: (ctx: RunOperationContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.operation`.
	 * @param ctx the parse tree
	 */
	enterOperation?: (ctx: OperationContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.operation`.
	 * @param ctx the parse tree
	 */
	exitOperation?: (ctx: OperationContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.wait`.
	 * @param ctx the parse tree
	 */
	enterWait?: (ctx: WaitContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.wait`.
	 * @param ctx the parse tree
	 */
	exitWait?: (ctx: WaitContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.waitSelector`.
	 * @param ctx the parse tree
	 */
	enterWaitSelector?: (ctx: WaitSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.waitSelector`.
	 * @param ctx the parse tree
	 */
	exitWaitSelector?: (ctx: WaitSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mousePress`.
	 * @param ctx the parse tree
	 */
	enterMousePress?: (ctx: MousePressContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mousePress`.
	 * @param ctx the parse tree
	 */
	exitMousePress?: (ctx: MousePressContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mousePressSelector`.
	 * @param ctx the parse tree
	 */
	enterMousePressSelector?: (ctx: MousePressSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mousePressSelector`.
	 * @param ctx the parse tree
	 */
	exitMousePressSelector?: (ctx: MousePressSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseClick`.
	 * @param ctx the parse tree
	 */
	enterMouseClick?: (ctx: MouseClickContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseClick`.
	 * @param ctx the parse tree
	 */
	exitMouseClick?: (ctx: MouseClickContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseClickSelector`.
	 * @param ctx the parse tree
	 */
	enterMouseClickSelector?: (ctx: MouseClickSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseClickSelector`.
	 * @param ctx the parse tree
	 */
	exitMouseClickSelector?: (ctx: MouseClickSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseDoubleClick`.
	 * @param ctx the parse tree
	 */
	enterMouseDoubleClick?: (ctx: MouseDoubleClickContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseDoubleClick`.
	 * @param ctx the parse tree
	 */
	exitMouseDoubleClick?: (ctx: MouseDoubleClickContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseDoubleClickSelector`.
	 * @param ctx the parse tree
	 */
	enterMouseDoubleClickSelector?: (ctx: MouseDoubleClickSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseDoubleClickSelector`.
	 * @param ctx the parse tree
	 */
	exitMouseDoubleClickSelector?: (ctx: MouseDoubleClickSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseRelease`.
	 * @param ctx the parse tree
	 */
	enterMouseRelease?: (ctx: MouseReleaseContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseRelease`.
	 * @param ctx the parse tree
	 */
	exitMouseRelease?: (ctx: MouseReleaseContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseReleaseSelector`.
	 * @param ctx the parse tree
	 */
	enterMouseReleaseSelector?: (ctx: MouseReleaseSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseReleaseSelector`.
	 * @param ctx the parse tree
	 */
	exitMouseReleaseSelector?: (ctx: MouseReleaseSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseScroll`.
	 * @param ctx the parse tree
	 */
	enterMouseScroll?: (ctx: MouseScrollContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseScroll`.
	 * @param ctx the parse tree
	 */
	exitMouseScroll?: (ctx: MouseScrollContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseScrollSelector`.
	 * @param ctx the parse tree
	 */
	enterMouseScrollSelector?: (ctx: MouseScrollSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseScrollSelector`.
	 * @param ctx the parse tree
	 */
	exitMouseScrollSelector?: (ctx: MouseScrollSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.keyPress`.
	 * @param ctx the parse tree
	 */
	enterKeyPress?: (ctx: KeyPressContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.keyPress`.
	 * @param ctx the parse tree
	 */
	exitKeyPress?: (ctx: KeyPressContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.keyRelease`.
	 * @param ctx the parse tree
	 */
	enterKeyRelease?: (ctx: KeyReleaseContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.keyRelease`.
	 * @param ctx the parse tree
	 */
	exitKeyRelease?: (ctx: KeyReleaseContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.keyType`.
	 * @param ctx the parse tree
	 */
	enterKeyType?: (ctx: KeyTypeContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.keyType`.
	 * @param ctx the parse tree
	 */
	exitKeyType?: (ctx: KeyTypeContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.keyPressSelector`.
	 * @param ctx the parse tree
	 */
	enterKeyPressSelector?: (ctx: KeyPressSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.keyPressSelector`.
	 * @param ctx the parse tree
	 */
	exitKeyPressSelector?: (ctx: KeyPressSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.keyReleaseSelector`.
	 * @param ctx the parse tree
	 */
	enterKeyReleaseSelector?: (ctx: KeyReleaseSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.keyReleaseSelector`.
	 * @param ctx the parse tree
	 */
	exitKeyReleaseSelector?: (ctx: KeyReleaseSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.keyTypeSelector`.
	 * @param ctx the parse tree
	 */
	enterKeyTypeSelector?: (ctx: KeyTypeSelectorContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.keyTypeSelector`.
	 * @param ctx the parse tree
	 */
	exitKeyTypeSelector?: (ctx: KeyTypeSelectorContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.mouseButton`.
	 * @param ctx the parse tree
	 */
	enterMouseButton?: (ctx: MouseButtonContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.mouseButton`.
	 * @param ctx the parse tree
	 */
	exitMouseButton?: (ctx: MouseButtonContext) => void;
	/**
	 * Enter a parse tree produced by `GrammarParser.number`.
	 * @param ctx the parse tree
	 */
	enterNumber?: (ctx: NumberContext) => void;
	/**
	 * Exit a parse tree produced by `GrammarParser.number`.
	 * @param ctx the parse tree
	 */
	exitNumber?: (ctx: NumberContext) => void;
}

