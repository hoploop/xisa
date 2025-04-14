// Generated from /Users/test/Workspace/xisa/services/player/src/Grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class GrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CONFIDENCE=1, GRAY=2, LEFT=3, RIGHT=4, MIDDLE=5, IMAGE=6, KEY_PRESS=7, 
		KEY_TYPE=8, KEY_COMBO=9, KEY_RELEASE=10, MOUSE_CLICK=11, MOUSE_DOUBLE_CLICK=12, 
		MOUSE_PRESS=13, MOUSE_RELEASE=14, MOUSE_SCROLL=15, WAIT=16, TEXT=17, POSITION=18, 
		REGEX=19, COMMA=20, DCOMMA=21, LABEL=22, USE=23, SEQUENCE=24, DETECTOR=25, 
		ID=26, STRING=27, ESC=28, ORPAR=29, EQ=30, CRPAR=31, OCPAR=32, CCPAR=33, 
		INT=34, FLOAT=35, WS=36;
	public static final int
		RULE_root = 0, RULE_stmt = 1, RULE_createDetector = 2, RULE_useDetector = 3, 
		RULE_createSelectorByPosition = 4, RULE_createSelectorByLabel = 5, RULE_createSelectorByText = 6, 
		RULE_createSelectorByRegex = 7, RULE_createOperation = 8, RULE_selector = 9, 
		RULE_selectorByLabel = 10, RULE_selectorByText = 11, RULE_selectorByRegex = 12, 
		RULE_selectorByPosition = 13, RULE_selectorByImage = 14, RULE_selectorOrder = 15, 
		RULE_createSequence = 16, RULE_runOperation = 17, RULE_operation = 18, 
		RULE_wait = 19, RULE_waitSelector = 20, RULE_mousePress = 21, RULE_mousePressSelector = 22, 
		RULE_mouseClick = 23, RULE_mouseClickSelector = 24, RULE_mouseDoubleClick = 25, 
		RULE_mouseDoubleClickSelector = 26, RULE_mouseRelease = 27, RULE_mouseReleaseSelector = 28, 
		RULE_mouseScroll = 29, RULE_mouseScrollSelector = 30, RULE_keyCombo = 31, 
		RULE_keyComboSelector = 32, RULE_keyPress = 33, RULE_keyRelease = 34, 
		RULE_keyType = 35, RULE_keyPressSelector = 36, RULE_keyReleaseSelector = 37, 
		RULE_keyTypeSelector = 38, RULE_mouseButton = 39, RULE_number = 40;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
			"createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
			"createOperation", "selector", "selectorByLabel", "selectorByText", "selectorByRegex", 
			"selectorByPosition", "selectorByImage", "selectorOrder", "createSequence", 
			"runOperation", "operation", "wait", "waitSelector", "mousePress", "mousePressSelector", 
			"mouseClick", "mouseClickSelector", "mouseDoubleClick", "mouseDoubleClickSelector", 
			"mouseRelease", "mouseReleaseSelector", "mouseScroll", "mouseScrollSelector", 
			"keyCombo", "keyComboSelector", "keyPress", "keyRelease", "keyType", 
			"keyPressSelector", "keyReleaseSelector", "keyTypeSelector", "mouseButton", 
			"number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'gray'", "'left'", "'right'", "'middle'", "'image'", "'keyPress'", 
			"'keyType'", "'keyCombo'", "'keyRelease'", "'mouseClick'", "'mouseDoubleClick'", 
			"'mousePress'", "'mouseRelease'", "'mouseScroll'", "'wait'", "'text'", 
			"'position'", "'regex'", "','", "';'", "'label'", "'use'", "'sequence'", 
			"'detector'", null, null, null, "'('", "'='", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CONFIDENCE", "GRAY", "LEFT", "RIGHT", "MIDDLE", "IMAGE", "KEY_PRESS", 
			"KEY_TYPE", "KEY_COMBO", "KEY_RELEASE", "MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", 
			"MOUSE_PRESS", "MOUSE_RELEASE", "MOUSE_SCROLL", "WAIT", "TEXT", "POSITION", 
			"REGEX", "COMMA", "DCOMMA", "LABEL", "USE", "SEQUENCE", "DETECTOR", "ID", 
			"STRING", "ESC", "ORPAR", "EQ", "CRPAR", "OCPAR", "CCPAR", "INT", "FLOAT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 75628416L) != 0)) {
				{
				{
				setState(82);
				stmt();
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public CreateDetectorContext createDetector() {
			return getRuleContext(CreateDetectorContext.class,0);
		}
		public UseDetectorContext useDetector() {
			return getRuleContext(UseDetectorContext.class,0);
		}
		public CreateSelectorByLabelContext createSelectorByLabel() {
			return getRuleContext(CreateSelectorByLabelContext.class,0);
		}
		public CreateSelectorByTextContext createSelectorByText() {
			return getRuleContext(CreateSelectorByTextContext.class,0);
		}
		public CreateSelectorByRegexContext createSelectorByRegex() {
			return getRuleContext(CreateSelectorByRegexContext.class,0);
		}
		public CreateSelectorByPositionContext createSelectorByPosition() {
			return getRuleContext(CreateSelectorByPositionContext.class,0);
		}
		public CreateOperationContext createOperation() {
			return getRuleContext(CreateOperationContext.class,0);
		}
		public CreateSequenceContext createSequence() {
			return getRuleContext(CreateSequenceContext.class,0);
		}
		public RunOperationContext runOperation() {
			return getRuleContext(RunOperationContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmt);
		try {
			setState(97);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				createDetector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
				useDetector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(90);
				createSelectorByLabel();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(91);
				createSelectorByText();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(92);
				createSelectorByRegex();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(93);
				createSelectorByPosition();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(94);
				createOperation();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(95);
				createSequence();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(96);
				runOperation();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateDetectorContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode DETECTOR() { return getToken(GrammarParser.DETECTOR, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public CreateDetectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createDetector; }
	}

	public final CreateDetectorContext createDetector() throws RecognitionException {
		CreateDetectorContext _localctx = new CreateDetectorContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_createDetector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(ID);
			setState(100);
			match(EQ);
			setState(101);
			match(DETECTOR);
			setState(102);
			match(ORPAR);
			setState(103);
			match(STRING);
			setState(104);
			match(CRPAR);
			setState(105);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UseDetectorContext extends ParserRuleContext {
		public TerminalNode USE() { return getToken(GrammarParser.USE, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public UseDetectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_useDetector; }
	}

	public final UseDetectorContext useDetector() throws RecognitionException {
		UseDetectorContext _localctx = new UseDetectorContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_useDetector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(USE);
			setState(108);
			match(ID);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ORPAR) {
				{
				setState(109);
				match(ORPAR);
				setState(110);
				match(FLOAT);
				setState(111);
				match(CRPAR);
				}
			}

			setState(114);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateSelectorByPositionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public SelectorByPositionContext selectorByPosition() {
			return getRuleContext(SelectorByPositionContext.class,0);
		}
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public CreateSelectorByPositionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSelectorByPosition; }
	}

	public final CreateSelectorByPositionContext createSelectorByPosition() throws RecognitionException {
		CreateSelectorByPositionContext _localctx = new CreateSelectorByPositionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_createSelectorByPosition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(ID);
			setState(117);
			match(EQ);
			setState(118);
			selectorByPosition();
			setState(119);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateSelectorByLabelContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public SelectorByLabelContext selectorByLabel() {
			return getRuleContext(SelectorByLabelContext.class,0);
		}
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public CreateSelectorByLabelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSelectorByLabel; }
	}

	public final CreateSelectorByLabelContext createSelectorByLabel() throws RecognitionException {
		CreateSelectorByLabelContext _localctx = new CreateSelectorByLabelContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_createSelectorByLabel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(ID);
			setState(122);
			match(EQ);
			setState(123);
			selectorByLabel();
			setState(124);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateSelectorByTextContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public SelectorByTextContext selectorByText() {
			return getRuleContext(SelectorByTextContext.class,0);
		}
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public CreateSelectorByTextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSelectorByText; }
	}

	public final CreateSelectorByTextContext createSelectorByText() throws RecognitionException {
		CreateSelectorByTextContext _localctx = new CreateSelectorByTextContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_createSelectorByText);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(ID);
			setState(127);
			match(EQ);
			setState(128);
			selectorByText();
			setState(129);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateSelectorByRegexContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public SelectorByRegexContext selectorByRegex() {
			return getRuleContext(SelectorByRegexContext.class,0);
		}
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public CreateSelectorByRegexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSelectorByRegex; }
	}

	public final CreateSelectorByRegexContext createSelectorByRegex() throws RecognitionException {
		CreateSelectorByRegexContext _localctx = new CreateSelectorByRegexContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_createSelectorByRegex);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(ID);
			setState(132);
			match(EQ);
			setState(133);
			selectorByRegex();
			setState(134);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateOperationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public CreateOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createOperation; }
	}

	public final CreateOperationContext createOperation() throws RecognitionException {
		CreateOperationContext _localctx = new CreateOperationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_createOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(ID);
			setState(137);
			match(EQ);
			setState(138);
			operation();
			setState(139);
			match(DCOMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorContext extends ParserRuleContext {
		public SelectorByLabelContext selectorByLabel() {
			return getRuleContext(SelectorByLabelContext.class,0);
		}
		public SelectorByTextContext selectorByText() {
			return getRuleContext(SelectorByTextContext.class,0);
		}
		public SelectorByRegexContext selectorByRegex() {
			return getRuleContext(SelectorByRegexContext.class,0);
		}
		public SelectorByPositionContext selectorByPosition() {
			return getRuleContext(SelectorByPositionContext.class,0);
		}
		public SelectorByImageContext selectorByImage() {
			return getRuleContext(SelectorByImageContext.class,0);
		}
		public SelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selector; }
	}

	public final SelectorContext selector() throws RecognitionException {
		SelectorContext _localctx = new SelectorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_selector);
		try {
			setState(146);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LABEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				selectorByLabel();
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(142);
				selectorByText();
				}
				break;
			case REGEX:
				enterOuterAlt(_localctx, 3);
				{
				setState(143);
				selectorByRegex();
				}
				break;
			case POSITION:
				enterOuterAlt(_localctx, 4);
				{
				setState(144);
				selectorByPosition();
				}
				break;
			case IMAGE:
				enterOuterAlt(_localctx, 5);
				{
				setState(145);
				selectorByImage();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorByLabelContext extends ParserRuleContext {
		public TerminalNode LABEL() { return getToken(GrammarParser.LABEL, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public SelectorOrderContext selectorOrder() {
			return getRuleContext(SelectorOrderContext.class,0);
		}
		public SelectorByLabelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectorByLabel; }
	}

	public final SelectorByLabelContext selectorByLabel() throws RecognitionException {
		SelectorByLabelContext _localctx = new SelectorByLabelContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_selectorByLabel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(LABEL);
			setState(149);
			match(ORPAR);
			setState(150);
			match(STRING);
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(151);
				match(COMMA);
				setState(152);
				selectorOrder();
				}
			}

			setState(155);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorByTextContext extends ParserRuleContext {
		public TerminalNode TEXT() { return getToken(GrammarParser.TEXT, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public SelectorOrderContext selectorOrder() {
			return getRuleContext(SelectorOrderContext.class,0);
		}
		public SelectorByTextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectorByText; }
	}

	public final SelectorByTextContext selectorByText() throws RecognitionException {
		SelectorByTextContext _localctx = new SelectorByTextContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_selectorByText);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(TEXT);
			setState(158);
			match(ORPAR);
			setState(159);
			match(STRING);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(160);
				match(COMMA);
				setState(161);
				selectorOrder();
				}
			}

			setState(164);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorByRegexContext extends ParserRuleContext {
		public TerminalNode REGEX() { return getToken(GrammarParser.REGEX, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public SelectorOrderContext selectorOrder() {
			return getRuleContext(SelectorOrderContext.class,0);
		}
		public SelectorByRegexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectorByRegex; }
	}

	public final SelectorByRegexContext selectorByRegex() throws RecognitionException {
		SelectorByRegexContext _localctx = new SelectorByRegexContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_selectorByRegex);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(REGEX);
			setState(167);
			match(ORPAR);
			setState(168);
			match(STRING);
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(169);
				match(COMMA);
				setState(170);
				selectorOrder();
				}
			}

			setState(173);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorByPositionContext extends ParserRuleContext {
		public TerminalNode POSITION() { return getToken(GrammarParser.POSITION, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public List<NumberContext> number() {
			return getRuleContexts(NumberContext.class);
		}
		public NumberContext number(int i) {
			return getRuleContext(NumberContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public SelectorByPositionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectorByPosition; }
	}

	public final SelectorByPositionContext selectorByPosition() throws RecognitionException {
		SelectorByPositionContext _localctx = new SelectorByPositionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_selectorByPosition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(POSITION);
			setState(176);
			match(ORPAR);
			setState(177);
			number();
			setState(178);
			match(COMMA);
			setState(179);
			number();
			setState(180);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorByImageContext extends ParserRuleContext {
		public TerminalNode IMAGE() { return getToken(GrammarParser.IMAGE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public SelectorOrderContext selectorOrder() {
			return getRuleContext(SelectorOrderContext.class,0);
		}
		public TerminalNode GRAY() { return getToken(GrammarParser.GRAY, 0); }
		public SelectorByImageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectorByImage; }
	}

	public final SelectorByImageContext selectorByImage() throws RecognitionException {
		SelectorByImageContext _localctx = new SelectorByImageContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_selectorByImage);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(IMAGE);
			setState(183);
			match(ORPAR);
			setState(184);
			match(STRING);
			setState(185);
			match(COMMA);
			setState(186);
			match(FLOAT);
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(187);
				match(COMMA);
				setState(188);
				selectorOrder();
				}
				break;
			}
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(191);
				match(COMMA);
				setState(192);
				match(GRAY);
				}
			}

			setState(195);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SelectorOrderContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(GrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(GrammarParser.INT, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public SelectorOrderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectorOrder; }
	}

	public final SelectorOrderContext selectorOrder() throws RecognitionException {
		SelectorOrderContext _localctx = new SelectorOrderContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_selectorOrder);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(INT);
			setState(202);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(198);
					match(COMMA);
					setState(199);
					match(INT);
					}
					} 
				}
				setState(204);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateSequenceContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode SEQUENCE() { return getToken(GrammarParser.SEQUENCE, 0); }
		public TerminalNode OCPAR() { return getToken(GrammarParser.OCPAR, 0); }
		public TerminalNode CCPAR() { return getToken(GrammarParser.CCPAR, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public CreateSequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSequence; }
	}

	public final CreateSequenceContext createSequence() throws RecognitionException {
		CreateSequenceContext _localctx = new CreateSequenceContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_createSequence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(ID);
			setState(206);
			match(EQ);
			setState(207);
			match(SEQUENCE);
			setState(208);
			match(OCPAR);
			setState(212);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 75628416L) != 0)) {
				{
				{
				setState(209);
				stmt();
				}
				}
				setState(214);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(215);
			match(CCPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RunOperationContext extends ParserRuleContext {
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public TerminalNode DCOMMA() { return getToken(GrammarParser.DCOMMA, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public RunOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_runOperation; }
	}

	public final RunOperationContext runOperation() throws RecognitionException {
		RunOperationContext _localctx = new RunOperationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_runOperation);
		try {
			setState(222);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY_PRESS:
			case KEY_TYPE:
			case KEY_COMBO:
			case KEY_RELEASE:
			case MOUSE_CLICK:
			case MOUSE_DOUBLE_CLICK:
			case MOUSE_PRESS:
			case MOUSE_RELEASE:
			case MOUSE_SCROLL:
			case WAIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(217);
				operation();
				setState(218);
				match(DCOMMA);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(220);
				match(ID);
				setState(221);
				match(DCOMMA);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationContext extends ParserRuleContext {
		public WaitContext wait() {
			return getRuleContext(WaitContext.class,0);
		}
		public WaitSelectorContext waitSelector() {
			return getRuleContext(WaitSelectorContext.class,0);
		}
		public MousePressContext mousePress() {
			return getRuleContext(MousePressContext.class,0);
		}
		public MousePressSelectorContext mousePressSelector() {
			return getRuleContext(MousePressSelectorContext.class,0);
		}
		public MouseReleaseSelectorContext mouseReleaseSelector() {
			return getRuleContext(MouseReleaseSelectorContext.class,0);
		}
		public MouseClickContext mouseClick() {
			return getRuleContext(MouseClickContext.class,0);
		}
		public MouseClickSelectorContext mouseClickSelector() {
			return getRuleContext(MouseClickSelectorContext.class,0);
		}
		public MouseDoubleClickContext mouseDoubleClick() {
			return getRuleContext(MouseDoubleClickContext.class,0);
		}
		public MouseDoubleClickSelectorContext mouseDoubleClickSelector() {
			return getRuleContext(MouseDoubleClickSelectorContext.class,0);
		}
		public MouseReleaseContext mouseRelease() {
			return getRuleContext(MouseReleaseContext.class,0);
		}
		public MouseScrollContext mouseScroll() {
			return getRuleContext(MouseScrollContext.class,0);
		}
		public MouseScrollSelectorContext mouseScrollSelector() {
			return getRuleContext(MouseScrollSelectorContext.class,0);
		}
		public KeyPressContext keyPress() {
			return getRuleContext(KeyPressContext.class,0);
		}
		public KeyReleaseContext keyRelease() {
			return getRuleContext(KeyReleaseContext.class,0);
		}
		public KeyTypeContext keyType() {
			return getRuleContext(KeyTypeContext.class,0);
		}
		public KeyComboContext keyCombo() {
			return getRuleContext(KeyComboContext.class,0);
		}
		public KeyComboSelectorContext keyComboSelector() {
			return getRuleContext(KeyComboSelectorContext.class,0);
		}
		public KeyPressSelectorContext keyPressSelector() {
			return getRuleContext(KeyPressSelectorContext.class,0);
		}
		public KeyReleaseSelectorContext keyReleaseSelector() {
			return getRuleContext(KeyReleaseSelectorContext.class,0);
		}
		public KeyTypeSelectorContext keyTypeSelector() {
			return getRuleContext(KeyTypeSelectorContext.class,0);
		}
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_operation);
		try {
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(224);
				wait();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(225);
				waitSelector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(226);
				mousePress();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(227);
				mousePressSelector();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(228);
				mouseReleaseSelector();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(229);
				mouseClick();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(230);
				mouseClickSelector();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(231);
				mouseDoubleClick();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(232);
				mouseDoubleClickSelector();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(233);
				mouseRelease();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(234);
				mouseScroll();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(235);
				mouseScrollSelector();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(236);
				keyPress();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(237);
				keyRelease();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(238);
				keyType();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(239);
				keyCombo();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(240);
				keyComboSelector();
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(241);
				keyPressSelector();
				}
				break;
			case 19:
				enterOuterAlt(_localctx, 19);
				{
				setState(242);
				keyReleaseSelector();
				}
				break;
			case 20:
				enterOuterAlt(_localctx, 20);
				{
				setState(243);
				keyTypeSelector();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WaitContext extends ParserRuleContext {
		public TerminalNode WAIT() { return getToken(GrammarParser.WAIT, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public WaitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wait; }
	}

	public final WaitContext wait() throws RecognitionException {
		WaitContext _localctx = new WaitContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_wait);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(WAIT);
			setState(247);
			match(ORPAR);
			setState(248);
			match(ID);
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(249);
				match(COMMA);
				setState(250);
				match(INT);
				}
			}

			setState(253);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WaitSelectorContext extends ParserRuleContext {
		public TerminalNode WAIT() { return getToken(GrammarParser.WAIT, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public WaitSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_waitSelector; }
	}

	public final WaitSelectorContext waitSelector() throws RecognitionException {
		WaitSelectorContext _localctx = new WaitSelectorContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_waitSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			match(WAIT);
			setState(256);
			match(ORPAR);
			setState(257);
			selector();
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(258);
				match(COMMA);
				setState(259);
				match(INT);
				}
			}

			setState(262);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MousePressContext extends ParserRuleContext {
		public TerminalNode MOUSE_PRESS() { return getToken(GrammarParser.MOUSE_PRESS, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MousePressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mousePress; }
	}

	public final MousePressContext mousePress() throws RecognitionException {
		MousePressContext _localctx = new MousePressContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_mousePress);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			match(MOUSE_PRESS);
			setState(265);
			match(ORPAR);
			setState(266);
			match(ID);
			setState(269);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(267);
				match(COMMA);
				setState(268);
				mouseButton();
				}
			}

			setState(271);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MousePressSelectorContext extends ParserRuleContext {
		public TerminalNode MOUSE_PRESS() { return getToken(GrammarParser.MOUSE_PRESS, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MousePressSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mousePressSelector; }
	}

	public final MousePressSelectorContext mousePressSelector() throws RecognitionException {
		MousePressSelectorContext _localctx = new MousePressSelectorContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_mousePressSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			match(MOUSE_PRESS);
			setState(274);
			match(ORPAR);
			setState(275);
			selector();
			setState(278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(276);
				match(COMMA);
				setState(277);
				mouseButton();
				}
			}

			setState(280);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseClickContext extends ParserRuleContext {
		public TerminalNode MOUSE_CLICK() { return getToken(GrammarParser.MOUSE_CLICK, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MouseClickContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseClick; }
	}

	public final MouseClickContext mouseClick() throws RecognitionException {
		MouseClickContext _localctx = new MouseClickContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_mouseClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			match(MOUSE_CLICK);
			setState(283);
			match(ORPAR);
			setState(284);
			match(ID);
			setState(287);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(285);
				match(COMMA);
				setState(286);
				mouseButton();
				}
			}

			setState(289);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseClickSelectorContext extends ParserRuleContext {
		public TerminalNode MOUSE_CLICK() { return getToken(GrammarParser.MOUSE_CLICK, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MouseClickSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseClickSelector; }
	}

	public final MouseClickSelectorContext mouseClickSelector() throws RecognitionException {
		MouseClickSelectorContext _localctx = new MouseClickSelectorContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_mouseClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			match(MOUSE_CLICK);
			setState(292);
			match(ORPAR);
			setState(293);
			selector();
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(294);
				match(COMMA);
				setState(295);
				mouseButton();
				}
			}

			setState(298);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseDoubleClickContext extends ParserRuleContext {
		public TerminalNode MOUSE_DOUBLE_CLICK() { return getToken(GrammarParser.MOUSE_DOUBLE_CLICK, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MouseDoubleClickContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseDoubleClick; }
	}

	public final MouseDoubleClickContext mouseDoubleClick() throws RecognitionException {
		MouseDoubleClickContext _localctx = new MouseDoubleClickContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_mouseDoubleClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(MOUSE_DOUBLE_CLICK);
			setState(301);
			match(ORPAR);
			setState(302);
			match(ID);
			setState(305);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(303);
				match(COMMA);
				setState(304);
				mouseButton();
				}
			}

			setState(307);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseDoubleClickSelectorContext extends ParserRuleContext {
		public TerminalNode MOUSE_DOUBLE_CLICK() { return getToken(GrammarParser.MOUSE_DOUBLE_CLICK, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MouseDoubleClickSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseDoubleClickSelector; }
	}

	public final MouseDoubleClickSelectorContext mouseDoubleClickSelector() throws RecognitionException {
		MouseDoubleClickSelectorContext _localctx = new MouseDoubleClickSelectorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_mouseDoubleClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			match(MOUSE_DOUBLE_CLICK);
			setState(310);
			match(ORPAR);
			setState(311);
			selector();
			setState(314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(312);
				match(COMMA);
				setState(313);
				mouseButton();
				}
			}

			setState(316);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseReleaseContext extends ParserRuleContext {
		public TerminalNode MOUSE_RELEASE() { return getToken(GrammarParser.MOUSE_RELEASE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MouseReleaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseRelease; }
	}

	public final MouseReleaseContext mouseRelease() throws RecognitionException {
		MouseReleaseContext _localctx = new MouseReleaseContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_mouseRelease);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			match(MOUSE_RELEASE);
			setState(319);
			match(ORPAR);
			setState(320);
			match(ID);
			setState(323);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(321);
				match(COMMA);
				setState(322);
				mouseButton();
				}
			}

			setState(325);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseReleaseSelectorContext extends ParserRuleContext {
		public TerminalNode MOUSE_RELEASE() { return getToken(GrammarParser.MOUSE_RELEASE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public MouseButtonContext mouseButton() {
			return getRuleContext(MouseButtonContext.class,0);
		}
		public MouseReleaseSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseReleaseSelector; }
	}

	public final MouseReleaseSelectorContext mouseReleaseSelector() throws RecognitionException {
		MouseReleaseSelectorContext _localctx = new MouseReleaseSelectorContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_mouseReleaseSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			match(MOUSE_RELEASE);
			setState(328);
			match(ORPAR);
			setState(329);
			selector();
			setState(332);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(330);
				match(COMMA);
				setState(331);
				mouseButton();
				}
			}

			setState(334);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseScrollContext extends ParserRuleContext {
		public TerminalNode MOUSE_SCROLL() { return getToken(GrammarParser.MOUSE_SCROLL, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public List<TerminalNode> INT() { return getTokens(GrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(GrammarParser.INT, i);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public MouseScrollContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseScroll; }
	}

	public final MouseScrollContext mouseScroll() throws RecognitionException {
		MouseScrollContext _localctx = new MouseScrollContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_mouseScroll);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			match(MOUSE_SCROLL);
			setState(337);
			match(ORPAR);
			setState(338);
			match(ID);
			setState(339);
			match(COMMA);
			setState(340);
			match(INT);
			setState(343);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(341);
				match(COMMA);
				setState(342);
				match(INT);
				}
			}

			setState(345);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseScrollSelectorContext extends ParserRuleContext {
		public TerminalNode MOUSE_SCROLL() { return getToken(GrammarParser.MOUSE_SCROLL, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public List<TerminalNode> INT() { return getTokens(GrammarParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(GrammarParser.INT, i);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public MouseScrollSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseScrollSelector; }
	}

	public final MouseScrollSelectorContext mouseScrollSelector() throws RecognitionException {
		MouseScrollSelectorContext _localctx = new MouseScrollSelectorContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_mouseScrollSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(347);
			match(MOUSE_SCROLL);
			setState(348);
			match(ORPAR);
			setState(349);
			selector();
			setState(350);
			match(COMMA);
			setState(351);
			match(INT);
			setState(354);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(352);
				match(COMMA);
				setState(353);
				match(INT);
				}
			}

			setState(356);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyComboContext extends ParserRuleContext {
		public TerminalNode KEY_COMBO() { return getToken(GrammarParser.KEY_COMBO, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public List<TerminalNode> STRING() { return getTokens(GrammarParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(GrammarParser.STRING, i);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public KeyComboContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyCombo; }
	}

	public final KeyComboContext keyCombo() throws RecognitionException {
		KeyComboContext _localctx = new KeyComboContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_keyCombo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(358);
			match(KEY_COMBO);
			setState(359);
			match(ORPAR);
			setState(360);
			match(ID);
			setState(361);
			match(STRING);
			setState(364); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(362);
				match(COMMA);
				setState(363);
				match(STRING);
				}
				}
				setState(366); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			setState(368);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyComboSelectorContext extends ParserRuleContext {
		public TerminalNode KEY_COMBO() { return getToken(GrammarParser.KEY_COMBO, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public List<TerminalNode> STRING() { return getTokens(GrammarParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(GrammarParser.STRING, i);
		}
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public KeyComboSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyComboSelector; }
	}

	public final KeyComboSelectorContext keyComboSelector() throws RecognitionException {
		KeyComboSelectorContext _localctx = new KeyComboSelectorContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_keyComboSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			match(KEY_COMBO);
			setState(371);
			match(ORPAR);
			setState(372);
			selector();
			setState(373);
			match(STRING);
			setState(376); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(374);
				match(COMMA);
				setState(375);
				match(STRING);
				}
				}
				setState(378); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			setState(380);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyPressContext extends ParserRuleContext {
		public TerminalNode KEY_PRESS() { return getToken(GrammarParser.KEY_PRESS, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyPressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyPress; }
	}

	public final KeyPressContext keyPress() throws RecognitionException {
		KeyPressContext _localctx = new KeyPressContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_keyPress);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			match(KEY_PRESS);
			setState(383);
			match(ORPAR);
			setState(384);
			match(ID);
			setState(385);
			match(COMMA);
			setState(386);
			match(STRING);
			setState(387);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyReleaseContext extends ParserRuleContext {
		public TerminalNode KEY_RELEASE() { return getToken(GrammarParser.KEY_RELEASE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyReleaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyRelease; }
	}

	public final KeyReleaseContext keyRelease() throws RecognitionException {
		KeyReleaseContext _localctx = new KeyReleaseContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_keyRelease);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			match(KEY_RELEASE);
			setState(390);
			match(ORPAR);
			setState(391);
			match(ID);
			setState(392);
			match(COMMA);
			setState(393);
			match(STRING);
			setState(394);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyTypeContext extends ParserRuleContext {
		public TerminalNode KEY_TYPE() { return getToken(GrammarParser.KEY_TYPE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyType; }
	}

	public final KeyTypeContext keyType() throws RecognitionException {
		KeyTypeContext _localctx = new KeyTypeContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_keyType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			match(KEY_TYPE);
			setState(397);
			match(ORPAR);
			setState(398);
			match(ID);
			setState(399);
			match(COMMA);
			setState(400);
			match(STRING);
			setState(401);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyPressSelectorContext extends ParserRuleContext {
		public TerminalNode KEY_PRESS() { return getToken(GrammarParser.KEY_PRESS, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyPressSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyPressSelector; }
	}

	public final KeyPressSelectorContext keyPressSelector() throws RecognitionException {
		KeyPressSelectorContext _localctx = new KeyPressSelectorContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_keyPressSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(403);
			match(KEY_PRESS);
			setState(404);
			match(ORPAR);
			setState(405);
			selector();
			setState(406);
			match(COMMA);
			setState(407);
			match(STRING);
			setState(408);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyReleaseSelectorContext extends ParserRuleContext {
		public TerminalNode KEY_RELEASE() { return getToken(GrammarParser.KEY_RELEASE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyReleaseSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyReleaseSelector; }
	}

	public final KeyReleaseSelectorContext keyReleaseSelector() throws RecognitionException {
		KeyReleaseSelectorContext _localctx = new KeyReleaseSelectorContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_keyReleaseSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			match(KEY_RELEASE);
			setState(411);
			match(ORPAR);
			setState(412);
			selector();
			setState(413);
			match(COMMA);
			setState(414);
			match(STRING);
			setState(415);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeyTypeSelectorContext extends ParserRuleContext {
		public TerminalNode KEY_TYPE() { return getToken(GrammarParser.KEY_TYPE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyTypeSelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyTypeSelector; }
	}

	public final KeyTypeSelectorContext keyTypeSelector() throws RecognitionException {
		KeyTypeSelectorContext _localctx = new KeyTypeSelectorContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_keyTypeSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(417);
			match(KEY_TYPE);
			setState(418);
			match(ORPAR);
			setState(419);
			selector();
			setState(420);
			match(COMMA);
			setState(421);
			match(STRING);
			setState(422);
			match(CRPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MouseButtonContext extends ParserRuleContext {
		public TerminalNode LEFT() { return getToken(GrammarParser.LEFT, 0); }
		public TerminalNode MIDDLE() { return getToken(GrammarParser.MIDDLE, 0); }
		public TerminalNode RIGHT() { return getToken(GrammarParser.RIGHT, 0); }
		public MouseButtonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseButton; }
	}

	public final MouseButtonContext mouseButton() throws RecognitionException {
		MouseButtonContext _localctx = new MouseButtonContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_mouseButton);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 56L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(426);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u01ad\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0001\u0000\u0005\u0000T\b\u0000\n\u0000\f\u0000W\t\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001b\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003"+
		"\u0003q\b\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0003\t\u0093\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u009a"+
		"\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u00a3\b\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0003\f\u00ac\b\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00be"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00c2\b\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00c9\b\u000f"+
		"\n\u000f\f\u000f\u00cc\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0005\u0010\u00d3\b\u0010\n\u0010\f\u0010\u00d6\t\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u00df\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012"+
		"\u00f5\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0003\u0013\u00fc\b\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u0105\b\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0003\u0015\u010e\b\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0117\b\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0003\u0017\u0120\b\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u0129\b\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0003\u0019\u0132\b\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u013b\b\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0003\u001b\u0144\b\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u014d\b\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0003\u001d\u0158\b\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0003\u001e\u0163\b\u001e\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0004\u001f"+
		"\u016d\b\u001f\u000b\u001f\f\u001f\u016e\u0001\u001f\u0001\u001f\u0001"+
		" \u0001 \u0001 \u0001 \u0001 \u0001 \u0004 \u0179\b \u000b \f \u017a\u0001"+
		" \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001\"\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001&\u0001&\u0001"+
		"&\u0001&\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0000"+
		"\u0000)\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNP\u0000\u0002\u0001\u0000\u0003"+
		"\u0005\u0001\u0000\"#\u01ba\u0000U\u0001\u0000\u0000\u0000\u0002a\u0001"+
		"\u0000\u0000\u0000\u0004c\u0001\u0000\u0000\u0000\u0006k\u0001\u0000\u0000"+
		"\u0000\bt\u0001\u0000\u0000\u0000\ny\u0001\u0000\u0000\u0000\f~\u0001"+
		"\u0000\u0000\u0000\u000e\u0083\u0001\u0000\u0000\u0000\u0010\u0088\u0001"+
		"\u0000\u0000\u0000\u0012\u0092\u0001\u0000\u0000\u0000\u0014\u0094\u0001"+
		"\u0000\u0000\u0000\u0016\u009d\u0001\u0000\u0000\u0000\u0018\u00a6\u0001"+
		"\u0000\u0000\u0000\u001a\u00af\u0001\u0000\u0000\u0000\u001c\u00b6\u0001"+
		"\u0000\u0000\u0000\u001e\u00c5\u0001\u0000\u0000\u0000 \u00cd\u0001\u0000"+
		"\u0000\u0000\"\u00de\u0001\u0000\u0000\u0000$\u00f4\u0001\u0000\u0000"+
		"\u0000&\u00f6\u0001\u0000\u0000\u0000(\u00ff\u0001\u0000\u0000\u0000*"+
		"\u0108\u0001\u0000\u0000\u0000,\u0111\u0001\u0000\u0000\u0000.\u011a\u0001"+
		"\u0000\u0000\u00000\u0123\u0001\u0000\u0000\u00002\u012c\u0001\u0000\u0000"+
		"\u00004\u0135\u0001\u0000\u0000\u00006\u013e\u0001\u0000\u0000\u00008"+
		"\u0147\u0001\u0000\u0000\u0000:\u0150\u0001\u0000\u0000\u0000<\u015b\u0001"+
		"\u0000\u0000\u0000>\u0166\u0001\u0000\u0000\u0000@\u0172\u0001\u0000\u0000"+
		"\u0000B\u017e\u0001\u0000\u0000\u0000D\u0185\u0001\u0000\u0000\u0000F"+
		"\u018c\u0001\u0000\u0000\u0000H\u0193\u0001\u0000\u0000\u0000J\u019a\u0001"+
		"\u0000\u0000\u0000L\u01a1\u0001\u0000\u0000\u0000N\u01a8\u0001\u0000\u0000"+
		"\u0000P\u01aa\u0001\u0000\u0000\u0000RT\u0003\u0002\u0001\u0000SR\u0001"+
		"\u0000\u0000\u0000TW\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000"+
		"UV\u0001\u0000\u0000\u0000V\u0001\u0001\u0000\u0000\u0000WU\u0001\u0000"+
		"\u0000\u0000Xb\u0003\u0004\u0002\u0000Yb\u0003\u0006\u0003\u0000Zb\u0003"+
		"\n\u0005\u0000[b\u0003\f\u0006\u0000\\b\u0003\u000e\u0007\u0000]b\u0003"+
		"\b\u0004\u0000^b\u0003\u0010\b\u0000_b\u0003 \u0010\u0000`b\u0003\"\u0011"+
		"\u0000aX\u0001\u0000\u0000\u0000aY\u0001\u0000\u0000\u0000aZ\u0001\u0000"+
		"\u0000\u0000a[\u0001\u0000\u0000\u0000a\\\u0001\u0000\u0000\u0000a]\u0001"+
		"\u0000\u0000\u0000a^\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000"+
		"a`\u0001\u0000\u0000\u0000b\u0003\u0001\u0000\u0000\u0000cd\u0005\u001a"+
		"\u0000\u0000de\u0005\u001e\u0000\u0000ef\u0005\u0019\u0000\u0000fg\u0005"+
		"\u001d\u0000\u0000gh\u0005\u001b\u0000\u0000hi\u0005\u001f\u0000\u0000"+
		"ij\u0005\u0015\u0000\u0000j\u0005\u0001\u0000\u0000\u0000kl\u0005\u0017"+
		"\u0000\u0000lp\u0005\u001a\u0000\u0000mn\u0005\u001d\u0000\u0000no\u0005"+
		"#\u0000\u0000oq\u0005\u001f\u0000\u0000pm\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0005\u0015\u0000\u0000"+
		"s\u0007\u0001\u0000\u0000\u0000tu\u0005\u001a\u0000\u0000uv\u0005\u001e"+
		"\u0000\u0000vw\u0003\u001a\r\u0000wx\u0005\u0015\u0000\u0000x\t\u0001"+
		"\u0000\u0000\u0000yz\u0005\u001a\u0000\u0000z{\u0005\u001e\u0000\u0000"+
		"{|\u0003\u0014\n\u0000|}\u0005\u0015\u0000\u0000}\u000b\u0001\u0000\u0000"+
		"\u0000~\u007f\u0005\u001a\u0000\u0000\u007f\u0080\u0005\u001e\u0000\u0000"+
		"\u0080\u0081\u0003\u0016\u000b\u0000\u0081\u0082\u0005\u0015\u0000\u0000"+
		"\u0082\r\u0001\u0000\u0000\u0000\u0083\u0084\u0005\u001a\u0000\u0000\u0084"+
		"\u0085\u0005\u001e\u0000\u0000\u0085\u0086\u0003\u0018\f\u0000\u0086\u0087"+
		"\u0005\u0015\u0000\u0000\u0087\u000f\u0001\u0000\u0000\u0000\u0088\u0089"+
		"\u0005\u001a\u0000\u0000\u0089\u008a\u0005\u001e\u0000\u0000\u008a\u008b"+
		"\u0003$\u0012\u0000\u008b\u008c\u0005\u0015\u0000\u0000\u008c\u0011\u0001"+
		"\u0000\u0000\u0000\u008d\u0093\u0003\u0014\n\u0000\u008e\u0093\u0003\u0016"+
		"\u000b\u0000\u008f\u0093\u0003\u0018\f\u0000\u0090\u0093\u0003\u001a\r"+
		"\u0000\u0091\u0093\u0003\u001c\u000e\u0000\u0092\u008d\u0001\u0000\u0000"+
		"\u0000\u0092\u008e\u0001\u0000\u0000\u0000\u0092\u008f\u0001\u0000\u0000"+
		"\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0092\u0091\u0001\u0000\u0000"+
		"\u0000\u0093\u0013\u0001\u0000\u0000\u0000\u0094\u0095\u0005\u0016\u0000"+
		"\u0000\u0095\u0096\u0005\u001d\u0000\u0000\u0096\u0099\u0005\u001b\u0000"+
		"\u0000\u0097\u0098\u0005\u0014\u0000\u0000\u0098\u009a\u0003\u001e\u000f"+
		"\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u0099\u009a\u0001\u0000\u0000"+
		"\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u009c\u0005\u001f\u0000"+
		"\u0000\u009c\u0015\u0001\u0000\u0000\u0000\u009d\u009e\u0005\u0011\u0000"+
		"\u0000\u009e\u009f\u0005\u001d\u0000\u0000\u009f\u00a2\u0005\u001b\u0000"+
		"\u0000\u00a0\u00a1\u0005\u0014\u0000\u0000\u00a1\u00a3\u0003\u001e\u000f"+
		"\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005\u001f\u0000"+
		"\u0000\u00a5\u0017\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005\u0013\u0000"+
		"\u0000\u00a7\u00a8\u0005\u001d\u0000\u0000\u00a8\u00ab\u0005\u001b\u0000"+
		"\u0000\u00a9\u00aa\u0005\u0014\u0000\u0000\u00aa\u00ac\u0003\u001e\u000f"+
		"\u0000\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000"+
		"\u0000\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005\u001f\u0000"+
		"\u0000\u00ae\u0019\u0001\u0000\u0000\u0000\u00af\u00b0\u0005\u0012\u0000"+
		"\u0000\u00b0\u00b1\u0005\u001d\u0000\u0000\u00b1\u00b2\u0003P(\u0000\u00b2"+
		"\u00b3\u0005\u0014\u0000\u0000\u00b3\u00b4\u0003P(\u0000\u00b4\u00b5\u0005"+
		"\u001f\u0000\u0000\u00b5\u001b\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005"+
		"\u0006\u0000\u0000\u00b7\u00b8\u0005\u001d\u0000\u0000\u00b8\u00b9\u0005"+
		"\u001b\u0000\u0000\u00b9\u00ba\u0005\u0014\u0000\u0000\u00ba\u00bd\u0005"+
		"#\u0000\u0000\u00bb\u00bc\u0005\u0014\u0000\u0000\u00bc\u00be\u0003\u001e"+
		"\u000f\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000"+
		"\u0000\u0000\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\u0014"+
		"\u0000\u0000\u00c0\u00c2\u0005\u0002\u0000\u0000\u00c1\u00bf\u0001\u0000"+
		"\u0000\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000"+
		"\u0000\u0000\u00c3\u00c4\u0005\u001f\u0000\u0000\u00c4\u001d\u0001\u0000"+
		"\u0000\u0000\u00c5\u00ca\u0005\"\u0000\u0000\u00c6\u00c7\u0005\u0014\u0000"+
		"\u0000\u00c7\u00c9\u0005\"\u0000\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c9\u00cc\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000"+
		"\u00ca\u00cb\u0001\u0000\u0000\u0000\u00cb\u001f\u0001\u0000\u0000\u0000"+
		"\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005\u001a\u0000\u0000"+
		"\u00ce\u00cf\u0005\u001e\u0000\u0000\u00cf\u00d0\u0005\u0018\u0000\u0000"+
		"\u00d0\u00d4\u0005 \u0000\u0000\u00d1\u00d3\u0003\u0002\u0001\u0000\u00d2"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d3\u00d6\u0001\u0000\u0000\u0000\u00d4"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000\u0000\u00d5"+
		"\u00d7\u0001\u0000\u0000\u0000\u00d6\u00d4\u0001\u0000\u0000\u0000\u00d7"+
		"\u00d8\u0005!\u0000\u0000\u00d8!\u0001\u0000\u0000\u0000\u00d9\u00da\u0003"+
		"$\u0012\u0000\u00da\u00db\u0005\u0015\u0000\u0000\u00db\u00df\u0001\u0000"+
		"\u0000\u0000\u00dc\u00dd\u0005\u001a\u0000\u0000\u00dd\u00df\u0005\u0015"+
		"\u0000\u0000\u00de\u00d9\u0001\u0000\u0000\u0000\u00de\u00dc\u0001\u0000"+
		"\u0000\u0000\u00df#\u0001\u0000\u0000\u0000\u00e0\u00f5\u0003&\u0013\u0000"+
		"\u00e1\u00f5\u0003(\u0014\u0000\u00e2\u00f5\u0003*\u0015\u0000\u00e3\u00f5"+
		"\u0003,\u0016\u0000\u00e4\u00f5\u00038\u001c\u0000\u00e5\u00f5\u0003."+
		"\u0017\u0000\u00e6\u00f5\u00030\u0018\u0000\u00e7\u00f5\u00032\u0019\u0000"+
		"\u00e8\u00f5\u00034\u001a\u0000\u00e9\u00f5\u00036\u001b\u0000\u00ea\u00f5"+
		"\u0003:\u001d\u0000\u00eb\u00f5\u0003<\u001e\u0000\u00ec\u00f5\u0003B"+
		"!\u0000\u00ed\u00f5\u0003D\"\u0000\u00ee\u00f5\u0003F#\u0000\u00ef\u00f5"+
		"\u0003>\u001f\u0000\u00f0\u00f5\u0003@ \u0000\u00f1\u00f5\u0003H$\u0000"+
		"\u00f2\u00f5\u0003J%\u0000\u00f3\u00f5\u0003L&\u0000\u00f4\u00e0\u0001"+
		"\u0000\u0000\u0000\u00f4\u00e1\u0001\u0000\u0000\u0000\u00f4\u00e2\u0001"+
		"\u0000\u0000\u0000\u00f4\u00e3\u0001\u0000\u0000\u0000\u00f4\u00e4\u0001"+
		"\u0000\u0000\u0000\u00f4\u00e5\u0001\u0000\u0000\u0000\u00f4\u00e6\u0001"+
		"\u0000\u0000\u0000\u00f4\u00e7\u0001\u0000\u0000\u0000\u00f4\u00e8\u0001"+
		"\u0000\u0000\u0000\u00f4\u00e9\u0001\u0000\u0000\u0000\u00f4\u00ea\u0001"+
		"\u0000\u0000\u0000\u00f4\u00eb\u0001\u0000\u0000\u0000\u00f4\u00ec\u0001"+
		"\u0000\u0000\u0000\u00f4\u00ed\u0001\u0000\u0000\u0000\u00f4\u00ee\u0001"+
		"\u0000\u0000\u0000\u00f4\u00ef\u0001\u0000\u0000\u0000\u00f4\u00f0\u0001"+
		"\u0000\u0000\u0000\u00f4\u00f1\u0001\u0000\u0000\u0000\u00f4\u00f2\u0001"+
		"\u0000\u0000\u0000\u00f4\u00f3\u0001\u0000\u0000\u0000\u00f5%\u0001\u0000"+
		"\u0000\u0000\u00f6\u00f7\u0005\u0010\u0000\u0000\u00f7\u00f8\u0005\u001d"+
		"\u0000\u0000\u00f8\u00fb\u0005\u001a\u0000\u0000\u00f9\u00fa\u0005\u0014"+
		"\u0000\u0000\u00fa\u00fc\u0005\"\u0000\u0000\u00fb\u00f9\u0001\u0000\u0000"+
		"\u0000\u00fb\u00fc\u0001\u0000\u0000\u0000\u00fc\u00fd\u0001\u0000\u0000"+
		"\u0000\u00fd\u00fe\u0005\u001f\u0000\u0000\u00fe\'\u0001\u0000\u0000\u0000"+
		"\u00ff\u0100\u0005\u0010\u0000\u0000\u0100\u0101\u0005\u001d\u0000\u0000"+
		"\u0101\u0104\u0003\u0012\t\u0000\u0102\u0103\u0005\u0014\u0000\u0000\u0103"+
		"\u0105\u0005\"\u0000\u0000\u0104\u0102\u0001\u0000\u0000\u0000\u0104\u0105"+
		"\u0001\u0000\u0000\u0000\u0105\u0106\u0001\u0000\u0000\u0000\u0106\u0107"+
		"\u0005\u001f\u0000\u0000\u0107)\u0001\u0000\u0000\u0000\u0108\u0109\u0005"+
		"\r\u0000\u0000\u0109\u010a\u0005\u001d\u0000\u0000\u010a\u010d\u0005\u001a"+
		"\u0000\u0000\u010b\u010c\u0005\u0014\u0000\u0000\u010c\u010e\u0003N\'"+
		"\u0000\u010d\u010b\u0001\u0000\u0000\u0000\u010d\u010e\u0001\u0000\u0000"+
		"\u0000\u010e\u010f\u0001\u0000\u0000\u0000\u010f\u0110\u0005\u001f\u0000"+
		"\u0000\u0110+\u0001\u0000\u0000\u0000\u0111\u0112\u0005\r\u0000\u0000"+
		"\u0112\u0113\u0005\u001d\u0000\u0000\u0113\u0116\u0003\u0012\t\u0000\u0114"+
		"\u0115\u0005\u0014\u0000\u0000\u0115\u0117\u0003N\'\u0000\u0116\u0114"+
		"\u0001\u0000\u0000\u0000\u0116\u0117\u0001\u0000\u0000\u0000\u0117\u0118"+
		"\u0001\u0000\u0000\u0000\u0118\u0119\u0005\u001f\u0000\u0000\u0119-\u0001"+
		"\u0000\u0000\u0000\u011a\u011b\u0005\u000b\u0000\u0000\u011b\u011c\u0005"+
		"\u001d\u0000\u0000\u011c\u011f\u0005\u001a\u0000\u0000\u011d\u011e\u0005"+
		"\u0014\u0000\u0000\u011e\u0120\u0003N\'\u0000\u011f\u011d\u0001\u0000"+
		"\u0000\u0000\u011f\u0120\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000"+
		"\u0000\u0000\u0121\u0122\u0005\u001f\u0000\u0000\u0122/\u0001\u0000\u0000"+
		"\u0000\u0123\u0124\u0005\u000b\u0000\u0000\u0124\u0125\u0005\u001d\u0000"+
		"\u0000\u0125\u0128\u0003\u0012\t\u0000\u0126\u0127\u0005\u0014\u0000\u0000"+
		"\u0127\u0129\u0003N\'\u0000\u0128\u0126\u0001\u0000\u0000\u0000\u0128"+
		"\u0129\u0001\u0000\u0000\u0000\u0129\u012a\u0001\u0000\u0000\u0000\u012a"+
		"\u012b\u0005\u001f\u0000\u0000\u012b1\u0001\u0000\u0000\u0000\u012c\u012d"+
		"\u0005\f\u0000\u0000\u012d\u012e\u0005\u001d\u0000\u0000\u012e\u0131\u0005"+
		"\u001a\u0000\u0000\u012f\u0130\u0005\u0014\u0000\u0000\u0130\u0132\u0003"+
		"N\'\u0000\u0131\u012f\u0001\u0000\u0000\u0000\u0131\u0132\u0001\u0000"+
		"\u0000\u0000\u0132\u0133\u0001\u0000\u0000\u0000\u0133\u0134\u0005\u001f"+
		"\u0000\u0000\u01343\u0001\u0000\u0000\u0000\u0135\u0136\u0005\f\u0000"+
		"\u0000\u0136\u0137\u0005\u001d\u0000\u0000\u0137\u013a\u0003\u0012\t\u0000"+
		"\u0138\u0139\u0005\u0014\u0000\u0000\u0139\u013b\u0003N\'\u0000\u013a"+
		"\u0138\u0001\u0000\u0000\u0000\u013a\u013b\u0001\u0000\u0000\u0000\u013b"+
		"\u013c\u0001\u0000\u0000\u0000\u013c\u013d\u0005\u001f\u0000\u0000\u013d"+
		"5\u0001\u0000\u0000\u0000\u013e\u013f\u0005\u000e\u0000\u0000\u013f\u0140"+
		"\u0005\u001d\u0000\u0000\u0140\u0143\u0005\u001a\u0000\u0000\u0141\u0142"+
		"\u0005\u0014\u0000\u0000\u0142\u0144\u0003N\'\u0000\u0143\u0141\u0001"+
		"\u0000\u0000\u0000\u0143\u0144\u0001\u0000\u0000\u0000\u0144\u0145\u0001"+
		"\u0000\u0000\u0000\u0145\u0146\u0005\u001f\u0000\u0000\u01467\u0001\u0000"+
		"\u0000\u0000\u0147\u0148\u0005\u000e\u0000\u0000\u0148\u0149\u0005\u001d"+
		"\u0000\u0000\u0149\u014c\u0003\u0012\t\u0000\u014a\u014b\u0005\u0014\u0000"+
		"\u0000\u014b\u014d\u0003N\'\u0000\u014c\u014a\u0001\u0000\u0000\u0000"+
		"\u014c\u014d\u0001\u0000\u0000\u0000\u014d\u014e\u0001\u0000\u0000\u0000"+
		"\u014e\u014f\u0005\u001f\u0000\u0000\u014f9\u0001\u0000\u0000\u0000\u0150"+
		"\u0151\u0005\u000f\u0000\u0000\u0151\u0152\u0005\u001d\u0000\u0000\u0152"+
		"\u0153\u0005\u001a\u0000\u0000\u0153\u0154\u0005\u0014\u0000\u0000\u0154"+
		"\u0157\u0005\"\u0000\u0000\u0155\u0156\u0005\u0014\u0000\u0000\u0156\u0158"+
		"\u0005\"\u0000\u0000\u0157\u0155\u0001\u0000\u0000\u0000\u0157\u0158\u0001"+
		"\u0000\u0000\u0000\u0158\u0159\u0001\u0000\u0000\u0000\u0159\u015a\u0005"+
		"\u001f\u0000\u0000\u015a;\u0001\u0000\u0000\u0000\u015b\u015c\u0005\u000f"+
		"\u0000\u0000\u015c\u015d\u0005\u001d\u0000\u0000\u015d\u015e\u0003\u0012"+
		"\t\u0000\u015e\u015f\u0005\u0014\u0000\u0000\u015f\u0162\u0005\"\u0000"+
		"\u0000\u0160\u0161\u0005\u0014\u0000\u0000\u0161\u0163\u0005\"\u0000\u0000"+
		"\u0162\u0160\u0001\u0000\u0000\u0000\u0162\u0163\u0001\u0000\u0000\u0000"+
		"\u0163\u0164\u0001\u0000\u0000\u0000\u0164\u0165\u0005\u001f\u0000\u0000"+
		"\u0165=\u0001\u0000\u0000\u0000\u0166\u0167\u0005\t\u0000\u0000\u0167"+
		"\u0168\u0005\u001d\u0000\u0000\u0168\u0169\u0005\u001a\u0000\u0000\u0169"+
		"\u016c\u0005\u001b\u0000\u0000\u016a\u016b\u0005\u0014\u0000\u0000\u016b"+
		"\u016d\u0005\u001b\u0000\u0000\u016c\u016a\u0001\u0000\u0000\u0000\u016d"+
		"\u016e\u0001\u0000\u0000\u0000\u016e\u016c\u0001\u0000\u0000\u0000\u016e"+
		"\u016f\u0001\u0000\u0000\u0000\u016f\u0170\u0001\u0000\u0000\u0000\u0170"+
		"\u0171\u0005\u001f\u0000\u0000\u0171?\u0001\u0000\u0000\u0000\u0172\u0173"+
		"\u0005\t\u0000\u0000\u0173\u0174\u0005\u001d\u0000\u0000\u0174\u0175\u0003"+
		"\u0012\t\u0000\u0175\u0178\u0005\u001b\u0000\u0000\u0176\u0177\u0005\u0014"+
		"\u0000\u0000\u0177\u0179\u0005\u001b\u0000\u0000\u0178\u0176\u0001\u0000"+
		"\u0000\u0000\u0179\u017a\u0001\u0000\u0000\u0000\u017a\u0178\u0001\u0000"+
		"\u0000\u0000\u017a\u017b\u0001\u0000\u0000\u0000\u017b\u017c\u0001\u0000"+
		"\u0000\u0000\u017c\u017d\u0005\u001f\u0000\u0000\u017dA\u0001\u0000\u0000"+
		"\u0000\u017e\u017f\u0005\u0007\u0000\u0000\u017f\u0180\u0005\u001d\u0000"+
		"\u0000\u0180\u0181\u0005\u001a\u0000\u0000\u0181\u0182\u0005\u0014\u0000"+
		"\u0000\u0182\u0183\u0005\u001b\u0000\u0000\u0183\u0184\u0005\u001f\u0000"+
		"\u0000\u0184C\u0001\u0000\u0000\u0000\u0185\u0186\u0005\n\u0000\u0000"+
		"\u0186\u0187\u0005\u001d\u0000\u0000\u0187\u0188\u0005\u001a\u0000\u0000"+
		"\u0188\u0189\u0005\u0014\u0000\u0000\u0189\u018a\u0005\u001b\u0000\u0000"+
		"\u018a\u018b\u0005\u001f\u0000\u0000\u018bE\u0001\u0000\u0000\u0000\u018c"+
		"\u018d\u0005\b\u0000\u0000\u018d\u018e\u0005\u001d\u0000\u0000\u018e\u018f"+
		"\u0005\u001a\u0000\u0000\u018f\u0190\u0005\u0014\u0000\u0000\u0190\u0191"+
		"\u0005\u001b\u0000\u0000\u0191\u0192\u0005\u001f\u0000\u0000\u0192G\u0001"+
		"\u0000\u0000\u0000\u0193\u0194\u0005\u0007\u0000\u0000\u0194\u0195\u0005"+
		"\u001d\u0000\u0000\u0195\u0196\u0003\u0012\t\u0000\u0196\u0197\u0005\u0014"+
		"\u0000\u0000\u0197\u0198\u0005\u001b\u0000\u0000\u0198\u0199\u0005\u001f"+
		"\u0000\u0000\u0199I\u0001\u0000\u0000\u0000\u019a\u019b\u0005\n\u0000"+
		"\u0000\u019b\u019c\u0005\u001d\u0000\u0000\u019c\u019d\u0003\u0012\t\u0000"+
		"\u019d\u019e\u0005\u0014\u0000\u0000\u019e\u019f\u0005\u001b\u0000\u0000"+
		"\u019f\u01a0\u0005\u001f\u0000\u0000\u01a0K\u0001\u0000\u0000\u0000\u01a1"+
		"\u01a2\u0005\b\u0000\u0000\u01a2\u01a3\u0005\u001d\u0000\u0000\u01a3\u01a4"+
		"\u0003\u0012\t\u0000\u01a4\u01a5\u0005\u0014\u0000\u0000\u01a5\u01a6\u0005"+
		"\u001b\u0000\u0000\u01a6\u01a7\u0005\u001f\u0000\u0000\u01a7M\u0001\u0000"+
		"\u0000\u0000\u01a8\u01a9\u0007\u0000\u0000\u0000\u01a9O\u0001\u0000\u0000"+
		"\u0000\u01aa\u01ab\u0007\u0001\u0000\u0000\u01abQ\u0001\u0000\u0000\u0000"+
		"\u001bUap\u0092\u0099\u00a2\u00ab\u00bd\u00c1\u00ca\u00d4\u00de\u00f4"+
		"\u00fb\u0104\u010d\u0116\u011f\u0128\u0131\u013a\u0143\u014c\u0157\u0162"+
		"\u016e\u017a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}