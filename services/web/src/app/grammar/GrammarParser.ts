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
	public static readonly LEFT = 1;
	public static readonly RIGHT = 2;
	public static readonly MIDDLE = 3;
	public static readonly KEY_PRESS = 4;
	public static readonly KEY_TYPE = 5;
	public static readonly KEY_RELEASE = 6;
	public static readonly MOUSE_CLICK = 7;
	public static readonly MOUSE_DOUBLE_CLICK = 8;
	public static readonly MOUSE_PRESS = 9;
	public static readonly MOUSE_RELEASE = 10;
	public static readonly MOUSE_SCROLL = 11;
	public static readonly WAIT = 12;
	public static readonly TEXT = 13;
	public static readonly POSITION = 14;
	public static readonly REGEX = 15;
	public static readonly COMMA = 16;
	public static readonly DCOMMA = 17;
	public static readonly LABEL = 18;
	public static readonly USE = 19;
	public static readonly SEQUENCE = 20;
	public static readonly DETECTOR = 21;
	public static readonly ID = 22;
	public static readonly STRING = 23;
	public static readonly ESC = 24;
	public static readonly ORPAR = 25;
	public static readonly EQ = 26;
	public static readonly CRPAR = 27;
	public static readonly OCPAR = 28;
	public static readonly CCPAR = 29;
	public static readonly INT = 30;
	public static readonly FLOAT = 31;
	public static readonly WS = 32;
	public static override readonly EOF = Token.EOF;
	public static readonly RULE_root = 0;
	public static readonly RULE_stmt = 1;
	public static readonly RULE_createDetector = 2;
	public static readonly RULE_useDetector = 3;
	public static readonly RULE_createSelectorByPosition = 4;
	public static readonly RULE_createSelectorByLabel = 5;
	public static readonly RULE_createSelectorByText = 6;
	public static readonly RULE_createSelectorByRegex = 7;
	public static readonly RULE_createOperation = 8;
	public static readonly RULE_selector = 9;
	public static readonly RULE_selectorByLabel = 10;
	public static readonly RULE_selectorByText = 11;
	public static readonly RULE_selectorByRegex = 12;
	public static readonly RULE_selectorByPosition = 13;
	public static readonly RULE_selectorOrder = 14;
	public static readonly RULE_createSequence = 15;
	public static readonly RULE_runOperation = 16;
	public static readonly RULE_operation = 17;
	public static readonly RULE_wait = 18;
	public static readonly RULE_waitSelector = 19;
	public static readonly RULE_mousePress = 20;
	public static readonly RULE_mousePressSelector = 21;
	public static readonly RULE_mouseClick = 22;
	public static readonly RULE_mouseClickSelector = 23;
	public static readonly RULE_mouseDoubleClick = 24;
	public static readonly RULE_mouseDoubleClickSelector = 25;
	public static readonly RULE_mouseRelease = 26;
	public static readonly RULE_mouseReleaseSelector = 27;
	public static readonly RULE_mouseScroll = 28;
	public static readonly RULE_mouseScrollSelector = 29;
	public static readonly RULE_keyPress = 30;
	public static readonly RULE_keyRelease = 31;
	public static readonly RULE_keyType = 32;
	public static readonly RULE_keyPressSelector = 33;
	public static readonly RULE_keyReleaseSelector = 34;
	public static readonly RULE_keyTypeSelector = 35;
	public static readonly RULE_mouseButton = 36;
	public static readonly RULE_number = 37;
	public static readonly literalNames: (string | null)[] = [ null, "'left'", 
                                                            "'right'", "'middle'", 
                                                            "'keyPress'", 
                                                            "'keyType'", 
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
	public static readonly symbolicNames: (string | null)[] = [ null, "LEFT", 
                                                             "RIGHT", "MIDDLE", 
                                                             "KEY_PRESS", 
                                                             "KEY_TYPE", 
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
                                                             "WS" ];
	// tslint:disable:no-trailing-whitespace
	public static readonly ruleNames: string[] = [
		"root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
		"createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
		"createOperation", "selector", "selectorByLabel", "selectorByText", "selectorByRegex", 
		"selectorByPosition", "selectorOrder", "createSequence", "runOperation", 
		"operation", "wait", "waitSelector", "mousePress", "mousePressSelector", 
		"mouseClick", "mouseClickSelector", "mouseDoubleClick", "mouseDoubleClickSelector", 
		"mouseRelease", "mouseReleaseSelector", "mouseScroll", "mouseScrollSelector", 
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
			this.state = 79;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while ((((_la) & ~0x1F) === 0 && ((1 << _la) & 4726768) !== 0)) {
				{
				{
				this.state = 76;
				this.stmt();
				}
				}
				this.state = 81;
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
			this.state = 91;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 1, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 82;
				this.createDetector();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 83;
				this.useDetector();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 84;
				this.createSelectorByLabel();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 85;
				this.createSelectorByText();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 86;
				this.createSelectorByRegex();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 87;
				this.createSelectorByPosition();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 88;
				this.createOperation();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 89;
				this.createSequence();
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 90;
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
			this.state = 93;
			this.match(GrammarParser.ID);
			this.state = 94;
			this.match(GrammarParser.EQ);
			this.state = 95;
			this.match(GrammarParser.DETECTOR);
			this.state = 96;
			this.match(GrammarParser.ORPAR);
			this.state = 97;
			this.match(GrammarParser.STRING);
			this.state = 98;
			this.match(GrammarParser.CRPAR);
			this.state = 99;
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
			this.state = 101;
			this.match(GrammarParser.USE);
			this.state = 102;
			this.match(GrammarParser.ID);
			this.state = 106;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===25) {
				{
				this.state = 103;
				this.match(GrammarParser.ORPAR);
				this.state = 104;
				this.match(GrammarParser.FLOAT);
				this.state = 105;
				this.match(GrammarParser.CRPAR);
				}
			}

			this.state = 108;
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
	public createSelectorByPosition(): CreateSelectorByPositionContext {
		let localctx: CreateSelectorByPositionContext = new CreateSelectorByPositionContext(this, this._ctx, this.state);
		this.enterRule(localctx, 8, GrammarParser.RULE_createSelectorByPosition);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 110;
			this.match(GrammarParser.ID);
			this.state = 111;
			this.match(GrammarParser.EQ);
			this.state = 112;
			this.selectorByPosition();
			this.state = 113;
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
		this.enterRule(localctx, 10, GrammarParser.RULE_createSelectorByLabel);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 115;
			this.match(GrammarParser.ID);
			this.state = 116;
			this.match(GrammarParser.EQ);
			this.state = 117;
			this.selectorByLabel();
			this.state = 118;
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
		this.enterRule(localctx, 12, GrammarParser.RULE_createSelectorByText);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 120;
			this.match(GrammarParser.ID);
			this.state = 121;
			this.match(GrammarParser.EQ);
			this.state = 122;
			this.selectorByText();
			this.state = 123;
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
		this.enterRule(localctx, 14, GrammarParser.RULE_createSelectorByRegex);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 125;
			this.match(GrammarParser.ID);
			this.state = 126;
			this.match(GrammarParser.EQ);
			this.state = 127;
			this.selectorByRegex();
			this.state = 128;
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
		this.enterRule(localctx, 16, GrammarParser.RULE_createOperation);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 130;
			this.match(GrammarParser.ID);
			this.state = 131;
			this.match(GrammarParser.EQ);
			this.state = 132;
			this.operation();
			this.state = 133;
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
		this.enterRule(localctx, 18, GrammarParser.RULE_selector);
		try {
			this.state = 139;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 18:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 135;
				this.selectorByLabel();
				}
				break;
			case 13:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 136;
				this.selectorByText();
				}
				break;
			case 15:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 137;
				this.selectorByRegex();
				}
				break;
			case 14:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 138;
				this.selectorByPosition();
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
		this.enterRule(localctx, 20, GrammarParser.RULE_selectorByLabel);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 141;
			this.match(GrammarParser.LABEL);
			this.state = 142;
			this.match(GrammarParser.ORPAR);
			this.state = 143;
			this.match(GrammarParser.STRING);
			this.state = 146;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 144;
				this.match(GrammarParser.COMMA);
				this.state = 145;
				this.selectorOrder();
				}
			}

			this.state = 148;
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
		this.enterRule(localctx, 22, GrammarParser.RULE_selectorByText);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 150;
			this.match(GrammarParser.TEXT);
			this.state = 151;
			this.match(GrammarParser.ORPAR);
			this.state = 152;
			this.match(GrammarParser.STRING);
			this.state = 155;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 153;
				this.match(GrammarParser.COMMA);
				this.state = 154;
				this.selectorOrder();
				}
			}

			this.state = 157;
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
		this.enterRule(localctx, 24, GrammarParser.RULE_selectorByRegex);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 159;
			this.match(GrammarParser.REGEX);
			this.state = 160;
			this.match(GrammarParser.ORPAR);
			this.state = 161;
			this.match(GrammarParser.STRING);
			this.state = 164;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 162;
				this.match(GrammarParser.COMMA);
				this.state = 163;
				this.selectorOrder();
				}
			}

			this.state = 166;
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
		this.enterRule(localctx, 26, GrammarParser.RULE_selectorByPosition);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 168;
			this.match(GrammarParser.POSITION);
			this.state = 169;
			this.match(GrammarParser.ORPAR);
			this.state = 170;
			this.number_();
			this.state = 171;
			this.match(GrammarParser.COMMA);
			this.state = 172;
			this.number_();
			this.state = 173;
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
		this.enterRule(localctx, 28, GrammarParser.RULE_selectorOrder);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 175;
			this.match(GrammarParser.INT);
			this.state = 180;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while (_la===16) {
				{
				{
				this.state = 176;
				this.match(GrammarParser.COMMA);
				this.state = 177;
				this.match(GrammarParser.INT);
				}
				}
				this.state = 182;
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
	public createSequence(): CreateSequenceContext {
		let localctx: CreateSequenceContext = new CreateSequenceContext(this, this._ctx, this.state);
		this.enterRule(localctx, 30, GrammarParser.RULE_createSequence);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 183;
			this.match(GrammarParser.ID);
			this.state = 184;
			this.match(GrammarParser.EQ);
			this.state = 185;
			this.match(GrammarParser.SEQUENCE);
			this.state = 186;
			this.match(GrammarParser.OCPAR);
			this.state = 190;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while ((((_la) & ~0x1F) === 0 && ((1 << _la) & 4726768) !== 0)) {
				{
				{
				this.state = 187;
				this.stmt();
				}
				}
				this.state = 192;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			this.state = 193;
			this.match(GrammarParser.CCPAR);
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
		this.enterRule(localctx, 32, GrammarParser.RULE_runOperation);
		try {
			this.state = 200;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 4:
			case 5:
			case 6:
			case 7:
			case 8:
			case 9:
			case 10:
			case 11:
			case 12:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 195;
				this.operation();
				this.state = 196;
				this.match(GrammarParser.DCOMMA);
				}
				break;
			case 22:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 198;
				this.match(GrammarParser.ID);
				this.state = 199;
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
		this.enterRule(localctx, 34, GrammarParser.RULE_operation);
		try {
			this.state = 220;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 10, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 202;
				this.wait();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 203;
				this.waitSelector();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 204;
				this.mousePress();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 205;
				this.mousePressSelector();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 206;
				this.mouseReleaseSelector();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 207;
				this.mouseClick();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 208;
				this.mouseClickSelector();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 209;
				this.mouseDoubleClick();
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 210;
				this.mouseDoubleClickSelector();
				}
				break;
			case 10:
				this.enterOuterAlt(localctx, 10);
				{
				this.state = 211;
				this.mouseRelease();
				}
				break;
			case 11:
				this.enterOuterAlt(localctx, 11);
				{
				this.state = 212;
				this.mouseScroll();
				}
				break;
			case 12:
				this.enterOuterAlt(localctx, 12);
				{
				this.state = 213;
				this.mouseScrollSelector();
				}
				break;
			case 13:
				this.enterOuterAlt(localctx, 13);
				{
				this.state = 214;
				this.keyPress();
				}
				break;
			case 14:
				this.enterOuterAlt(localctx, 14);
				{
				this.state = 215;
				this.keyRelease();
				}
				break;
			case 15:
				this.enterOuterAlt(localctx, 15);
				{
				this.state = 216;
				this.keyType();
				}
				break;
			case 16:
				this.enterOuterAlt(localctx, 16);
				{
				this.state = 217;
				this.keyPressSelector();
				}
				break;
			case 17:
				this.enterOuterAlt(localctx, 17);
				{
				this.state = 218;
				this.keyReleaseSelector();
				}
				break;
			case 18:
				this.enterOuterAlt(localctx, 18);
				{
				this.state = 219;
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
		this.enterRule(localctx, 36, GrammarParser.RULE_wait);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 222;
			this.match(GrammarParser.WAIT);
			this.state = 223;
			this.match(GrammarParser.ORPAR);
			this.state = 224;
			this.match(GrammarParser.ID);
			this.state = 227;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 225;
				this.match(GrammarParser.COMMA);
				this.state = 226;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 229;
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
		this.enterRule(localctx, 38, GrammarParser.RULE_waitSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 231;
			this.match(GrammarParser.WAIT);
			this.state = 232;
			this.match(GrammarParser.ORPAR);
			this.state = 233;
			this.selector();
			this.state = 236;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 234;
				this.match(GrammarParser.COMMA);
				this.state = 235;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 238;
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
		this.enterRule(localctx, 40, GrammarParser.RULE_mousePress);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 240;
			this.match(GrammarParser.MOUSE_PRESS);
			this.state = 241;
			this.match(GrammarParser.ORPAR);
			this.state = 242;
			this.match(GrammarParser.ID);
			this.state = 245;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 243;
				this.match(GrammarParser.COMMA);
				this.state = 244;
				this.mouseButton();
				}
			}

			this.state = 247;
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
		this.enterRule(localctx, 42, GrammarParser.RULE_mousePressSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 249;
			this.match(GrammarParser.MOUSE_PRESS);
			this.state = 250;
			this.match(GrammarParser.ORPAR);
			this.state = 251;
			this.selector();
			this.state = 254;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 252;
				this.match(GrammarParser.COMMA);
				this.state = 253;
				this.mouseButton();
				}
			}

			this.state = 256;
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
		this.enterRule(localctx, 44, GrammarParser.RULE_mouseClick);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 258;
			this.match(GrammarParser.MOUSE_CLICK);
			this.state = 259;
			this.match(GrammarParser.ORPAR);
			this.state = 260;
			this.match(GrammarParser.ID);
			this.state = 263;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 261;
				this.match(GrammarParser.COMMA);
				this.state = 262;
				this.mouseButton();
				}
			}

			this.state = 265;
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
		this.enterRule(localctx, 46, GrammarParser.RULE_mouseClickSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 267;
			this.match(GrammarParser.MOUSE_CLICK);
			this.state = 268;
			this.match(GrammarParser.ORPAR);
			this.state = 269;
			this.selector();
			this.state = 272;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 270;
				this.match(GrammarParser.COMMA);
				this.state = 271;
				this.mouseButton();
				}
			}

			this.state = 274;
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
		this.enterRule(localctx, 48, GrammarParser.RULE_mouseDoubleClick);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 276;
			this.match(GrammarParser.MOUSE_DOUBLE_CLICK);
			this.state = 277;
			this.match(GrammarParser.ORPAR);
			this.state = 278;
			this.match(GrammarParser.ID);
			this.state = 281;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 279;
				this.match(GrammarParser.COMMA);
				this.state = 280;
				this.mouseButton();
				}
			}

			this.state = 283;
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
		this.enterRule(localctx, 50, GrammarParser.RULE_mouseDoubleClickSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 285;
			this.match(GrammarParser.MOUSE_DOUBLE_CLICK);
			this.state = 286;
			this.match(GrammarParser.ORPAR);
			this.state = 287;
			this.selector();
			this.state = 290;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 288;
				this.match(GrammarParser.COMMA);
				this.state = 289;
				this.mouseButton();
				}
			}

			this.state = 292;
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
		this.enterRule(localctx, 52, GrammarParser.RULE_mouseRelease);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 294;
			this.match(GrammarParser.MOUSE_RELEASE);
			this.state = 295;
			this.match(GrammarParser.ORPAR);
			this.state = 296;
			this.match(GrammarParser.ID);
			this.state = 299;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 297;
				this.match(GrammarParser.COMMA);
				this.state = 298;
				this.mouseButton();
				}
			}

			this.state = 301;
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
		this.enterRule(localctx, 54, GrammarParser.RULE_mouseReleaseSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 303;
			this.match(GrammarParser.MOUSE_RELEASE);
			this.state = 304;
			this.match(GrammarParser.ORPAR);
			this.state = 305;
			this.selector();
			this.state = 308;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 306;
				this.match(GrammarParser.COMMA);
				this.state = 307;
				this.mouseButton();
				}
			}

			this.state = 310;
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
		this.enterRule(localctx, 56, GrammarParser.RULE_mouseScroll);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 312;
			this.match(GrammarParser.MOUSE_SCROLL);
			this.state = 313;
			this.match(GrammarParser.ORPAR);
			this.state = 314;
			this.match(GrammarParser.ID);
			this.state = 315;
			this.match(GrammarParser.COMMA);
			this.state = 316;
			this.match(GrammarParser.INT);
			this.state = 319;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 317;
				this.match(GrammarParser.COMMA);
				this.state = 318;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 321;
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
		this.enterRule(localctx, 58, GrammarParser.RULE_mouseScrollSelector);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 323;
			this.match(GrammarParser.MOUSE_SCROLL);
			this.state = 324;
			this.match(GrammarParser.ORPAR);
			this.state = 325;
			this.selector();
			this.state = 326;
			this.match(GrammarParser.COMMA);
			this.state = 327;
			this.match(GrammarParser.INT);
			this.state = 330;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===16) {
				{
				this.state = 328;
				this.match(GrammarParser.COMMA);
				this.state = 329;
				this.match(GrammarParser.INT);
				}
			}

			this.state = 332;
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
		this.enterRule(localctx, 60, GrammarParser.RULE_keyPress);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 334;
			this.match(GrammarParser.KEY_PRESS);
			this.state = 335;
			this.match(GrammarParser.ORPAR);
			this.state = 336;
			this.match(GrammarParser.ID);
			this.state = 337;
			this.match(GrammarParser.COMMA);
			this.state = 338;
			this.match(GrammarParser.STRING);
			this.state = 339;
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
		this.enterRule(localctx, 62, GrammarParser.RULE_keyRelease);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 341;
			this.match(GrammarParser.KEY_RELEASE);
			this.state = 342;
			this.match(GrammarParser.ORPAR);
			this.state = 343;
			this.match(GrammarParser.ID);
			this.state = 344;
			this.match(GrammarParser.COMMA);
			this.state = 345;
			this.match(GrammarParser.STRING);
			this.state = 346;
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
		this.enterRule(localctx, 64, GrammarParser.RULE_keyType);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 348;
			this.match(GrammarParser.KEY_TYPE);
			this.state = 349;
			this.match(GrammarParser.ORPAR);
			this.state = 350;
			this.match(GrammarParser.ID);
			this.state = 351;
			this.match(GrammarParser.COMMA);
			this.state = 352;
			this.match(GrammarParser.STRING);
			this.state = 353;
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
		this.enterRule(localctx, 66, GrammarParser.RULE_keyPressSelector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 355;
			this.match(GrammarParser.KEY_PRESS);
			this.state = 356;
			this.match(GrammarParser.ORPAR);
			this.state = 357;
			this.selector();
			this.state = 358;
			this.match(GrammarParser.COMMA);
			this.state = 359;
			this.match(GrammarParser.STRING);
			this.state = 360;
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
		this.enterRule(localctx, 68, GrammarParser.RULE_keyReleaseSelector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 362;
			this.match(GrammarParser.KEY_RELEASE);
			this.state = 363;
			this.match(GrammarParser.ORPAR);
			this.state = 364;
			this.selector();
			this.state = 365;
			this.match(GrammarParser.COMMA);
			this.state = 366;
			this.match(GrammarParser.STRING);
			this.state = 367;
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
		this.enterRule(localctx, 70, GrammarParser.RULE_keyTypeSelector);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 369;
			this.match(GrammarParser.KEY_TYPE);
			this.state = 370;
			this.match(GrammarParser.ORPAR);
			this.state = 371;
			this.selector();
			this.state = 372;
			this.match(GrammarParser.COMMA);
			this.state = 373;
			this.match(GrammarParser.STRING);
			this.state = 374;
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
		this.enterRule(localctx, 72, GrammarParser.RULE_mouseButton);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 376;
			_la = this._input.LA(1);
			if(!((((_la) & ~0x1F) === 0 && ((1 << _la) & 14) !== 0))) {
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
		this.enterRule(localctx, 74, GrammarParser.RULE_number);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 378;
			_la = this._input.LA(1);
			if(!(_la===30 || _la===31)) {
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

	public static readonly _serializedATN: number[] = [4,1,32,381,2,0,7,0,2,
	1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,
	10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,
	7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,
	24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,
	2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,5,0,78,
	8,0,10,0,12,0,81,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,
	1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,107,8,3,1,3,1,3,1,4,
	1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
	1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,140,8,9,1,10,1,10,1,10,1,10,
	1,10,3,10,147,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,156,8,11,1,11,
	1,11,1,12,1,12,1,12,1,12,1,12,3,12,165,8,12,1,12,1,12,1,13,1,13,1,13,1,
	13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,179,8,14,10,14,12,14,182,9,14,1,15,
	1,15,1,15,1,15,1,15,5,15,189,8,15,10,15,12,15,192,9,15,1,15,1,15,1,16,1,
	16,1,16,1,16,1,16,3,16,201,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
	1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,221,8,17,1,18,1,
	18,1,18,1,18,1,18,3,18,228,8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,
	237,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,246,8,20,1,20,1,20,1,21,
	1,21,1,21,1,21,1,21,3,21,255,8,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,
	22,264,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,3,23,273,8,23,1,23,1,23,
	1,24,1,24,1,24,1,24,1,24,3,24,282,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,
	25,3,25,291,8,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,3,26,300,8,26,1,26,
	1,26,1,27,1,27,1,27,1,27,1,27,3,27,309,8,27,1,27,1,27,1,28,1,28,1,28,1,
	28,1,28,1,28,1,28,3,28,320,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
	1,29,3,29,331,8,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,
	31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,
	1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,
	35,1,35,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,37,0,0,38,0,2,4,6,8,10,12,
	14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
	62,64,66,68,70,72,74,0,2,1,0,1,3,1,0,30,31,390,0,79,1,0,0,0,2,91,1,0,0,
	0,4,93,1,0,0,0,6,101,1,0,0,0,8,110,1,0,0,0,10,115,1,0,0,0,12,120,1,0,0,
	0,14,125,1,0,0,0,16,130,1,0,0,0,18,139,1,0,0,0,20,141,1,0,0,0,22,150,1,
	0,0,0,24,159,1,0,0,0,26,168,1,0,0,0,28,175,1,0,0,0,30,183,1,0,0,0,32,200,
	1,0,0,0,34,220,1,0,0,0,36,222,1,0,0,0,38,231,1,0,0,0,40,240,1,0,0,0,42,
	249,1,0,0,0,44,258,1,0,0,0,46,267,1,0,0,0,48,276,1,0,0,0,50,285,1,0,0,0,
	52,294,1,0,0,0,54,303,1,0,0,0,56,312,1,0,0,0,58,323,1,0,0,0,60,334,1,0,
	0,0,62,341,1,0,0,0,64,348,1,0,0,0,66,355,1,0,0,0,68,362,1,0,0,0,70,369,
	1,0,0,0,72,376,1,0,0,0,74,378,1,0,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,81,
	1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,1,1,0,0,0,81,79,1,0,0,0,82,92,3,
	4,2,0,83,92,3,6,3,0,84,92,3,10,5,0,85,92,3,12,6,0,86,92,3,14,7,0,87,92,
	3,8,4,0,88,92,3,16,8,0,89,92,3,30,15,0,90,92,3,32,16,0,91,82,1,0,0,0,91,
	83,1,0,0,0,91,84,1,0,0,0,91,85,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,
	1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,3,1,0,0,0,93,94,5,22,0,0,94,95,5,
	26,0,0,95,96,5,21,0,0,96,97,5,25,0,0,97,98,5,23,0,0,98,99,5,27,0,0,99,100,
	5,17,0,0,100,5,1,0,0,0,101,102,5,19,0,0,102,106,5,22,0,0,103,104,5,25,0,
	0,104,105,5,31,0,0,105,107,5,27,0,0,106,103,1,0,0,0,106,107,1,0,0,0,107,
	108,1,0,0,0,108,109,5,17,0,0,109,7,1,0,0,0,110,111,5,22,0,0,111,112,5,26,
	0,0,112,113,3,26,13,0,113,114,5,17,0,0,114,9,1,0,0,0,115,116,5,22,0,0,116,
	117,5,26,0,0,117,118,3,20,10,0,118,119,5,17,0,0,119,11,1,0,0,0,120,121,
	5,22,0,0,121,122,5,26,0,0,122,123,3,22,11,0,123,124,5,17,0,0,124,13,1,0,
	0,0,125,126,5,22,0,0,126,127,5,26,0,0,127,128,3,24,12,0,128,129,5,17,0,
	0,129,15,1,0,0,0,130,131,5,22,0,0,131,132,5,26,0,0,132,133,3,34,17,0,133,
	134,5,17,0,0,134,17,1,0,0,0,135,140,3,20,10,0,136,140,3,22,11,0,137,140,
	3,24,12,0,138,140,3,26,13,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,0,
	0,0,139,138,1,0,0,0,140,19,1,0,0,0,141,142,5,18,0,0,142,143,5,25,0,0,143,
	146,5,23,0,0,144,145,5,16,0,0,145,147,3,28,14,0,146,144,1,0,0,0,146,147,
	1,0,0,0,147,148,1,0,0,0,148,149,5,27,0,0,149,21,1,0,0,0,150,151,5,13,0,
	0,151,152,5,25,0,0,152,155,5,23,0,0,153,154,5,16,0,0,154,156,3,28,14,0,
	155,153,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,27,0,0,158,23,
	1,0,0,0,159,160,5,15,0,0,160,161,5,25,0,0,161,164,5,23,0,0,162,163,5,16,
	0,0,163,165,3,28,14,0,164,162,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,
	167,5,27,0,0,167,25,1,0,0,0,168,169,5,14,0,0,169,170,5,25,0,0,170,171,3,
	74,37,0,171,172,5,16,0,0,172,173,3,74,37,0,173,174,5,27,0,0,174,27,1,0,
	0,0,175,180,5,30,0,0,176,177,5,16,0,0,177,179,5,30,0,0,178,176,1,0,0,0,
	179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,29,1,0,0,0,182,180,
	1,0,0,0,183,184,5,22,0,0,184,185,5,26,0,0,185,186,5,20,0,0,186,190,5,28,
	0,0,187,189,3,2,1,0,188,187,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,
	191,1,0,0,0,191,193,1,0,0,0,192,190,1,0,0,0,193,194,5,29,0,0,194,31,1,0,
	0,0,195,196,3,34,17,0,196,197,5,17,0,0,197,201,1,0,0,0,198,199,5,22,0,0,
	199,201,5,17,0,0,200,195,1,0,0,0,200,198,1,0,0,0,201,33,1,0,0,0,202,221,
	3,36,18,0,203,221,3,38,19,0,204,221,3,40,20,0,205,221,3,42,21,0,206,221,
	3,54,27,0,207,221,3,44,22,0,208,221,3,46,23,0,209,221,3,48,24,0,210,221,
	3,50,25,0,211,221,3,52,26,0,212,221,3,56,28,0,213,221,3,58,29,0,214,221,
	3,60,30,0,215,221,3,62,31,0,216,221,3,64,32,0,217,221,3,66,33,0,218,221,
	3,68,34,0,219,221,3,70,35,0,220,202,1,0,0,0,220,203,1,0,0,0,220,204,1,0,
	0,0,220,205,1,0,0,0,220,206,1,0,0,0,220,207,1,0,0,0,220,208,1,0,0,0,220,
	209,1,0,0,0,220,210,1,0,0,0,220,211,1,0,0,0,220,212,1,0,0,0,220,213,1,0,
	0,0,220,214,1,0,0,0,220,215,1,0,0,0,220,216,1,0,0,0,220,217,1,0,0,0,220,
	218,1,0,0,0,220,219,1,0,0,0,221,35,1,0,0,0,222,223,5,12,0,0,223,224,5,25,
	0,0,224,227,5,22,0,0,225,226,5,16,0,0,226,228,5,30,0,0,227,225,1,0,0,0,
	227,228,1,0,0,0,228,229,1,0,0,0,229,230,5,27,0,0,230,37,1,0,0,0,231,232,
	5,12,0,0,232,233,5,25,0,0,233,236,3,18,9,0,234,235,5,16,0,0,235,237,5,30,
	0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,238,1,0,0,0,238,239,5,27,0,0,239,
	39,1,0,0,0,240,241,5,9,0,0,241,242,5,25,0,0,242,245,5,22,0,0,243,244,5,
	16,0,0,244,246,3,72,36,0,245,243,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,
	0,247,248,5,27,0,0,248,41,1,0,0,0,249,250,5,9,0,0,250,251,5,25,0,0,251,
	254,3,18,9,0,252,253,5,16,0,0,253,255,3,72,36,0,254,252,1,0,0,0,254,255,
	1,0,0,0,255,256,1,0,0,0,256,257,5,27,0,0,257,43,1,0,0,0,258,259,5,7,0,0,
	259,260,5,25,0,0,260,263,5,22,0,0,261,262,5,16,0,0,262,264,3,72,36,0,263,
	261,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,27,0,0,266,45,1,0,
	0,0,267,268,5,7,0,0,268,269,5,25,0,0,269,272,3,18,9,0,270,271,5,16,0,0,
	271,273,3,72,36,0,272,270,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,275,
	5,27,0,0,275,47,1,0,0,0,276,277,5,8,0,0,277,278,5,25,0,0,278,281,5,22,0,
	0,279,280,5,16,0,0,280,282,3,72,36,0,281,279,1,0,0,0,281,282,1,0,0,0,282,
	283,1,0,0,0,283,284,5,27,0,0,284,49,1,0,0,0,285,286,5,8,0,0,286,287,5,25,
	0,0,287,290,3,18,9,0,288,289,5,16,0,0,289,291,3,72,36,0,290,288,1,0,0,0,
	290,291,1,0,0,0,291,292,1,0,0,0,292,293,5,27,0,0,293,51,1,0,0,0,294,295,
	5,10,0,0,295,296,5,25,0,0,296,299,5,22,0,0,297,298,5,16,0,0,298,300,3,72,
	36,0,299,297,1,0,0,0,299,300,1,0,0,0,300,301,1,0,0,0,301,302,5,27,0,0,302,
	53,1,0,0,0,303,304,5,10,0,0,304,305,5,25,0,0,305,308,3,18,9,0,306,307,5,
	16,0,0,307,309,3,72,36,0,308,306,1,0,0,0,308,309,1,0,0,0,309,310,1,0,0,
	0,310,311,5,27,0,0,311,55,1,0,0,0,312,313,5,11,0,0,313,314,5,25,0,0,314,
	315,5,22,0,0,315,316,5,16,0,0,316,319,5,30,0,0,317,318,5,16,0,0,318,320,
	5,30,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,321,1,0,0,0,321,322,5,27,0,
	0,322,57,1,0,0,0,323,324,5,11,0,0,324,325,5,25,0,0,325,326,3,18,9,0,326,
	327,5,16,0,0,327,330,5,30,0,0,328,329,5,16,0,0,329,331,5,30,0,0,330,328,
	1,0,0,0,330,331,1,0,0,0,331,332,1,0,0,0,332,333,5,27,0,0,333,59,1,0,0,0,
	334,335,5,4,0,0,335,336,5,25,0,0,336,337,5,22,0,0,337,338,5,16,0,0,338,
	339,5,23,0,0,339,340,5,27,0,0,340,61,1,0,0,0,341,342,5,6,0,0,342,343,5,
	25,0,0,343,344,5,22,0,0,344,345,5,16,0,0,345,346,5,23,0,0,346,347,5,27,
	0,0,347,63,1,0,0,0,348,349,5,5,0,0,349,350,5,25,0,0,350,351,5,22,0,0,351,
	352,5,16,0,0,352,353,5,23,0,0,353,354,5,27,0,0,354,65,1,0,0,0,355,356,5,
	4,0,0,356,357,5,25,0,0,357,358,3,18,9,0,358,359,5,16,0,0,359,360,5,23,0,
	0,360,361,5,27,0,0,361,67,1,0,0,0,362,363,5,6,0,0,363,364,5,25,0,0,364,
	365,3,18,9,0,365,366,5,16,0,0,366,367,5,23,0,0,367,368,5,27,0,0,368,69,
	1,0,0,0,369,370,5,5,0,0,370,371,5,25,0,0,371,372,3,18,9,0,372,373,5,16,
	0,0,373,374,5,23,0,0,374,375,5,27,0,0,375,71,1,0,0,0,376,377,7,0,0,0,377,
	73,1,0,0,0,378,379,7,1,0,0,379,75,1,0,0,0,23,79,91,106,139,146,155,164,
	180,190,200,220,227,236,245,254,263,272,281,290,299,308,319,330];

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
	public useDetector(): UseDetectorContext {
		return this.getTypedRuleContext(UseDetectorContext, 0) as UseDetectorContext;
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
	public ID(): TerminalNode {
		return this.getToken(GrammarParser.ID, 0);
	}
	public DCOMMA(): TerminalNode {
		return this.getToken(GrammarParser.DCOMMA, 0);
	}
	public ORPAR(): TerminalNode {
		return this.getToken(GrammarParser.ORPAR, 0);
	}
	public FLOAT(): TerminalNode {
		return this.getToken(GrammarParser.FLOAT, 0);
	}
	public CRPAR(): TerminalNode {
		return this.getToken(GrammarParser.CRPAR, 0);
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
