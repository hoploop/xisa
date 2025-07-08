// Generated from Grammar.g4 by ANTLR 4.13.2
// noinspection ES6UnusedImports,JSUnusedGlobalSymbols,JSUnusedLocalSymbols

import {
	ATN,
	ATNDeserializer, DecisionState, DFA, FailedPredicateException,
	RecognitionException, NoViableAltException, BailErrorStrategy,
	Parser, ParserATNSimulator,
	RuleContext, ParserRuleContext, PredictionMode, PredictionContextCache,
	TerminalNode, RuleNode,
	Token, TokenStream,
	Interval, IntervalSet
} from 'antlr4';
import GrammarListener from "./GrammarListener.js";
import GrammarVisitor from "./GrammarVisitor.js";

// for running tests with parameters, TODO: discuss strategy for typed parameters in CI
// eslint-disable-next-line no-unused-vars
type int = number;

export default class GrammarParser extends Parser {
	public static readonly CONFIDENCE = 1;
	public static readonly GRAY = 2;
	public static readonly LEFT = 3;
	public static readonly RIGHT = 4;
	public static readonly MIDDLE = 5;
	public static readonly IMAGE = 6;
	public static readonly KEY_PRESS = 7;
	public static readonly KEY_TYPE = 8;
	public static readonly KEY_COMBO = 9;
	public static readonly KEY_RELEASE = 10;
	public static readonly MOUSE_CLICK = 11;
	public static readonly MOUSE_DOUBLE_CLICK = 12;
	public static readonly MOUSE_PRESS = 13;
	public static readonly MOUSE_RELEASE = 14;
	public static readonly MOUSE_SCROLL = 15;
	public static readonly WAIT = 16;
	public static readonly TEXT = 17;
	public static readonly POSITION = 18;
	public static readonly REGEX = 19;
	public static readonly COMMA = 20;
	public static readonly DCOMMA = 21;
	public static readonly LABEL = 22;
	public static readonly USE = 23;
	public static readonly SEQUENCE = 24;
	public static readonly DETECTOR = 25;
	public static readonly ID = 26;
	public static readonly STRING = 27;
	public static readonly ESC = 28;
	public static readonly ORPAR = 29;
	public static readonly EQ = 30;
	public static readonly CRPAR = 31;
	public static readonly OCPAR = 32;
	public static readonly CCPAR = 33;
	public static readonly INT = 34;
	public static readonly FLOAT = 35;
	public static readonly WS = 36;
	public static readonly COMMENT = 37;
	public static readonly LINE_COMMENT = 38;
	public static override readonly EOF = Token.EOF;
	public static readonly RULE_root = 0;
	public static readonly RULE_stmt = 1;
	public static readonly RULE_createDetector = 2;
	public static readonly RULE_useDetector = 3;
	public static readonly RULE_createAndUseDetector = 4;
	public static readonly RULE_createSelectorByPosition = 5;
	public static readonly RULE_createSelectorByLabel = 6;
	public static readonly RULE_createSelectorByText = 7;
	public static readonly RULE_createSelectorByRegex = 8;
	public static readonly RULE_createOperation = 9;
	public static readonly RULE_selector = 10;
	public static readonly RULE_selectorByLabel = 11;
	public static readonly RULE_selectorByText = 12;
	public static readonly RULE_selectorByRegex = 13;
	public static readonly RULE_selectorByPosition = 14;
	public static readonly RULE_selectorByImage = 15;
	public static readonly RULE_selectorOrder = 16;
	public static readonly RULE_createSequence = 17;
	public static readonly RULE_runOperation = 18;
	public static readonly RULE_operation = 19;
	public static readonly RULE_wait = 20;
	public static readonly RULE_waitSelector = 21;
	public static readonly RULE_mousePress = 22;
	public static readonly RULE_mousePressSelector = 23;
	public static readonly RULE_mouseClick = 24;
	public static readonly RULE_mouseClickSelector = 25;
	public static readonly RULE_mouseDoubleClick = 26;
	public static readonly RULE_mouseDoubleClickSelector = 27;
	public static readonly RULE_mouseRelease = 28;
	public static readonly RULE_mouseReleaseSelector = 29;
	public static readonly RULE_mouseScroll = 30;
	public static readonly RULE_mouseScrollSelector = 31;
	public static readonly RULE_keyCombo = 32;
	public static readonly RULE_keyComboSelector = 33;
	public static readonly RULE_keyPress = 34;
	public static readonly RULE_keyRelease = 35;
	public static readonly RULE_keyType = 36;
	public static readonly RULE_keyPressSelector = 37;
	public static readonly RULE_keyReleaseSelector = 38;
	public static readonly RULE_keyTypeSelector = 39;
	public static readonly RULE_mouseButton = 40;
	public static readonly RULE_number = 41;
	public static readonly literalNames: (string | null)[] = [ null, null, 
                                                            "'gray'", "'left'", 
                                                            "'right'", "'middle'", 
                                                            "'image'", "'keyPress'", 
                                                            "'keyType'", 
                                                            "'keyCombo'", 
                                                            "'keyRelease'", 
                                                            "'mouseClick'", 
                                                            "'mouseDoubleClick'", 
                                                            "'mousePress'", 
                                                            "'mouseRelease'", 
                                                            "'mouseScroll'", 
                                                            "'wait'", "'text'", 
                                                            "'position'", 
                                                            "'regex'", "','", 
                                                            "';'", "'label'", 
                                                            "'use'", "'sequence'", 
                                                            "'detector'", 
                                                            null, null, 
                                                            null, "'('", 
                                                            "'='", "')'", 
                                                            "'{'", "'}'" ];
	public static readonly symbolicNames: (string | null)[] = [ null, "CONFIDENCE", 
                                                             "GRAY", "LEFT", 
                                                             "RIGHT", "MIDDLE", 
                                                             "IMAGE", "KEY_PRESS", 
                                                             "KEY_TYPE", 
                                                             "KEY_COMBO", 
                                                             "KEY_RELEASE", 
                                                             "MOUSE_CLICK", 
                                                             "MOUSE_DOUBLE_CLICK", 
                                                             "MOUSE_PRESS", 
                                                             "MOUSE_RELEASE", 
                                                             "MOUSE_SCROLL", 
                                                             "WAIT", "TEXT", 
                                                             "POSITION", 
                                                             "REGEX", "COMMA", 
                                                             "DCOMMA", "LABEL", 
                                                             "USE", "SEQUENCE", 
                                                             "DETECTOR", 
                                                             "ID", "STRING", 
                                                             "ESC", "ORPAR", 
                                                             "EQ", "CRPAR", 
                                                             "OCPAR", "CCPAR", 
                                                             "INT", "FLOAT", 
                                                             "WS", "COMMENT", 
                                                             "LINE_COMMENT" ];
	// tslint:disable:no-trailing-whitespace
	public static readonly ruleNames: string[] = [
		"root", "stmt", "createDetector", "useDetector", "createAndUseDetector", 
		"createSelectorByPosition", "createSelectorByLabel", "createSelectorByText", 
		"createSelectorByRegex", "createOperation", "selector", "selectorByLabel", 
		"selectorByText", "selectorByRegex", "selectorByPosition", "selectorByImage", 
		"selectorOrder", "createSequence", "runOperation", "operation", "wait", 
		"waitSelector", "mousePress", "mousePressSelector", "mouseClick", "mouseClickSelector", 
		"mouseDoubleClick", "mouseDoubleClickSelector", "mouseRelease", "mouseReleaseSelector", 
		"mouseScroll", "mouseScrollSelector", "keyCombo", "keyComboSelector", 
		"keyPress", "keyRelease", "keyType", "keyPressSelector", "keyReleaseSelector", 
		"keyTypeSelector", "mouseButton", "number",
	];
	public get grammarFileName(): string { return "Grammar.g4"; }
	public get literalNames(): (string | null)[] { return GrammarParser.literalNames; }
	public get symbolicNames(): (string | null)[] { return GrammarParser.symbolicNames; }
	public get ruleNames(): string[] { return GrammarParser.ruleNames; }
	public get serializedATN(): number[] { return GrammarParser._serializedATN; }

	protected createFailedPredicateException(predicate?: string, message?: string): FailedPredicateException {
		return new FailedPredicateException(this, predicate, message);
	}

