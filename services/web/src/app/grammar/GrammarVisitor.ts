// Generated from Grammar.g4 by ANTLR 4.13.2

import {ParseTreeVisitor} from 'antlr4';


import { RootContext } from "./GrammarParser.js";
import { StmtContext } from "./GrammarParser.js";
import { CreateDetectorContext } from "./GrammarParser.js";
import { UseDetectorContext } from "./GrammarParser.js";
import { CreateAndUseDetectorContext } from "./GrammarParser.js";
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
import { SelectorByImageContext } from "./GrammarParser.js";
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
import { KeyComboContext } from "./GrammarParser.js";
import { KeyComboSelectorContext } from "./GrammarParser.js";
import { KeyPressContext } from "./GrammarParser.js";
import { KeyReleaseContext } from "./GrammarParser.js";
import { KeyTypeContext } from "./GrammarParser.js";
import { KeyPressSelectorContext } from "./GrammarParser.js";
import { KeyReleaseSelectorContext } from "./GrammarParser.js";
import { KeyTypeSelectorContext } from "./GrammarParser.js";
import { MouseButtonContext } from "./GrammarParser.js";
import { NumberContext } from "./GrammarParser.js";


/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by `GrammarParser`.
 *
 * @param <Result> The return type of the visit operation. Use `void` for
 * operations with no return type.
 */
export default class GrammarVisitor<Result> extends ParseTreeVisitor<Result> {
	/**
	 * Visit a parse tree produced by `GrammarParser.root`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitRoot?: (ctx: RootContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.stmt`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitStmt?: (ctx: StmtContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createDetector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateDetector?: (ctx: CreateDetectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.useDetector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitUseDetector?: (ctx: UseDetectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createAndUseDetector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateAndUseDetector?: (ctx: CreateAndUseDetectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createSelectorByPosition`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateSelectorByPosition?: (ctx: CreateSelectorByPositionContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createSelectorByLabel`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateSelectorByLabel?: (ctx: CreateSelectorByLabelContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createSelectorByText`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateSelectorByText?: (ctx: CreateSelectorByTextContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createSelectorByRegex`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateSelectorByRegex?: (ctx: CreateSelectorByRegexContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createOperation`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateOperation?: (ctx: CreateOperationContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelector?: (ctx: SelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selectorByLabel`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelectorByLabel?: (ctx: SelectorByLabelContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selectorByText`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelectorByText?: (ctx: SelectorByTextContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selectorByRegex`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelectorByRegex?: (ctx: SelectorByRegexContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selectorByPosition`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelectorByPosition?: (ctx: SelectorByPositionContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selectorByImage`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelectorByImage?: (ctx: SelectorByImageContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.selectorOrder`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSelectorOrder?: (ctx: SelectorOrderContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.createSequence`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCreateSequence?: (ctx: CreateSequenceContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.runOperation`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitRunOperation?: (ctx: RunOperationContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.operation`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitOperation?: (ctx: OperationContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.wait`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitWait?: (ctx: WaitContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.waitSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitWaitSelector?: (ctx: WaitSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mousePress`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMousePress?: (ctx: MousePressContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mousePressSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMousePressSelector?: (ctx: MousePressSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseClick`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseClick?: (ctx: MouseClickContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseClickSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseClickSelector?: (ctx: MouseClickSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseDoubleClick`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseDoubleClick?: (ctx: MouseDoubleClickContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseDoubleClickSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseDoubleClickSelector?: (ctx: MouseDoubleClickSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseRelease`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseRelease?: (ctx: MouseReleaseContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseReleaseSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseReleaseSelector?: (ctx: MouseReleaseSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseScroll`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseScroll?: (ctx: MouseScrollContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseScrollSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseScrollSelector?: (ctx: MouseScrollSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyCombo`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyCombo?: (ctx: KeyComboContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyComboSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyComboSelector?: (ctx: KeyComboSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyPress`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyPress?: (ctx: KeyPressContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyRelease`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyRelease?: (ctx: KeyReleaseContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyType`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyType?: (ctx: KeyTypeContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyPressSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyPressSelector?: (ctx: KeyPressSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyReleaseSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyReleaseSelector?: (ctx: KeyReleaseSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.keyTypeSelector`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitKeyTypeSelector?: (ctx: KeyTypeSelectorContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.mouseButton`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMouseButton?: (ctx: MouseButtonContext) => Result;
	/**
	 * Visit a parse tree produced by `GrammarParser.number`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitNumber?: (ctx: NumberContext) => Result;
}