	constructor(input: TokenStream) {
		super(input);
		this._interp = new ParserATNSimulator(this, GrammarParser._ATN, GrammarParser.DecisionsToDFA, new PredictionContextCache());
	}
	// @RuleVersion(0)
	public root(): RootContext {
		let localctx: RootContext = new RootContext(this, this._ctx, this.state);
		this.enterRule(localctx, 0, GrammarParser.RULE_root);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 87;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while ((((_la) & ~0x1F) === 0 && ((1 << _la) & 75628416) !== 0)) {
				{
				{
				this.state = 84;
				this.stmt();
				}
				}
				this.state = 89;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public stmt(): StmtContext {
		let localctx: StmtContext = new StmtContext(this, this._ctx, this.state);
		this.enterRule(localctx, 2, GrammarParser.RULE_stmt);
		try {
			this.state = 98;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 1, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 90;
				this.createDetector();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 91;
				this.createSelectorByLabel();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 92;
				this.createSelectorByText();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 93;
				this.createSelectorByRegex();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 94;
				this.createSelectorByPosition();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 95;
				this.createOperation();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 96;
				this.createSequence();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 97;
				this.runOperation();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createDetector(): CreateDetectorContext {
		let localctx: CreateDetectorContext = new CreateDetectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 4, GrammarParser.RULE_createDetector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 100;
			this.match(GrammarParser.ID);
			this.state = 101;
			this.match(GrammarParser.EQ);
			this.state = 102;
			this.match(GrammarParser.DETECTOR);
			this.state = 103;
			this.match(GrammarParser.ORPAR);
			this.state = 104;
			this.match(GrammarParser.STRING);
			this.state = 105;
			this.match(GrammarParser.CRPAR);
			this.state = 106;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public useDetector(): UseDetectorContext {
		let localctx: UseDetectorContext = new UseDetectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 6, GrammarParser.RULE_useDetector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 108;
			this.match(GrammarParser.USE);
			this.state = 109;
			this.match(GrammarParser.ORPAR);
			this.state = 110;
			this.match(GrammarParser.ID);
			this.state = 113;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 111;
				this.match(GrammarParser.COMMA);
				this.state = 112;
				this.match(GrammarParser.FLOAT);
				}
			}

			this.state = 115;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createAndUseDetector(): CreateAndUseDetectorContext {
		let localctx: CreateAndUseDetectorContext = new CreateAndUseDetectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 8, GrammarParser.RULE_createAndUseDetector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 117;
			this.match(GrammarParser.USE);
			this.state = 118;
			this.match(GrammarParser.ORPAR);
			this.state = 119;
			this.match(GrammarParser.STRING);
			this.state = 122;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 120;
				this.match(GrammarParser.COMMA);
				this.state = 121;
				this.match(GrammarParser.FLOAT);
				}
			}

			this.state = 124;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createSelectorByPosition(): CreateSelectorByPositionContext {
		let localctx: CreateSelectorByPositionContext = new CreateSelectorByPositionContext(this, this._ctx, this.state);
		this.enterRule(localctx, 10, GrammarParser.RULE_createSelectorByPosition);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 126;
			this.match(GrammarParser.ID);
			this.state = 127;
			this.match(GrammarParser.EQ);
			this.state = 128;
			this.selectorByPosition();
			this.state = 129;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createSelectorByLabel(): CreateSelectorByLabelContext {
		let localctx: CreateSelectorByLabelContext = new CreateSelectorByLabelContext(this, this._ctx, this.state);
		this.enterRule(localctx, 12, GrammarParser.RULE_createSelectorByLabel);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 131;
			this.match(GrammarParser.ID);
			this.state = 132;
			this.match(GrammarParser.EQ);
			this.state = 133;
			this.selectorByLabel();
			this.state = 134;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createSelectorByText(): CreateSelectorByTextContext {
		let localctx: CreateSelectorByTextContext = new CreateSelectorByTextContext(this, this._ctx, this.state);
		this.enterRule(localctx, 14, GrammarParser.RULE_createSelectorByText);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 136;
			this.match(GrammarParser.ID);
			this.state = 137;
			this.match(GrammarParser.EQ);
			this.state = 138;
			this.selectorByText();
			this.state = 139;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createSelectorByRegex(): CreateSelectorByRegexContext {
		let localctx: CreateSelectorByRegexContext = new CreateSelectorByRegexContext(this, this._ctx, this.state);
		this.enterRule(localctx, 16, GrammarParser.RULE_createSelectorByRegex);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 141;
			this.match(GrammarParser.ID);
			this.state = 142;
			this.match(GrammarParser.EQ);
			this.state = 143;
			this.selectorByRegex();
			this.state = 144;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createOperation(): CreateOperationContext {
		let localctx: CreateOperationContext = new CreateOperationContext(this, this._ctx, this.state);
		this.enterRule(localctx, 18, GrammarParser.RULE_createOperation);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 146;
			this.match(GrammarParser.ID);
			this.state = 147;
			this.match(GrammarParser.EQ);
			this.state = 148;
			this.operation();
			this.state = 149;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selector(): SelectorContext {
		let localctx: SelectorContext = new SelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 20, GrammarParser.RULE_selector);
		try {
			this.state = 156;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 22:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 151;
				this.selectorByLabel();
				}
				break;
			case 17:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 152;
				this.selectorByText();
				}
				break;
			case 19:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 153;
				this.selectorByRegex();
				}
				break;
			case 18:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 154;
				this.selectorByPosition();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 155;
				this.selectorByImage();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selectorByLabel(): SelectorByLabelContext {
		let localctx: SelectorByLabelContext = new SelectorByLabelContext(this, this._ctx, this.state);
		this.enterRule(localctx, 22, GrammarParser.RULE_selectorByLabel);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 158;
			this.match(GrammarParser.LABEL);
			this.state = 159;
			this.match(GrammarParser.ORPAR);
			this.state = 160;
			this.match(GrammarParser.STRING);
			this.state = 163;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 161;
				this.match(GrammarParser.COMMA);
				this.state = 162;
				this.selectorOrder();
				}
			}

			this.state = 165;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selectorByText(): SelectorByTextContext {
		let localctx: SelectorByTextContext = new SelectorByTextContext(this, this._ctx, this.state);
		this.enterRule(localctx, 24, GrammarParser.RULE_selectorByText);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 167;
			this.match(GrammarParser.TEXT);
			this.state = 168;
			this.match(GrammarParser.ORPAR);
			this.state = 169;
			this.match(GrammarParser.STRING);
			this.state = 172;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 170;
				this.match(GrammarParser.COMMA);
				this.state = 171;
				this.selectorOrder();
				}
			}

			this.state = 174;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selectorByRegex(): SelectorByRegexContext {
		let localctx: SelectorByRegexContext = new SelectorByRegexContext(this, this._ctx, this.state);
		this.enterRule(localctx, 26, GrammarParser.RULE_selectorByRegex);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 176;
			this.match(GrammarParser.REGEX);
			this.state = 177;
			this.match(GrammarParser.ORPAR);
			this.state = 178;
			this.match(GrammarParser.STRING);
			this.state = 181;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 179;
				this.match(GrammarParser.COMMA);
				this.state = 180;
				this.selectorOrder();
				}
			}

			this.state = 183;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selectorByPosition(): SelectorByPositionContext {
		let localctx: SelectorByPositionContext = new SelectorByPositionContext(this, this._ctx, this.state);
		this.enterRule(localctx, 28, GrammarParser.RULE_selectorByPosition);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 185;
			this.match(GrammarParser.POSITION);
			this.state = 186;
			this.match(GrammarParser.ORPAR);
			this.state = 187;
			this.number_();
			this.state = 188;
			this.match(GrammarParser.COMMA);
			this.state = 189;
			this.number_();
			this.state = 190;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selectorByImage(): SelectorByImageContext {
		let localctx: SelectorByImageContext = new SelectorByImageContext(this, this._ctx, this.state);
		this.enterRule(localctx, 30, GrammarParser.RULE_selectorByImage);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 192;
			this.match(GrammarParser.IMAGE);
			this.state = 193;
			this.match(GrammarParser.ORPAR);
			this.state = 194;
			this.match(GrammarParser.STRING);
			this.state = 195;
			this.match(GrammarParser.COMMA);
			this.state = 196;
			this.match(GrammarParser.FLOAT);
			this.state = 199;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 8, this._ctx) ) {
			case 1:
				{
				this.state = 197;
				this.match(GrammarParser.COMMA);
				this.state = 198;
				this.selectorOrder();
				}
				break;
			}
			this.state = 203;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 201;
				this.match(GrammarParser.COMMA);
				this.state = 202;
				this.match(GrammarParser.GRAY);
				}
			}

			this.state = 205;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public selectorOrder(): SelectorOrderContext {
		let localctx: SelectorOrderContext = new SelectorOrderContext(this, this._ctx, this.state);
		this.enterRule(localctx, 32, GrammarParser.RULE_selectorOrder);
		try {
			let _alt: number;
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 207;
			this.match(GrammarParser.INT);
			this.state = 212;
			this._errHandler.sync(this);
			_alt = this._interp.adaptivePredict(this._input, 10, this._ctx);
			while (_alt !== 2 && _alt !== ATN.INVALID_ALT_NUMBER) {
				if (_alt === 1) {
					{
					{
					this.state = 208;
					this.match(GrammarParser.COMMA);
					this.state = 209;
					this.match(GrammarParser.INT);
					}
					}
				}
				this.state = 214;
				this._errHandler.sync(this);
				_alt = this._interp.adaptivePredict(this._input, 10, this._ctx);
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public createSequence(): CreateSequenceContext {
		let localctx: CreateSequenceContext = new CreateSequenceContext(this, this._ctx, this.state);
		this.enterRule(localctx, 34, GrammarParser.RULE_createSequence);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 215;
			this.match(GrammarParser.ID);
			this.state = 216;
			this.match(GrammarParser.EQ);
			this.state = 217;
			this.match(GrammarParser.SEQUENCE);
			this.state = 218;
			this.match(GrammarParser.OCPAR);
			this.state = 222;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while ((((_la) & ~0x1F) === 0 && ((1 << _la) & 75628416) !== 0)) {
				{
				{
				this.state = 219;
				this.stmt();
				}
				}
				this.state = 224;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			this.state = 225;
			this.match(GrammarParser.CCPAR);
			this.state = 226;
			this.match(GrammarParser.DCOMMA);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public runOperation(): RunOperationContext {
		let localctx: RunOperationContext = new RunOperationContext(this, this._ctx, this.state);
		this.enterRule(localctx, 36, GrammarParser.RULE_runOperation);
		try {
			this.state = 233;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 7:
			case 8:
			case 9:
			case 10:
			case 11:
			case 12:
			case 13:
			case 14:
			case 15:
			case 16:
			case 23:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 228;
				this.operation();
				this.state = 229;
				this.match(GrammarParser.DCOMMA);
				}
				break;
			case 26:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 231;
				this.match(GrammarParser.ID);
				this.state = 232;
				this.match(GrammarParser.DCOMMA);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public operation(): OperationContext {
		let localctx: OperationContext = new OperationContext(this, this._ctx, this.state);
		this.enterRule(localctx, 38, GrammarParser.RULE_operation);
		try {
			this.state = 257;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 13, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 235;
				this.wait();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 236;
				this.waitSelector();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 237;
				this.useDetector();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 238;
				this.createAndUseDetector();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 239;
				this.mousePress();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 240;
				this.mousePressSelector();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 241;
				this.mouseReleaseSelector();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 242;
				this.mouseClick();
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 243;
				this.mouseClickSelector();
				}
				break;
			case 10:
				this.enterOuterAlt(localctx, 10);
				{
				this.state = 244;
				this.mouseDoubleClick();
				}
				break;
			case 11:
				this.enterOuterAlt(localctx, 11);
				{
				this.state = 245;
				this.mouseDoubleClickSelector();
				}
				break;
			case 12:
				this.enterOuterAlt(localctx, 12);
				{
				this.state = 246;
				this.mouseRelease();
				}
				break;
			case 13:
				this.enterOuterAlt(localctx, 13);
				{
				this.state = 247;
				this.mouseScroll();
				}
				break;
			case 14:
				this.enterOuterAlt(localctx, 14);
				{
				this.state = 248;
				this.mouseScrollSelector();
				}
				break;
			case 15:
				this.enterOuterAlt(localctx, 15);
				{
				this.state = 249;
				this.keyPress();
				}
				break;
			case 16:
				this.enterOuterAlt(localctx, 16);
				{
				this.state = 250;
				this.keyRelease();
				}
				break;
			case 17:
				this.enterOuterAlt(localctx, 17);
				{
				this.state = 251;
				this.keyType();
				}
				break;
			case 18:
				this.enterOuterAlt(localctx, 18);
				{
				this.state = 252;
				this.keyCombo();
				}
				break;
			case 19:
				this.enterOuterAlt(localctx, 19);
				{
				this.state = 253;
				this.keyComboSelector();
				}
				break;
			case 20:
				this.enterOuterAlt(localctx, 20);
				{
				this.state = 254;
				this.keyPressSelector();
				}
				break;
			case 21:
				this.enterOuterAlt(localctx, 21);
				{
				this.state = 255;
				this.keyReleaseSelector();
				}
				break;
			case 22:
				this.enterOuterAlt(localctx, 22);
				{
				this.state = 256;
				this.keyTypeSelector();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public wait(): WaitContext {
		let localctx: WaitContext = new WaitContext(this, this._ctx, this.state);
		this.enterRule(localctx, 40, GrammarParser.RULE_wait);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 259;
			this.match(GrammarParser.WAIT);
			this.state = 260;
			this.match(GrammarParser.ORPAR);
			this.state = 261;
			this.match(GrammarParser.ID);
			this.state = 264;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 262;
				this.match(GrammarParser.COMMA);
				this.state = 263;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 266;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public waitSelector(): WaitSelectorContext {
		let localctx: WaitSelectorContext = new WaitSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 42, GrammarParser.RULE_waitSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 268;
			this.match(GrammarParser.WAIT);
			this.state = 269;
			this.match(GrammarParser.ORPAR);
			this.state = 270;
			this.selector();
			this.state = 273;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 271;
				this.match(GrammarParser.COMMA);
				this.state = 272;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 275;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mousePress(): MousePressContext {
		let localctx: MousePressContext = new MousePressContext(this, this._ctx, this.state);
		this.enterRule(localctx, 44, GrammarParser.RULE_mousePress);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 277;
			this.match(GrammarParser.MOUSE_PRESS);
			this.state = 278;
			this.match(GrammarParser.ORPAR);
			this.state = 279;
			this.match(GrammarParser.ID);
			this.state = 282;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 280;
				this.match(GrammarParser.COMMA);
				this.state = 281;
				this.mouseButton();
				}
			}

			this.state = 284;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mousePressSelector(): MousePressSelectorContext {
		let localctx: MousePressSelectorContext = new MousePressSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 46, GrammarParser.RULE_mousePressSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 286;
			this.match(GrammarParser.MOUSE_PRESS);
			this.state = 287;
			this.match(GrammarParser.ORPAR);
			this.state = 288;
			this.selector();
			this.state = 291;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 289;
				this.match(GrammarParser.COMMA);
				this.state = 290;
				this.mouseButton();
				}
			}

			this.state = 293;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseClick(): MouseClickContext {
		let localctx: MouseClickContext = new MouseClickContext(this, this._ctx, this.state);
		this.enterRule(localctx, 48, GrammarParser.RULE_mouseClick);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 295;
			this.match(GrammarParser.MOUSE_CLICK);
			this.state = 296;
			this.match(GrammarParser.ORPAR);
			this.state = 297;
			this.match(GrammarParser.ID);
			this.state = 300;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 298;
				this.match(GrammarParser.COMMA);
				this.state = 299;
				this.mouseButton();
				}
			}

			this.state = 302;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseClickSelector(): MouseClickSelectorContext {
		let localctx: MouseClickSelectorContext = new MouseClickSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 50, GrammarParser.RULE_mouseClickSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 304;
			this.match(GrammarParser.MOUSE_CLICK);
			this.state = 305;
			this.match(GrammarParser.ORPAR);
			this.state = 306;
			this.selector();
			this.state = 309;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 307;
				this.match(GrammarParser.COMMA);
				this.state = 308;
				this.mouseButton();
				}
			}

			this.state = 311;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseDoubleClick(): MouseDoubleClickContext {
		let localctx: MouseDoubleClickContext = new MouseDoubleClickContext(this, this._ctx, this.state);
		this.enterRule(localctx, 52, GrammarParser.RULE_mouseDoubleClick);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 313;
			this.match(GrammarParser.MOUSE_DOUBLE_CLICK);
			this.state = 314;
			this.match(GrammarParser.ORPAR);
			this.state = 315;
			this.match(GrammarParser.ID);
			this.state = 318;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 316;
				this.match(GrammarParser.COMMA);
				this.state = 317;
				this.mouseButton();
				}
			}

			this.state = 320;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseDoubleClickSelector(): MouseDoubleClickSelectorContext {
		let localctx: MouseDoubleClickSelectorContext = new MouseDoubleClickSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 54, GrammarParser.RULE_mouseDoubleClickSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 322;
			this.match(GrammarParser.MOUSE_DOUBLE_CLICK);
			this.state = 323;
			this.match(GrammarParser.ORPAR);
			this.state = 324;
			this.selector();
			this.state = 327;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 325;
				this.match(GrammarParser.COMMA);
				this.state = 326;
				this.mouseButton();
				}
			}

			this.state = 329;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseRelease(): MouseReleaseContext {
		let localctx: MouseReleaseContext = new MouseReleaseContext(this, this._ctx, this.state);
		this.enterRule(localctx, 56, GrammarParser.RULE_mouseRelease);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 331;
			this.match(GrammarParser.MOUSE_RELEASE);
			this.state = 332;
			this.match(GrammarParser.ORPAR);
			this.state = 333;
			this.match(GrammarParser.ID);
			this.state = 336;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 334;
				this.match(GrammarParser.COMMA);
				this.state = 335;
				this.mouseButton();
				}
			}

			this.state = 338;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseReleaseSelector(): MouseReleaseSelectorContext {
		let localctx: MouseReleaseSelectorContext = new MouseReleaseSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 58, GrammarParser.RULE_mouseReleaseSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 340;
			this.match(GrammarParser.MOUSE_RELEASE);
			this.state = 341;
			this.match(GrammarParser.ORPAR);
			this.state = 342;
			this.selector();
			this.state = 345;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 343;
				this.match(GrammarParser.COMMA);
				this.state = 344;
				this.mouseButton();
				}
			}

			this.state = 347;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseScroll(): MouseScrollContext {
		let localctx: MouseScrollContext = new MouseScrollContext(this, this._ctx, this.state);
		this.enterRule(localctx, 60, GrammarParser.RULE_mouseScroll);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 349;
			this.match(GrammarParser.MOUSE_SCROLL);
			this.state = 350;
			this.match(GrammarParser.ORPAR);
			this.state = 351;
			this.match(GrammarParser.ID);
			this.state = 352;
			this.match(GrammarParser.COMMA);
			this.state = 353;
			this.match(GrammarParser.INT);
			this.state = 356;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 354;
				this.match(GrammarParser.COMMA);
				this.state = 355;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 358;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseScrollSelector(): MouseScrollSelectorContext {
		let localctx: MouseScrollSelectorContext = new MouseScrollSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 62, GrammarParser.RULE_mouseScrollSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 360;
			this.match(GrammarParser.MOUSE_SCROLL);
			this.state = 361;
			this.match(GrammarParser.ORPAR);
			this.state = 362;
			this.selector();
			this.state = 363;
			this.match(GrammarParser.COMMA);
			this.state = 364;
			this.match(GrammarParser.INT);
			this.state = 367;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===20) {
				{
				this.state = 365;
				this.match(GrammarParser.COMMA);
				this.state = 366;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 369;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyCombo(): KeyComboContext {
		let localctx: KeyComboContext = new KeyComboContext(this, this._ctx, this.state);
		this.enterRule(localctx, 64, GrammarParser.RULE_keyCombo);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 371;
			this.match(GrammarParser.KEY_COMBO);
			this.state = 372;
			this.match(GrammarParser.ORPAR);
			this.state = 373;
			this.match(GrammarParser.ID);
			this.state = 374;
			this.match(GrammarParser.STRING);
			this.state = 377;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			do {
				{
				{
				this.state = 375;
				this.match(GrammarParser.COMMA);
				this.state = 376;
				this.match(GrammarParser.STRING);
				}
				}
				this.state = 379;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			} while (_la===20);
			this.state = 381;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyComboSelector(): KeyComboSelectorContext {
		let localctx: KeyComboSelectorContext = new KeyComboSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 66, GrammarParser.RULE_keyComboSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 383;
			this.match(GrammarParser.KEY_COMBO);
			this.state = 384;
			this.match(GrammarParser.ORPAR);
			this.state = 385;
			this.selector();
			this.state = 386;
			this.match(GrammarParser.STRING);
			this.state = 389;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			do {
				{
				{
				this.state = 387;
				this.match(GrammarParser.COMMA);
				this.state = 388;
				this.match(GrammarParser.STRING);
				}
				}
				this.state = 391;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			} while (_la===20);
			this.state = 393;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyPress(): KeyPressContext {
		let localctx: KeyPressContext = new KeyPressContext(this, this._ctx, this.state);
		this.enterRule(localctx, 68, GrammarParser.RULE_keyPress);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 395;
			this.match(GrammarParser.KEY_PRESS);
			this.state = 396;
			this.match(GrammarParser.ORPAR);
			this.state = 397;
			this.match(GrammarParser.ID);
			this.state = 398;
			this.match(GrammarParser.COMMA);
			this.state = 399;
			this.match(GrammarParser.STRING);
			this.state = 400;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyRelease(): KeyReleaseContext {
		let localctx: KeyReleaseContext = new KeyReleaseContext(this, this._ctx, this.state);
		this.enterRule(localctx, 70, GrammarParser.RULE_keyRelease);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 402;
			this.match(GrammarParser.KEY_RELEASE);
			this.state = 403;
			this.match(GrammarParser.ORPAR);
			this.state = 404;
			this.match(GrammarParser.ID);
			this.state = 405;
			this.match(GrammarParser.COMMA);
			this.state = 406;
			this.match(GrammarParser.STRING);
			this.state = 407;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyType(): KeyTypeContext {
		let localctx: KeyTypeContext = new KeyTypeContext(this, this._ctx, this.state);
		this.enterRule(localctx, 72, GrammarParser.RULE_keyType);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 409;
			this.match(GrammarParser.KEY_TYPE);
			this.state = 410;
			this.match(GrammarParser.ORPAR);
			this.state = 411;
			this.match(GrammarParser.ID);
			this.state = 412;
			this.match(GrammarParser.COMMA);
			this.state = 413;
			this.match(GrammarParser.STRING);
			this.state = 414;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyPressSelector(): KeyPressSelectorContext {
		let localctx: KeyPressSelectorContext = new KeyPressSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 74, GrammarParser.RULE_keyPressSelector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 416;
			this.match(GrammarParser.KEY_PRESS);
			this.state = 417;
			this.match(GrammarParser.ORPAR);
			this.state = 418;
			this.selector();
			this.state = 419;
			this.match(GrammarParser.COMMA);
			this.state = 420;
			this.match(GrammarParser.STRING);
			this.state = 421;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyReleaseSelector(): KeyReleaseSelectorContext {
		let localctx: KeyReleaseSelectorContext = new KeyReleaseSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 76, GrammarParser.RULE_keyReleaseSelector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 423;
			this.match(GrammarParser.KEY_RELEASE);
			this.state = 424;
			this.match(GrammarParser.ORPAR);
			this.state = 425;
			this.selector();
			this.state = 426;
			this.match(GrammarParser.COMMA);
			this.state = 427;
			this.match(GrammarParser.STRING);
			this.state = 428;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public keyTypeSelector(): KeyTypeSelectorContext {
		let localctx: KeyTypeSelectorContext = new KeyTypeSelectorContext(this, this._ctx, this.state);
		this.enterRule(localctx, 78, GrammarParser.RULE_keyTypeSelector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 430;
			this.match(GrammarParser.KEY_TYPE);
			this.state = 431;
			this.match(GrammarParser.ORPAR);
			this.state = 432;
			this.selector();
			this.state = 433;
			this.match(GrammarParser.COMMA);
			this.state = 434;
			this.match(GrammarParser.STRING);
			this.state = 435;
			this.match(GrammarParser.CRPAR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mouseButton(): MouseButtonContext {
		let localctx: MouseButtonContext = new MouseButtonContext(this, this._ctx, this.state);
		this.enterRule(localctx, 80, GrammarParser.RULE_mouseButton);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 437;
			_la = this._input.LA(1);
			if(!((((_la) & ~0x1F) === 0 && ((1 << _la) & 56) !== 0))) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public number_(): NumberContext {
		let localctx: NumberContext = new NumberContext(this, this._ctx, this.state);
		this.enterRule(localctx, 82, GrammarParser.RULE_number);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 439;
			_la = this._input.LA(1);
			if(!(_la===34 || _la===35)) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}

	public static readonly _serializedATN: number[] = [4,1,38,442,2,0,7,0,2,
	1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,
	10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,
	7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,
	24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,
	2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
	39,7,39,2,40,7,40,2,41,7,41,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,1,1,1,1,1,
	1,1,1,1,1,1,1,1,1,1,3,1,99,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
	1,3,1,3,1,3,3,3,114,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,123,8,4,1,4,1,4,
	1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
	1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,157,8,10,1,11,
	1,11,1,11,1,11,1,11,3,11,164,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,
	12,173,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,182,8,13,1,13,1,13,
	1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
	15,200,8,15,1,15,1,15,3,15,204,8,15,1,15,1,15,1,16,1,16,1,16,5,16,211,8,
	16,10,16,12,16,214,9,16,1,17,1,17,1,17,1,17,1,17,5,17,221,8,17,10,17,12,
	17,224,9,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,234,8,18,1,19,
	1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
	19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,258,8,19,1,20,1,20,1,20,1,20,1,20,
	3,20,265,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,21,274,8,21,1,21,1,21,
	1,22,1,22,1,22,1,22,1,22,3,22,283,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,
	23,3,23,292,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,301,8,24,1,24,
	1,24,1,25,1,25,1,25,1,25,1,25,3,25,310,8,25,1,25,1,25,1,26,1,26,1,26,1,
	26,1,26,3,26,319,8,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,328,8,27,
	1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,337,8,28,1,28,1,28,1,29,1,29,1,
	29,1,29,1,29,3,29,346,8,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
	3,30,357,8,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,368,8,31,
	1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,4,32,378,8,32,11,32,12,32,379,1,
	32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,4,33,390,8,33,11,33,12,33,391,1,33,
	1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,
	35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
	1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,
	40,1,40,1,41,1,41,1,41,0,0,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
	32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
	80,82,0,2,1,0,3,5,1,0,34,35,456,0,87,1,0,0,0,2,98,1,0,0,0,4,100,1,0,0,0,
	6,108,1,0,0,0,8,117,1,0,0,0,10,126,1,0,0,0,12,131,1,0,0,0,14,136,1,0,0,
	0,16,141,1,0,0,0,18,146,1,0,0,0,20,156,1,0,0,0,22,158,1,0,0,0,24,167,1,
	0,0,0,26,176,1,0,0,0,28,185,1,0,0,0,30,192,1,0,0,0,32,207,1,0,0,0,34,215,
	1,0,0,0,36,233,1,0,0,0,38,257,1,0,0,0,40,259,1,0,0,0,42,268,1,0,0,0,44,
	277,1,0,0,0,46,286,1,0,0,0,48,295,1,0,0,0,50,304,1,0,0,0,52,313,1,0,0,0,
	54,322,1,0,0,0,56,331,1,0,0,0,58,340,1,0,0,0,60,349,1,0,0,0,62,360,1,0,
	0,0,64,371,1,0,0,0,66,383,1,0,0,0,68,395,1,0,0,0,70,402,1,0,0,0,72,409,
	1,0,0,0,74,416,1,0,0,0,76,423,1,0,0,0,78,430,1,0,0,0,80,437,1,0,0,0,82,
	439,1,0,0,0,84,86,3,2,1,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,
	88,1,0,0,0,88,1,1,0,0,0,89,87,1,0,0,0,90,99,3,4,2,0,91,99,3,12,6,0,92,99,
	3,14,7,0,93,99,3,16,8,0,94,99,3,10,5,0,95,99,3,18,9,0,96,99,3,34,17,0,97,
	99,3,36,18,0,98,90,1,0,0,0,98,91,1,0,0,0,98,92,1,0,0,0,98,93,1,0,0,0,98,
	94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,3,1,0,0,0,100,101,
	5,26,0,0,101,102,5,30,0,0,102,103,5,25,0,0,103,104,5,29,0,0,104,105,5,27,
	0,0,105,106,5,31,0,0,106,107,5,21,0,0,107,5,1,0,0,0,108,109,5,23,0,0,109,
	110,5,29,0,0,110,113,5,26,0,0,111,112,5,20,0,0,112,114,5,35,0,0,113,111,
	1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,31,0,0,116,7,1,0,0,0,
	117,118,5,23,0,0,118,119,5,29,0,0,119,122,5,27,0,0,120,121,5,20,0,0,121,
	123,5,35,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,5,
	31,0,0,125,9,1,0,0,0,126,127,5,26,0,0,127,128,5,30,0,0,128,129,3,28,14,
	0,129,130,5,21,0,0,130,11,1,0,0,0,131,132,5,26,0,0,132,133,5,30,0,0,133,
	134,3,22,11,0,134,135,5,21,0,0,135,13,1,0,0,0,136,137,5,26,0,0,137,138,
	5,30,0,0,138,139,3,24,12,0,139,140,5,21,0,0,140,15,1,0,0,0,141,142,5,26,
	0,0,142,143,5,30,0,0,143,144,3,26,13,0,144,145,5,21,0,0,145,17,1,0,0,0,
	146,147,5,26,0,0,147,148,5,30,0,0,148,149,3,38,19,0,149,150,5,21,0,0,150,
	19,1,0,0,0,151,157,3,22,11,0,152,157,3,24,12,0,153,157,3,26,13,0,154,157,
	3,28,14,0,155,157,3,30,15,0,156,151,1,0,0,0,156,152,1,0,0,0,156,153,1,0,
	0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,21,1,0,0,0,158,159,5,22,0,0,159,
	160,5,29,0,0,160,163,5,27,0,0,161,162,5,20,0,0,162,164,3,32,16,0,163,161,
	1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,5,31,0,0,166,23,1,0,0,0,
	167,168,5,17,0,0,168,169,5,29,0,0,169,172,5,27,0,0,170,171,5,20,0,0,171,
	173,3,32,16,0,172,170,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,5,
	31,0,0,175,25,1,0,0,0,176,177,5,19,0,0,177,178,5,29,0,0,178,181,5,27,0,
	0,179,180,5,20,0,0,180,182,3,32,16,0,181,179,1,0,0,0,181,182,1,0,0,0,182,
	183,1,0,0,0,183,184,5,31,0,0,184,27,1,0,0,0,185,186,5,18,0,0,186,187,5,
	29,0,0,187,188,3,82,41,0,188,189,5,20,0,0,189,190,3,82,41,0,190,191,5,31,
	0,0,191,29,1,0,0,0,192,193,5,6,0,0,193,194,5,29,0,0,194,195,5,27,0,0,195,
	196,5,20,0,0,196,199,5,35,0,0,197,198,5,20,0,0,198,200,3,32,16,0,199,197,
	1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,202,5,20,0,0,202,204,5,2,0,
	0,203,201,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,31,0,0,206,
	31,1,0,0,0,207,212,5,34,0,0,208,209,5,20,0,0,209,211,5,34,0,0,210,208,1,
	0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,33,1,0,0,0,214,
	212,1,0,0,0,215,216,5,26,0,0,216,217,5,30,0,0,217,218,5,24,0,0,218,222,
	5,32,0,0,219,221,3,2,1,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,
	0,222,223,1,0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,226,5,33,0,0,226,
	227,5,21,0,0,227,35,1,0,0,0,228,229,3,38,19,0,229,230,5,21,0,0,230,234,
	1,0,0,0,231,232,5,26,0,0,232,234,5,21,0,0,233,228,1,0,0,0,233,231,1,0,0,
	0,234,37,1,0,0,0,235,258,3,40,20,0,236,258,3,42,21,0,237,258,3,6,3,0,238,
	258,3,8,4,0,239,258,3,44,22,0,240,258,3,46,23,0,241,258,3,58,29,0,242,258,
	3,48,24,0,243,258,3,50,25,0,244,258,3,52,26,0,245,258,3,54,27,0,246,258,
	3,56,28,0,247,258,3,60,30,0,248,258,3,62,31,0,249,258,3,68,34,0,250,258,
	3,70,35,0,251,258,3,72,36,0,252,258,3,64,32,0,253,258,3,66,33,0,254,258,
	3,74,37,0,255,258,3,76,38,0,256,258,3,78,39,0,257,235,1,0,0,0,257,236,1,
	0,0,0,257,237,1,0,0,0,257,238,1,0,0,0,257,239,1,0,0,0,257,240,1,0,0,0,257,
	241,1,0,0,0,257,242,1,0,0,0,257,243,1,0,0,0,257,244,1,0,0,0,257,245,1,0,
	0,0,257,246,1,0,0,0,257,247,1,0,0,0,257,248,1,0,0,0,257,249,1,0,0,0,257,
	250,1,0,0,0,257,251,1,0,0,0,257,252,1,0,0,0,257,253,1,0,0,0,257,254,1,0,
	0,0,257,255,1,0,0,0,257,256,1,0,0,0,258,39,1,0,0,0,259,260,5,16,0,0,260,
	261,5,29,0,0,261,264,5,26,0,0,262,263,5,20,0,0,263,265,5,34,0,0,264,262,
	1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,267,5,31,0,0,267,41,1,0,0,0,
	268,269,5,16,0,0,269,270,5,29,0,0,270,273,3,20,10,0,271,272,5,20,0,0,272,
	274,5,34,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,276,5,
	31,0,0,276,43,1,0,0,0,277,278,5,13,0,0,278,279,5,29,0,0,279,282,5,26,0,
	0,280,281,5,20,0,0,281,283,3,80,40,0,282,280,1,0,0,0,282,283,1,0,0,0,283,
	284,1,0,0,0,284,285,5,31,0,0,285,45,1,0,0,0,286,287,5,13,0,0,287,288,5,
	29,0,0,288,291,3,20,10,0,289,290,5,20,0,0,290,292,3,80,40,0,291,289,1,0,
	0,0,291,292,1,0,0,0,292,293,1,0,0,0,293,294,5,31,0,0,294,47,1,0,0,0,295,
	296,5,11,0,0,296,297,5,29,0,0,297,300,5,26,0,0,298,299,5,20,0,0,299,301,
	3,80,40,0,300,298,1,0,0,0,300,301,1,0,0,0,301,302,1,0,0,0,302,303,5,31,
	0,0,303,49,1,0,0,0,304,305,5,11,0,0,305,306,5,29,0,0,306,309,3,20,10,0,
	307,308,5,20,0,0,308,310,3,80,40,0,309,307,1,0,0,0,309,310,1,0,0,0,310,
	311,1,0,0,0,311,312,5,31,0,0,312,51,1,0,0,0,313,314,5,12,0,0,314,315,5,
	29,0,0,315,318,5,26,0,0,316,317,5,20,0,0,317,319,3,80,40,0,318,316,1,0,
	0,0,318,319,1,0,0,0,319,320,1,0,0,0,320,321,5,31,0,0,321,53,1,0,0,0,322,
	323,5,12,0,0,323,324,5,29,0,0,324,327,3,20,10,0,325,326,5,20,0,0,326,328,
	3,80,40,0,327,325,1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,330,5,31,
	0,0,330,55,1,0,0,0,331,332,5,14,0,0,332,333,5,29,0,0,333,336,5,26,0,0,334,
	335,5,20,0,0,335,337,3,80,40,0,336,334,1,0,0,0,336,337,1,0,0,0,337,338,
	1,0,0,0,338,339,5,31,0,0,339,57,1,0,0,0,340,341,5,14,0,0,341,342,5,29,0,
	0,342,345,3,20,10,0,343,344,5,20,0,0,344,346,3,80,40,0,345,343,1,0,0,0,
	345,346,1,0,0,0,346,347,1,0,0,0,347,348,5,31,0,0,348,59,1,0,0,0,349,350,
	5,15,0,0,350,351,5,29,0,0,351,352,5,26,0,0,352,353,5,20,0,0,353,356,5,34,
	0,0,354,355,5,20,0,0,355,357,5,34,0,0,356,354,1,0,0,0,356,357,1,0,0,0,357,
	358,1,0,0,0,358,359,5,31,0,0,359,61,1,0,0,0,360,361,5,15,0,0,361,362,5,
	29,0,0,362,363,3,20,10,0,363,364,5,20,0,0,364,367,5,34,0,0,365,366,5,20,
	0,0,366,368,5,34,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,369,1,0,0,0,369,
	370,5,31,0,0,370,63,1,0,0,0,371,372,5,9,0,0,372,373,5,29,0,0,373,374,5,
	26,0,0,374,377,5,27,0,0,375,376,5,20,0,0,376,378,5,27,0,0,377,375,1,0,0,
	0,378,379,1,0,0,0,379,377,1,0,0,0,379,380,1,0,0,0,380,381,1,0,0,0,381,382,
	5,31,0,0,382,65,1,0,0,0,383,384,5,9,0,0,384,385,5,29,0,0,385,386,3,20,10,
	0,386,389,5,27,0,0,387,388,5,20,0,0,388,390,5,27,0,0,389,387,1,0,0,0,390,
	391,1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,393,1,0,0,0,393,394,5,31,
	0,0,394,67,1,0,0,0,395,396,5,7,0,0,396,397,5,29,0,0,397,398,5,26,0,0,398,
	399,5,20,0,0,399,400,5,27,0,0,400,401,5,31,0,0,401,69,1,0,0,0,402,403,5,
	10,0,0,403,404,5,29,0,0,404,405,5,26,0,0,405,406,5,20,0,0,406,407,5,27,
	0,0,407,408,5,31,0,0,408,71,1,0,0,0,409,410,5,8,0,0,410,411,5,29,0,0,411,
	412,5,26,0,0,412,413,5,20,0,0,413,414,5,27,0,0,414,415,5,31,0,0,415,73,
	1,0,0,0,416,417,5,7,0,0,417,418,5,29,0,0,418,419,3,20,10,0,419,420,5,20,
	0,0,420,421,5,27,0,0,421,422,5,31,0,0,422,75,1,0,0,0,423,424,5,10,0,0,424,
	425,5,29,0,0,425,426,3,20,10,0,426,427,5,20,0,0,427,428,5,27,0,0,428,429,
	5,31,0,0,429,77,1,0,0,0,430,431,5,8,0,0,431,432,5,29,0,0,432,433,3,20,10,
	0,433,434,5,20,0,0,434,435,5,27,0,0,435,436,5,31,0,0,436,79,1,0,0,0,437,
	438,7,0,0,0,438,81,1,0,0,0,439,440,7,1,0,0,440,83,1,0,0,0,28,87,98,113,
	122,156,163,172,181,199,203,212,222,233,257,264,273,282,291,300,309,318,
	327,336,345,356,367,379,391];

	private static __ATN: ATN;
	public static get _ATN(): ATN {
		if (!GrammarParser.__ATN) {
			GrammarParser.__ATN = new ATNDeserializer().deserialize(GrammarParser._serializedATN);
		}

		return GrammarParser.__ATN;
	}


	static DecisionsToDFA = GrammarParser._ATN.decisionToState.map( (ds: DecisionState, index: number) => new DFA(ds, index) );

}

export class RootContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public stmt_list(): StmtContext[] {
		return this.getTypedRuleContexts(StmtContext) as StmtContext[];
	}
	public stmt(i: number): StmtContext {
		return this.getTypedRuleContext(StmtContext, i) as StmtContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_root;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterRoot) {
	 		listener.enterRoot(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitRoot) {
	 		listener.exitRoot(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitRoot) {
			return visitor.visitRoot(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class StmtContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public createDetector(): CreateDetectorContext {
		return this.getTypedRuleContext(CreateDetectorContext, 0) as CreateDetectorContext;
	}
	public createSelectorByLabel(): CreateSelectorByLabelContext {
		return this.getTypedRuleContext(CreateSelectorByLabelContext, 0) as CreateSelectorByLabelContext;
	}
	public createSelectorByText(): CreateSelectorByTextContext {
		return this.getTypedRuleContext(CreateSelectorByTextContext, 0) as CreateSelectorByTextContext;
	}
	public createSelectorByRegex(): CreateSelectorByRegexContext {
		return this.getTypedRuleContext(CreateSelectorByRegexContext, 0) as CreateSelectorByRegexContext;
	}
	public createSelectorByPosition(): CreateSelectorByPositionContext {
		return this.getTypedRuleContext(CreateSelectorByPositionContext, 0) as CreateSelectorByPositionContext;
	}
	public createOperation(): CreateOperationContext {
		return this.getTypedRuleContext(CreateOperationContext, 0) as CreateOperationContext;
	}
	public createSequence(): CreateSequenceContext {
		return this.getTypedRuleContext(CreateSequenceContext, 0) as CreateSequenceContext;
	}
	public runOperation(): RunOperationContext {
		return this.getTypedRuleContext(RunOperationContext, 0) as RunOperationContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_stmt;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterStmt) {
	 		listener.enterStmt(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitStmt) {
	 		listener.exitStmt(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitStmt) {
			return visitor.visitStmt(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateDetectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public DETECTOR(): TerminalNode {
		return this.getToken(GrammarParser.DETECTOR, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createDetector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateDetector) {
	 		listener.enterCreateDetector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateDetector) {
	 		listener.exitCreateDetector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateDetector) {
			return visitor.visitCreateDetector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class UseDetectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public USE(): TerminalNode {
		return this.getToken(GrammarParser.USE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public FLOAT(): TerminalNode {
		return this.getToken(GrammarParser.FLOAT, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_useDetector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterUseDetector) {
	 		listener.enterUseDetector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitUseDetector) {
	 		listener.exitUseDetector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitUseDetector) {
			return visitor.visitUseDetector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateAndUseDetectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public USE(): TerminalNode {
		return this.getToken(GrammarParser.USE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public FLOAT(): TerminalNode {
		return this.getToken(GrammarParser.FLOAT, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createAndUseDetector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateAndUseDetector) {
	 		listener.enterCreateAndUseDetector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateAndUseDetector) {
	 		listener.exitCreateAndUseDetector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateAndUseDetector) {
			return visitor.visitCreateAndUseDetector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateSelectorByPositionContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public selectorByPosition(): SelectorByPositionContext {
		return this.getTypedRuleContext(SelectorByPositionContext, 0) as SelectorByPositionContext;
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createSelectorByPosition;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateSelectorByPosition) {
	 		listener.enterCreateSelectorByPosition(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateSelectorByPosition) {
	 		listener.exitCreateSelectorByPosition(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateSelectorByPosition) {
			return visitor.visitCreateSelectorByPosition(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateSelectorByLabelContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public selectorByLabel(): SelectorByLabelContext {
		return this.getTypedRuleContext(SelectorByLabelContext, 0) as SelectorByLabelContext;
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createSelectorByLabel;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateSelectorByLabel) {
	 		listener.enterCreateSelectorByLabel(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateSelectorByLabel) {
	 		listener.exitCreateSelectorByLabel(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateSelectorByLabel) {
			return visitor.visitCreateSelectorByLabel(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateSelectorByTextContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public selectorByText(): SelectorByTextContext {
		return this.getTypedRuleContext(SelectorByTextContext, 0) as SelectorByTextContext;
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createSelectorByText;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateSelectorByText) {
	 		listener.enterCreateSelectorByText(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateSelectorByText) {
	 		listener.exitCreateSelectorByText(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateSelectorByText) {
			return visitor.visitCreateSelectorByText(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateSelectorByRegexContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public selectorByRegex(): SelectorByRegexContext {
		return this.getTypedRuleContext(SelectorByRegexContext, 0) as SelectorByRegexContext;
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createSelectorByRegex;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateSelectorByRegex) {
	 		listener.enterCreateSelectorByRegex(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateSelectorByRegex) {
	 		listener.exitCreateSelectorByRegex(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateSelectorByRegex) {
			return visitor.visitCreateSelectorByRegex(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateOperationContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public operation(): OperationContext {
		return this.getTypedRuleContext(OperationContext, 0) as OperationContext;
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createOperation;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateOperation) {
	 		listener.enterCreateOperation(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateOperation) {
	 		listener.exitCreateOperation(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateOperation) {
			return visitor.visitCreateOperation(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public selectorByLabel(): SelectorByLabelContext {
		return this.getTypedRuleContext(SelectorByLabelContext, 0) as SelectorByLabelContext;
	}
	public selectorByText(): SelectorByTextContext {
		return this.getTypedRuleContext(SelectorByTextContext, 0) as SelectorByTextContext;
	}
	public selectorByRegex(): SelectorByRegexContext {
		return this.getTypedRuleContext(SelectorByRegexContext, 0) as SelectorByRegexContext;
	}
	public selectorByPosition(): SelectorByPositionContext {
		return this.getTypedRuleContext(SelectorByPositionContext, 0) as SelectorByPositionContext;
	}
	public selectorByImage(): SelectorByImageContext {
		return this.getTypedRuleContext(SelectorByImageContext, 0) as SelectorByImageContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelector) {
	 		listener.enterSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelector) {
	 		listener.exitSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelector) {
			return visitor.visitSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorByLabelContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public LABEL(): TerminalNode {
		return this.getToken(GrammarParser.LABEL, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public selectorOrder(): SelectorOrderContext {
		return this.getTypedRuleContext(SelectorOrderContext, 0) as SelectorOrderContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selectorByLabel;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelectorByLabel) {
	 		listener.enterSelectorByLabel(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelectorByLabel) {
	 		listener.exitSelectorByLabel(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelectorByLabel) {
			return visitor.visitSelectorByLabel(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorByTextContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public TEXT(): TerminalNode {
		return this.getToken(GrammarParser.TEXT, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public selectorOrder(): SelectorOrderContext {
		return this.getTypedRuleContext(SelectorOrderContext, 0) as SelectorOrderContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selectorByText;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelectorByText) {
	 		listener.enterSelectorByText(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelectorByText) {
	 		listener.exitSelectorByText(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelectorByText) {
			return visitor.visitSelectorByText(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorByRegexContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public REGEX(): TerminalNode {
		return this.getToken(GrammarParser.REGEX, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public selectorOrder(): SelectorOrderContext {
		return this.getTypedRuleContext(SelectorOrderContext, 0) as SelectorOrderContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selectorByRegex;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelectorByRegex) {
	 		listener.enterSelectorByRegex(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelectorByRegex) {
	 		listener.exitSelectorByRegex(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelectorByRegex) {
			return visitor.visitSelectorByRegex(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorByPositionContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public POSITION(): TerminalNode {
		return this.getToken(GrammarParser.POSITION, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public number__list(): NumberContext[] {
		return this.getTypedRuleContexts(NumberContext) as NumberContext[];
	}
	public number_(i: number): NumberContext {
		return this.getTypedRuleContext(NumberContext, i) as NumberContext;
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selectorByPosition;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelectorByPosition) {
	 		listener.enterSelectorByPosition(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelectorByPosition) {
	 		listener.exitSelectorByPosition(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelectorByPosition) {
			return visitor.visitSelectorByPosition(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorByImageContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public IMAGE(): TerminalNode {
		return this.getToken(GrammarParser.IMAGE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public COMMA_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.COMMA);
	}
	public COMMA(i: number): TerminalNode {
		return this.getToken(GrammarParser.COMMA, i);
	}
	public FLOAT(): TerminalNode {
		return this.getToken(GrammarParser.FLOAT, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public selectorOrder(): SelectorOrderContext {
		return this.getTypedRuleContext(SelectorOrderContext, 0) as SelectorOrderContext;
	}
	public GRAY(): TerminalNode {
		return this.getToken(GrammarParser.GRAY, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selectorByImage;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelectorByImage) {
	 		listener.enterSelectorByImage(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelectorByImage) {
	 		listener.exitSelectorByImage(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelectorByImage) {
			return visitor.visitSelectorByImage(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SelectorOrderContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public INT_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.INT);
	}
	public INT(i: number): TerminalNode {
		return this.getToken(GrammarParser.INT, i);
	}
	public COMMA_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.COMMA);
	}
	public COMMA(i: number): TerminalNode {
		return this.getToken(GrammarParser.COMMA, i);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_selectorOrder;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterSelectorOrder) {
	 		listener.enterSelectorOrder(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitSelectorOrder) {
	 		listener.exitSelectorOrder(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitSelectorOrder) {
			return visitor.visitSelectorOrder(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CreateSequenceContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public EQ(): TerminalNode {
		return this.getToken(GrammarParser.EQ, 0);
	}
	public SEQUENCE(): TerminalNode {
		return this.getToken(GrammarParser.SEQUENCE, 0);
	}
	public OCPAR(): TerminalNode {
		return this.getToken(GrammarParser.OCPAR, 0);
	}
	public CCPAR(): TerminalNode {
		return this.getToken(GrammarParser.CCPAR, 0);
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
	public stmt_list(): StmtContext[] {
		return this.getTypedRuleContexts(StmtContext) as StmtContext[];
	}
	public stmt(i: number): StmtContext {
		return this.getTypedRuleContext(StmtContext, i) as StmtContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_createSequence;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterCreateSequence) {
	 		listener.enterCreateSequence(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitCreateSequence) {
	 		listener.exitCreateSequence(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitCreateSequence) {
			return visitor.visitCreateSequence(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class RunOperationContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public operation(): OperationContext {
		return this.getTypedRuleContext(OperationContext, 0) as OperationContext;
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_runOperation;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterRunOperation) {
	 		listener.enterRunOperation(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitRunOperation) {
	 		listener.exitRunOperation(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitRunOperation) {
			return visitor.visitRunOperation(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class OperationContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public wait(): WaitContext {
		return this.getTypedRuleContext(WaitContext, 0) as WaitContext;
	}
	public waitSelector(): WaitSelectorContext {
		return this.getTypedRuleContext(WaitSelectorContext, 0) as WaitSelectorContext;
	}
	public useDetector(): UseDetectorContext {
		return this.getTypedRuleContext(UseDetectorContext, 0) as UseDetectorContext;
	}
	public createAndUseDetector(): CreateAndUseDetectorContext {
		return this.getTypedRuleContext(CreateAndUseDetectorContext, 0) as CreateAndUseDetectorContext;
	}
	public mousePress(): MousePressContext {
		return this.getTypedRuleContext(MousePressContext, 0) as MousePressContext;
	}
	public mousePressSelector(): MousePressSelectorContext {
		return this.getTypedRuleContext(MousePressSelectorContext, 0) as MousePressSelectorContext;
	}
	public mouseReleaseSelector(): MouseReleaseSelectorContext {
		return this.getTypedRuleContext(MouseReleaseSelectorContext, 0) as MouseReleaseSelectorContext;
	}
	public mouseClick(): MouseClickContext {
		return this.getTypedRuleContext(MouseClickContext, 0) as MouseClickContext;
	}
	public mouseClickSelector(): MouseClickSelectorContext {
		return this.getTypedRuleContext(MouseClickSelectorContext, 0) as MouseClickSelectorContext;
	}
	public mouseDoubleClick(): MouseDoubleClickContext {
		return this.getTypedRuleContext(MouseDoubleClickContext, 0) as MouseDoubleClickContext;
	}
	public mouseDoubleClickSelector(): MouseDoubleClickSelectorContext {
		return this.getTypedRuleContext(MouseDoubleClickSelectorContext, 0) as MouseDoubleClickSelectorContext;
	}
	public mouseRelease(): MouseReleaseContext {
		return this.getTypedRuleContext(MouseReleaseContext, 0) as MouseReleaseContext;
	}
	public mouseScroll(): MouseScrollContext {
		return this.getTypedRuleContext(MouseScrollContext, 0) as MouseScrollContext;
	}
	public mouseScrollSelector(): MouseScrollSelectorContext {
		return this.getTypedRuleContext(MouseScrollSelectorContext, 0) as MouseScrollSelectorContext;
	}
	public keyPress(): KeyPressContext {
		return this.getTypedRuleContext(KeyPressContext, 0) as KeyPressContext;
	}
	public keyRelease(): KeyReleaseContext {
		return this.getTypedRuleContext(KeyReleaseContext, 0) as KeyReleaseContext;
	}
	public keyType(): KeyTypeContext {
		return this.getTypedRuleContext(KeyTypeContext, 0) as KeyTypeContext;
	}
	public keyCombo(): KeyComboContext {
		return this.getTypedRuleContext(KeyComboContext, 0) as KeyComboContext;
	}
	public keyComboSelector(): KeyComboSelectorContext {
		return this.getTypedRuleContext(KeyComboSelectorContext, 0) as KeyComboSelectorContext;
	}
	public keyPressSelector(): KeyPressSelectorContext {
		return this.getTypedRuleContext(KeyPressSelectorContext, 0) as KeyPressSelectorContext;
	}
	public keyReleaseSelector(): KeyReleaseSelectorContext {
		return this.getTypedRuleContext(KeyReleaseSelectorContext, 0) as KeyReleaseSelectorContext;
	}
	public keyTypeSelector(): KeyTypeSelectorContext {
		return this.getTypedRuleContext(KeyTypeSelectorContext, 0) as KeyTypeSelectorContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_operation;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterOperation) {
	 		listener.enterOperation(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitOperation) {
	 		listener.exitOperation(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitOperation) {
			return visitor.visitOperation(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class WaitContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WAIT(): TerminalNode {
		return this.getToken(GrammarParser.WAIT, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public INT(): TerminalNode {
		return this.getToken(GrammarParser.INT, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_wait;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterWait) {
	 		listener.enterWait(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitWait) {
	 		listener.exitWait(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitWait) {
			return visitor.visitWait(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class WaitSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WAIT(): TerminalNode {
		return this.getToken(GrammarParser.WAIT, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public INT(): TerminalNode {
		return this.getToken(GrammarParser.INT, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_waitSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterWaitSelector) {
	 		listener.enterWaitSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitWaitSelector) {
	 		listener.exitWaitSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitWaitSelector) {
			return visitor.visitWaitSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MousePressContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_PRESS(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_PRESS, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mousePress;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMousePress) {
	 		listener.enterMousePress(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMousePress) {
	 		listener.exitMousePress(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMousePress) {
			return visitor.visitMousePress(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MousePressSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_PRESS(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_PRESS, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mousePressSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMousePressSelector) {
	 		listener.enterMousePressSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMousePressSelector) {
	 		listener.exitMousePressSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMousePressSelector) {
			return visitor.visitMousePressSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseClickContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_CLICK(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_CLICK, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseClick;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseClick) {
	 		listener.enterMouseClick(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseClick) {
	 		listener.exitMouseClick(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseClick) {
			return visitor.visitMouseClick(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseClickSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_CLICK(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_CLICK, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseClickSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseClickSelector) {
	 		listener.enterMouseClickSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseClickSelector) {
	 		listener.exitMouseClickSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseClickSelector) {
			return visitor.visitMouseClickSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseDoubleClickContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_DOUBLE_CLICK(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_DOUBLE_CLICK, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseDoubleClick;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseDoubleClick) {
	 		listener.enterMouseDoubleClick(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseDoubleClick) {
	 		listener.exitMouseDoubleClick(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseDoubleClick) {
			return visitor.visitMouseDoubleClick(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseDoubleClickSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_DOUBLE_CLICK(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_DOUBLE_CLICK, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseDoubleClickSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseDoubleClickSelector) {
	 		listener.enterMouseDoubleClickSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseDoubleClickSelector) {
	 		listener.exitMouseDoubleClickSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseDoubleClickSelector) {
			return visitor.visitMouseDoubleClickSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseReleaseContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_RELEASE(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_RELEASE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseRelease;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseRelease) {
	 		listener.enterMouseRelease(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseRelease) {
	 		listener.exitMouseRelease(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseRelease) {
			return visitor.visitMouseRelease(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseReleaseSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_RELEASE(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_RELEASE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public mouseButton(): MouseButtonContext {
		return this.getTypedRuleContext(MouseButtonContext, 0) as MouseButtonContext;
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseReleaseSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseReleaseSelector) {
	 		listener.enterMouseReleaseSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseReleaseSelector) {
	 		listener.exitMouseReleaseSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseReleaseSelector) {
			return visitor.visitMouseReleaseSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseScrollContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_SCROLL(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_SCROLL, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public COMMA_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.COMMA);
	}
	public COMMA(i: number): TerminalNode {
		return this.getToken(GrammarParser.COMMA, i);
	}
	public INT_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.INT);
	}
	public INT(i: number): TerminalNode {
		return this.getToken(GrammarParser.INT, i);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseScroll;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseScroll) {
	 		listener.enterMouseScroll(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseScroll) {
	 		listener.exitMouseScroll(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseScroll) {
			return visitor.visitMouseScroll(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseScrollSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public MOUSE_SCROLL(): TerminalNode {
		return this.getToken(GrammarParser.MOUSE_SCROLL, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public COMMA_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.COMMA);
	}
	public COMMA(i: number): TerminalNode {
		return this.getToken(GrammarParser.COMMA, i);
	}
	public INT_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.INT);
	}
	public INT(i: number): TerminalNode {
		return this.getToken(GrammarParser.INT, i);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseScrollSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseScrollSelector) {
	 		listener.enterMouseScrollSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseScrollSelector) {
	 		listener.exitMouseScrollSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseScrollSelector) {
			return visitor.visitMouseScrollSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyComboContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_COMBO(): TerminalNode {
		return this.getToken(GrammarParser.KEY_COMBO, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public STRING_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.STRING);
	}
	public STRING(i: number): TerminalNode {
		return this.getToken(GrammarParser.STRING, i);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.COMMA);
	}
	public COMMA(i: number): TerminalNode {
		return this.getToken(GrammarParser.COMMA, i);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyCombo;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyCombo) {
	 		listener.enterKeyCombo(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyCombo) {
	 		listener.exitKeyCombo(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyCombo) {
			return visitor.visitKeyCombo(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyComboSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_COMBO(): TerminalNode {
		return this.getToken(GrammarParser.KEY_COMBO, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public STRING_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.STRING);
	}
	public STRING(i: number): TerminalNode {
		return this.getToken(GrammarParser.STRING, i);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
	public COMMA_list(): TerminalNode[] {
	    	return this.getTokens(GrammarParser.COMMA);
	}
	public COMMA(i: number): TerminalNode {
		return this.getToken(GrammarParser.COMMA, i);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyComboSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyComboSelector) {
	 		listener.enterKeyComboSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyComboSelector) {
	 		listener.exitKeyComboSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyComboSelector) {
			return visitor.visitKeyComboSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyPressContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_PRESS(): TerminalNode {
		return this.getToken(GrammarParser.KEY_PRESS, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyPress;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyPress) {
	 		listener.enterKeyPress(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyPress) {
	 		listener.exitKeyPress(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyPress) {
			return visitor.visitKeyPress(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyReleaseContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_RELEASE(): TerminalNode {
		return this.getToken(GrammarParser.KEY_RELEASE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyRelease;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyRelease) {
	 		listener.enterKeyRelease(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyRelease) {
	 		listener.exitKeyRelease(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyRelease) {
			return visitor.visitKeyRelease(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyTypeContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_TYPE(): TerminalNode {
		return this.getToken(GrammarParser.KEY_TYPE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyType;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyType) {
	 		listener.enterKeyType(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyType) {
	 		listener.exitKeyType(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyType) {
			return visitor.visitKeyType(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyPressSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_PRESS(): TerminalNode {
		return this.getToken(GrammarParser.KEY_PRESS, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyPressSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyPressSelector) {
	 		listener.enterKeyPressSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyPressSelector) {
	 		listener.exitKeyPressSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyPressSelector) {
			return visitor.visitKeyPressSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyReleaseSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_RELEASE(): TerminalNode {
		return this.getToken(GrammarParser.KEY_RELEASE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyReleaseSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyReleaseSelector) {
	 		listener.enterKeyReleaseSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyReleaseSelector) {
	 		listener.exitKeyReleaseSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyReleaseSelector) {
			return visitor.visitKeyReleaseSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class KeyTypeSelectorContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public KEY_TYPE(): TerminalNode {
		return this.getToken(GrammarParser.KEY_TYPE, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public selector(): SelectorContext {
		return this.getTypedRuleContext(SelectorContext, 0) as SelectorContext;
	}
	public COMMA(): TerminalNode {
		return this.getToken(GrammarParser.COMMA, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(GrammarParser.STRING, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_keyTypeSelector;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterKeyTypeSelector) {
	 		listener.enterKeyTypeSelector(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitKeyTypeSelector) {
	 		listener.exitKeyTypeSelector(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitKeyTypeSelector) {
			return visitor.visitKeyTypeSelector(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MouseButtonContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public LEFT(): TerminalNode {
		return this.getToken(GrammarParser.LEFT, 0);
	}
	public MIDDLE(): TerminalNode {
		return this.getToken(GrammarParser.MIDDLE, 0);
	}
	public RIGHT(): TerminalNode {
		return this.getToken(GrammarParser.RIGHT, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_mouseButton;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterMouseButton) {
	 		listener.enterMouseButton(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitMouseButton) {
	 		listener.exitMouseButton(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitMouseButton) {
			return visitor.visitMouseButton(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class NumberContext extends ParserRuleContext {
	constructor(parser?: GrammarParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public INT(): TerminalNode {
		return this.getToken(GrammarParser.INT, 0);
	}
	public FLOAT(): TerminalNode {
		return this.getToken(GrammarParser.FLOAT, 0);
	}
    public get ruleIndex(): number {
    	return GrammarParser.RULE_number;
	}
	public enterRule(listener: GrammarListener): void {
	    if(listener.enterNumber) {
	 		listener.enterNumber(this);
		}
	}
	public exitRule(listener: GrammarListener): void {
	    if(listener.exitNumber) {
	 		listener.exitNumber(this);
		}
	}
	// @Override
	public accept<Result>(visitor: GrammarVisitor<Result>): Result {
		if (visitor.visitNumber) {
			return visitor.visitNumber(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}
