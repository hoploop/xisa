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
		LEFT=1, RIGHT=2, MIDDLE=3, KEY_PRESS=4, KEY_RELEASE=5, KEY_TYPE=6, MOUSE_CLICK=7, 
		MOUSE_DOUBLE_CLICK=8, MOUSE_PRESS=9, MOUSE_RELEASE=10, MOUSE_SCROLL=11, 
		WAIT=12, TEXT=13, POSITION=14, REGEX=15, COMMA=16, LABEL=17, USE=18, SCENARIO=19, 
		DETECTOR=20, ID=21, STRING=22, ESC=23, ORPAR=24, EQ=25, CRPAR=26, OCPAR=27, 
		CCPAR=28, INT=29, FLOAT=30, WS=31;
	public static final int
		RULE_root = 0, RULE_stmt = 1, RULE_createDetector = 2, RULE_useDetector = 3, 
		RULE_createSelectorByPosition = 4, RULE_createSelectorByLabel = 5, RULE_createSelectorByText = 6, 
		RULE_createSelectorByRegex = 7, RULE_createStep = 8, RULE_selector = 9, 
		RULE_selectorByLabel = 10, RULE_selectorByText = 11, RULE_selectorByRegex = 12, 
		RULE_selectorByPosition = 13, RULE_selectorOrder = 14, RULE_createScenario = 15, 
		RULE_action = 16, RULE_wait = 17, RULE_waitSelector = 18, RULE_mousePress = 19, 
		RULE_mousePressSelector = 20, RULE_mouseClick = 21, RULE_mouseClickSelector = 22, 
		RULE_mouseDoubleClick = 23, RULE_mouseDoubleClickSelector = 24, RULE_mouseRelease = 25, 
		RULE_mouseReleaseSelector = 26, RULE_mouseScroll = 27, RULE_keyPress = 28, 
		RULE_keyRelease = 29, RULE_mouseButton = 30, RULE_number = 31;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
			"createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
			"createStep", "selector", "selectorByLabel", "selectorByText", "selectorByRegex", 
			"selectorByPosition", "selectorOrder", "createScenario", "action", "wait", 
			"waitSelector", "mousePress", "mousePressSelector", "mouseClick", "mouseClickSelector", 
			"mouseDoubleClick", "mouseDoubleClickSelector", "mouseRelease", "mouseReleaseSelector", 
			"mouseScroll", "keyPress", "keyRelease", "mouseButton", "number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'left'", "'right'", "'middle'", "'keyPress'", "'keyRelease'", 
			"'keyType'", "'mouseClick'", "'mouseDoubleClick'", "'mousePress'", "'mouseRelease'", 
			"'mouseScroll'", "'wait'", "'text'", "'position'", "'regex'", "','", 
			"'label'", "'use'", "'scenario'", "'detector'", null, null, null, "'('", 
			"'='", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", "KEY_RELEASE", "KEY_TYPE", 
			"MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", "MOUSE_PRESS", "MOUSE_RELEASE", 
			"MOUSE_SCROLL", "WAIT", "TEXT", "POSITION", "REGEX", "COMMA", "LABEL", 
			"USE", "SCENARIO", "DETECTOR", "ID", "STRING", "ESC", "ORPAR", "EQ", 
			"CRPAR", "OCPAR", "CCPAR", "INT", "FLOAT", "WS"
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
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==USE || _la==ID) {
				{
				{
				setState(64);
				stmt();
				}
				}
				setState(69);
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
		public CreateStepContext createStep() {
			return getRuleContext(CreateStepContext.class,0);
		}
		public CreateScenarioContext createScenario() {
			return getRuleContext(CreateScenarioContext.class,0);
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
			setState(78);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				createDetector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(71);
				useDetector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(72);
				createSelectorByLabel();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(73);
				createSelectorByText();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(74);
				createSelectorByRegex();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(75);
				createSelectorByPosition();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(76);
				createStep();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(77);
				createScenario();
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
			setState(80);
			match(ID);
			setState(81);
			match(EQ);
			setState(82);
			match(DETECTOR);
			setState(83);
			match(ORPAR);
			setState(84);
			match(STRING);
			setState(85);
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
	public static class UseDetectorContext extends ParserRuleContext {
		public TerminalNode USE() { return getToken(GrammarParser.USE, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public UseDetectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_useDetector; }
	}

	public final UseDetectorContext useDetector() throws RecognitionException {
		UseDetectorContext _localctx = new UseDetectorContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_useDetector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(USE);
			setState(88);
			match(ID);
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
			setState(90);
			match(ID);
			setState(91);
			match(EQ);
			setState(92);
			selectorByPosition();
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
			setState(94);
			match(ID);
			setState(95);
			match(EQ);
			setState(96);
			selectorByLabel();
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
			setState(98);
			match(ID);
			setState(99);
			match(EQ);
			setState(100);
			selectorByText();
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
			setState(102);
			match(ID);
			setState(103);
			match(EQ);
			setState(104);
			selectorByRegex();
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
	public static class CreateStepContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public CreateStepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createStep; }
	}

	public final CreateStepContext createStep() throws RecognitionException {
		CreateStepContext _localctx = new CreateStepContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_createStep);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(ID);
			setState(107);
			match(EQ);
			setState(108);
			action();
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
		public SelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selector; }
	}

	public final SelectorContext selector() throws RecognitionException {
		SelectorContext _localctx = new SelectorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_selector);
		try {
			setState(114);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LABEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				selectorByLabel();
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				selectorByText();
				}
				break;
			case REGEX:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				selectorByRegex();
				}
				break;
			case POSITION:
				enterOuterAlt(_localctx, 4);
				{
				setState(113);
				selectorByPosition();
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
			setState(116);
			match(LABEL);
			setState(117);
			match(ORPAR);
			setState(118);
			match(STRING);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(119);
				match(COMMA);
				setState(120);
				selectorOrder();
				}
			}

			setState(123);
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
			setState(125);
			match(TEXT);
			setState(126);
			match(ORPAR);
			setState(127);
			match(STRING);
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(128);
				match(COMMA);
				setState(129);
				selectorOrder();
				}
			}

			setState(132);
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
			setState(134);
			match(REGEX);
			setState(135);
			match(ORPAR);
			setState(136);
			match(STRING);
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(137);
				match(COMMA);
				setState(138);
				selectorOrder();
				}
			}

			setState(141);
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
			setState(143);
			match(POSITION);
			setState(144);
			match(ORPAR);
			setState(145);
			number();
			setState(146);
			match(COMMA);
			setState(147);
			number();
			setState(148);
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
		enterRule(_localctx, 28, RULE_selectorOrder);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(INT);
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(151);
				match(COMMA);
				setState(152);
				match(INT);
				}
				}
				setState(157);
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
	public static class CreateScenarioContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GrammarParser.ID, i);
		}
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode SCENARIO() { return getToken(GrammarParser.SCENARIO, 0); }
		public TerminalNode OCPAR() { return getToken(GrammarParser.OCPAR, 0); }
		public TerminalNode CCPAR() { return getToken(GrammarParser.CCPAR, 0); }
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public CreateScenarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createScenario; }
	}

	public final CreateScenarioContext createScenario() throws RecognitionException {
		CreateScenarioContext _localctx = new CreateScenarioContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_createScenario);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(ID);
			setState(159);
			match(EQ);
			setState(160);
			match(SCENARIO);
			setState(161);
			match(OCPAR);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2105264L) != 0)) {
				{
				setState(164);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case KEY_PRESS:
				case KEY_RELEASE:
				case MOUSE_CLICK:
				case MOUSE_DOUBLE_CLICK:
				case MOUSE_PRESS:
				case MOUSE_RELEASE:
				case MOUSE_SCROLL:
				case WAIT:
					{
					setState(162);
					action();
					}
					break;
				case ID:
					{
					setState(163);
					match(ID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(169);
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
	public static class ActionContext extends ParserRuleContext {
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
		public KeyPressContext keyPress() {
			return getRuleContext(KeyPressContext.class,0);
		}
		public KeyReleaseContext keyRelease() {
			return getRuleContext(KeyReleaseContext.class,0);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_action);
		try {
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				wait();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				waitSelector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(173);
				mousePress();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(174);
				mousePressSelector();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(175);
				mouseReleaseSelector();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(176);
				mouseClick();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(177);
				mouseClickSelector();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(178);
				mouseDoubleClick();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(179);
				mouseDoubleClickSelector();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(180);
				mouseRelease();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(181);
				mouseScroll();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(182);
				keyPress();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(183);
				keyRelease();
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
		enterRule(_localctx, 34, RULE_wait);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			match(WAIT);
			setState(187);
			match(ORPAR);
			setState(188);
			match(ID);
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(189);
				match(COMMA);
				setState(190);
				match(INT);
				}
			}

			setState(193);
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
		enterRule(_localctx, 36, RULE_waitSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(WAIT);
			setState(196);
			match(ORPAR);
			setState(197);
			selector();
			setState(200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(198);
				match(COMMA);
				setState(199);
				match(INT);
				}
			}

			setState(202);
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
		enterRule(_localctx, 38, RULE_mousePress);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(MOUSE_PRESS);
			setState(205);
			match(ORPAR);
			setState(206);
			match(ID);
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(207);
				match(COMMA);
				setState(208);
				mouseButton();
				}
			}

			setState(211);
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
		enterRule(_localctx, 40, RULE_mousePressSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(MOUSE_PRESS);
			setState(214);
			match(ORPAR);
			setState(215);
			selector();
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(216);
				match(COMMA);
				setState(217);
				mouseButton();
				}
			}

			setState(220);
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
		enterRule(_localctx, 42, RULE_mouseClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(MOUSE_CLICK);
			setState(223);
			match(ORPAR);
			setState(224);
			match(ID);
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(225);
				match(COMMA);
				setState(226);
				mouseButton();
				}
			}

			setState(229);
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
		enterRule(_localctx, 44, RULE_mouseClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(MOUSE_CLICK);
			setState(232);
			match(ORPAR);
			setState(233);
			selector();
			setState(236);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(234);
				match(COMMA);
				setState(235);
				mouseButton();
				}
			}

			setState(238);
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
		enterRule(_localctx, 46, RULE_mouseDoubleClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(MOUSE_DOUBLE_CLICK);
			setState(241);
			match(ORPAR);
			setState(242);
			match(ID);
			setState(245);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(243);
				match(COMMA);
				setState(244);
				mouseButton();
				}
			}

			setState(247);
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
		enterRule(_localctx, 48, RULE_mouseDoubleClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			match(MOUSE_DOUBLE_CLICK);
			setState(250);
			match(ORPAR);
			setState(251);
			selector();
			setState(254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(252);
				match(COMMA);
				setState(253);
				mouseButton();
				}
			}

			setState(256);
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
		enterRule(_localctx, 50, RULE_mouseRelease);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(MOUSE_RELEASE);
			setState(259);
			match(ORPAR);
			setState(260);
			match(ID);
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(261);
				match(COMMA);
				setState(262);
				mouseButton();
				}
			}

			setState(265);
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
		enterRule(_localctx, 52, RULE_mouseReleaseSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(MOUSE_RELEASE);
			setState(268);
			match(ORPAR);
			setState(269);
			selector();
			setState(272);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(270);
				match(COMMA);
				setState(271);
				mouseButton();
				}
			}

			setState(274);
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
		enterRule(_localctx, 54, RULE_mouseScroll);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			match(MOUSE_SCROLL);
			setState(277);
			match(ORPAR);
			setState(278);
			match(ID);
			setState(279);
			match(COMMA);
			setState(280);
			match(INT);
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(281);
				match(COMMA);
				setState(282);
				match(INT);
				}
			}

			setState(285);
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
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyPressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyPress; }
	}

	public final KeyPressContext keyPress() throws RecognitionException {
		KeyPressContext _localctx = new KeyPressContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_keyPress);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			match(KEY_PRESS);
			setState(288);
			match(ORPAR);
			setState(289);
			match(STRING);
			setState(290);
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
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public KeyReleaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyRelease; }
	}

	public final KeyReleaseContext keyRelease() throws RecognitionException {
		KeyReleaseContext _localctx = new KeyReleaseContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_keyRelease);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			match(KEY_RELEASE);
			setState(293);
			match(ORPAR);
			setState(294);
			match(STRING);
			setState(295);
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
		enterRule(_localctx, 60, RULE_mouseButton);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14L) != 0)) ) {
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
		enterRule(_localctx, 62, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
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
		"\u0004\u0001\u001f\u012e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0002\u001f\u0007\u001f\u0001\u0000\u0005\u0000B\b\u0000\n\u0000"+
		"\f\u0000E\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001O\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0003\ts\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\nz\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u0083\b\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u008c\b\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000e\u009a\b\u000e\n\u000e\f\u000e\u009d\t\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005"+
		"\u000f\u00a5\b\u000f\n\u000f\f\u000f\u00a8\t\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0003\u0010\u00b9\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0003\u0011\u00c0\b\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012"+
		"\u00c9\b\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0003\u0013\u00d2\b\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014"+
		"\u00db\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0003\u0015\u00e4\b\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016"+
		"\u00ed\b\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u00f6\b\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0003\u0018"+
		"\u00ff\b\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0003\u0019\u0108\b\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a"+
		"\u0111\b\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u011c\b\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0000\u0000"+
		" \u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.02468:<>\u0000\u0002\u0001\u0000\u0001\u0003\u0001"+
		"\u0000\u001d\u001e\u0135\u0000C\u0001\u0000\u0000\u0000\u0002N\u0001\u0000"+
		"\u0000\u0000\u0004P\u0001\u0000\u0000\u0000\u0006W\u0001\u0000\u0000\u0000"+
		"\bZ\u0001\u0000\u0000\u0000\n^\u0001\u0000\u0000\u0000\fb\u0001\u0000"+
		"\u0000\u0000\u000ef\u0001\u0000\u0000\u0000\u0010j\u0001\u0000\u0000\u0000"+
		"\u0012r\u0001\u0000\u0000\u0000\u0014t\u0001\u0000\u0000\u0000\u0016}"+
		"\u0001\u0000\u0000\u0000\u0018\u0086\u0001\u0000\u0000\u0000\u001a\u008f"+
		"\u0001\u0000\u0000\u0000\u001c\u0096\u0001\u0000\u0000\u0000\u001e\u009e"+
		"\u0001\u0000\u0000\u0000 \u00b8\u0001\u0000\u0000\u0000\"\u00ba\u0001"+
		"\u0000\u0000\u0000$\u00c3\u0001\u0000\u0000\u0000&\u00cc\u0001\u0000\u0000"+
		"\u0000(\u00d5\u0001\u0000\u0000\u0000*\u00de\u0001\u0000\u0000\u0000,"+
		"\u00e7\u0001\u0000\u0000\u0000.\u00f0\u0001\u0000\u0000\u00000\u00f9\u0001"+
		"\u0000\u0000\u00002\u0102\u0001\u0000\u0000\u00004\u010b\u0001\u0000\u0000"+
		"\u00006\u0114\u0001\u0000\u0000\u00008\u011f\u0001\u0000\u0000\u0000:"+
		"\u0124\u0001\u0000\u0000\u0000<\u0129\u0001\u0000\u0000\u0000>\u012b\u0001"+
		"\u0000\u0000\u0000@B\u0003\u0002\u0001\u0000A@\u0001\u0000\u0000\u0000"+
		"BE\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000"+
		"\u0000D\u0001\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000FO\u0003"+
		"\u0004\u0002\u0000GO\u0003\u0006\u0003\u0000HO\u0003\n\u0005\u0000IO\u0003"+
		"\f\u0006\u0000JO\u0003\u000e\u0007\u0000KO\u0003\b\u0004\u0000LO\u0003"+
		"\u0010\b\u0000MO\u0003\u001e\u000f\u0000NF\u0001\u0000\u0000\u0000NG\u0001"+
		"\u0000\u0000\u0000NH\u0001\u0000\u0000\u0000NI\u0001\u0000\u0000\u0000"+
		"NJ\u0001\u0000\u0000\u0000NK\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000"+
		"\u0000NM\u0001\u0000\u0000\u0000O\u0003\u0001\u0000\u0000\u0000PQ\u0005"+
		"\u0015\u0000\u0000QR\u0005\u0019\u0000\u0000RS\u0005\u0014\u0000\u0000"+
		"ST\u0005\u0018\u0000\u0000TU\u0005\u0016\u0000\u0000UV\u0005\u001a\u0000"+
		"\u0000V\u0005\u0001\u0000\u0000\u0000WX\u0005\u0012\u0000\u0000XY\u0005"+
		"\u0015\u0000\u0000Y\u0007\u0001\u0000\u0000\u0000Z[\u0005\u0015\u0000"+
		"\u0000[\\\u0005\u0019\u0000\u0000\\]\u0003\u001a\r\u0000]\t\u0001\u0000"+
		"\u0000\u0000^_\u0005\u0015\u0000\u0000_`\u0005\u0019\u0000\u0000`a\u0003"+
		"\u0014\n\u0000a\u000b\u0001\u0000\u0000\u0000bc\u0005\u0015\u0000\u0000"+
		"cd\u0005\u0019\u0000\u0000de\u0003\u0016\u000b\u0000e\r\u0001\u0000\u0000"+
		"\u0000fg\u0005\u0015\u0000\u0000gh\u0005\u0019\u0000\u0000hi\u0003\u0018"+
		"\f\u0000i\u000f\u0001\u0000\u0000\u0000jk\u0005\u0015\u0000\u0000kl\u0005"+
		"\u0019\u0000\u0000lm\u0003 \u0010\u0000m\u0011\u0001\u0000\u0000\u0000"+
		"ns\u0003\u0014\n\u0000os\u0003\u0016\u000b\u0000ps\u0003\u0018\f\u0000"+
		"qs\u0003\u001a\r\u0000rn\u0001\u0000\u0000\u0000ro\u0001\u0000\u0000\u0000"+
		"rp\u0001\u0000\u0000\u0000rq\u0001\u0000\u0000\u0000s\u0013\u0001\u0000"+
		"\u0000\u0000tu\u0005\u0011\u0000\u0000uv\u0005\u0018\u0000\u0000vy\u0005"+
		"\u0016\u0000\u0000wx\u0005\u0010\u0000\u0000xz\u0003\u001c\u000e\u0000"+
		"yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000"+
		"\u0000{|\u0005\u001a\u0000\u0000|\u0015\u0001\u0000\u0000\u0000}~\u0005"+
		"\r\u0000\u0000~\u007f\u0005\u0018\u0000\u0000\u007f\u0082\u0005\u0016"+
		"\u0000\u0000\u0080\u0081\u0005\u0010\u0000\u0000\u0081\u0083\u0003\u001c"+
		"\u000e\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000"+
		"\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0085\u0005\u001a"+
		"\u0000\u0000\u0085\u0017\u0001\u0000\u0000\u0000\u0086\u0087\u0005\u000f"+
		"\u0000\u0000\u0087\u0088\u0005\u0018\u0000\u0000\u0088\u008b\u0005\u0016"+
		"\u0000\u0000\u0089\u008a\u0005\u0010\u0000\u0000\u008a\u008c\u0003\u001c"+
		"\u000e\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000"+
		"\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u001a"+
		"\u0000\u0000\u008e\u0019\u0001\u0000\u0000\u0000\u008f\u0090\u0005\u000e"+
		"\u0000\u0000\u0090\u0091\u0005\u0018\u0000\u0000\u0091\u0092\u0003>\u001f"+
		"\u0000\u0092\u0093\u0005\u0010\u0000\u0000\u0093\u0094\u0003>\u001f\u0000"+
		"\u0094\u0095\u0005\u001a\u0000\u0000\u0095\u001b\u0001\u0000\u0000\u0000"+
		"\u0096\u009b\u0005\u001d\u0000\u0000\u0097\u0098\u0005\u0010\u0000\u0000"+
		"\u0098\u009a\u0005\u001d\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000"+
		"\u009a\u009d\u0001\u0000\u0000\u0000\u009b\u0099\u0001\u0000\u0000\u0000"+
		"\u009b\u009c\u0001\u0000\u0000\u0000\u009c\u001d\u0001\u0000\u0000\u0000"+
		"\u009d\u009b\u0001\u0000\u0000\u0000\u009e\u009f\u0005\u0015\u0000\u0000"+
		"\u009f\u00a0\u0005\u0019\u0000\u0000\u00a0\u00a1\u0005\u0013\u0000\u0000"+
		"\u00a1\u00a6\u0005\u001b\u0000\u0000\u00a2\u00a5\u0003 \u0010\u0000\u00a3"+
		"\u00a5\u0005\u0015\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a9\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9"+
		"\u00aa\u0005\u001c\u0000\u0000\u00aa\u001f\u0001\u0000\u0000\u0000\u00ab"+
		"\u00b9\u0003\"\u0011\u0000\u00ac\u00b9\u0003$\u0012\u0000\u00ad\u00b9"+
		"\u0003&\u0013\u0000\u00ae\u00b9\u0003(\u0014\u0000\u00af\u00b9\u00034"+
		"\u001a\u0000\u00b0\u00b9\u0003*\u0015\u0000\u00b1\u00b9\u0003,\u0016\u0000"+
		"\u00b2\u00b9\u0003.\u0017\u0000\u00b3\u00b9\u00030\u0018\u0000\u00b4\u00b9"+
		"\u00032\u0019\u0000\u00b5\u00b9\u00036\u001b\u0000\u00b6\u00b9\u00038"+
		"\u001c\u0000\u00b7\u00b9\u0003:\u001d\u0000\u00b8\u00ab\u0001\u0000\u0000"+
		"\u0000\u00b8\u00ac\u0001\u0000\u0000\u0000\u00b8\u00ad\u0001\u0000\u0000"+
		"\u0000\u00b8\u00ae\u0001\u0000\u0000\u0000\u00b8\u00af\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b0\u0001\u0000\u0000\u0000\u00b8\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b2\u0001\u0000\u0000\u0000\u00b8\u00b3\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b4\u0001\u0000\u0000\u0000\u00b8\u00b5\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b8\u00b7\u0001\u0000\u0000"+
		"\u0000\u00b9!\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005\f\u0000\u0000"+
		"\u00bb\u00bc\u0005\u0018\u0000\u0000\u00bc\u00bf\u0005\u0015\u0000\u0000"+
		"\u00bd\u00be\u0005\u0010\u0000\u0000\u00be\u00c0\u0005\u001d\u0000\u0000"+
		"\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000"+
		"\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005\u001a\u0000\u0000"+
		"\u00c2#\u0001\u0000\u0000\u0000\u00c3\u00c4\u0005\f\u0000\u0000\u00c4"+
		"\u00c5\u0005\u0018\u0000\u0000\u00c5\u00c8\u0003\u0012\t\u0000\u00c6\u00c7"+
		"\u0005\u0010\u0000\u0000\u00c7\u00c9\u0005\u001d\u0000\u0000\u00c8\u00c6"+
		"\u0001\u0000\u0000\u0000\u00c8\u00c9\u0001\u0000\u0000\u0000\u00c9\u00ca"+
		"\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005\u001a\u0000\u0000\u00cb%\u0001"+
		"\u0000\u0000\u0000\u00cc\u00cd\u0005\t\u0000\u0000\u00cd\u00ce\u0005\u0018"+
		"\u0000\u0000\u00ce\u00d1\u0005\u0015\u0000\u0000\u00cf\u00d0\u0005\u0010"+
		"\u0000\u0000\u00d0\u00d2\u0003<\u001e\u0000\u00d1\u00cf\u0001\u0000\u0000"+
		"\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000"+
		"\u0000\u00d3\u00d4\u0005\u001a\u0000\u0000\u00d4\'\u0001\u0000\u0000\u0000"+
		"\u00d5\u00d6\u0005\t\u0000\u0000\u00d6\u00d7\u0005\u0018\u0000\u0000\u00d7"+
		"\u00da\u0003\u0012\t\u0000\u00d8\u00d9\u0005\u0010\u0000\u0000\u00d9\u00db"+
		"\u0003<\u001e\u0000\u00da\u00d8\u0001\u0000\u0000\u0000\u00da\u00db\u0001"+
		"\u0000\u0000\u0000\u00db\u00dc\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005"+
		"\u001a\u0000\u0000\u00dd)\u0001\u0000\u0000\u0000\u00de\u00df\u0005\u0007"+
		"\u0000\u0000\u00df\u00e0\u0005\u0018\u0000\u0000\u00e0\u00e3\u0005\u0015"+
		"\u0000\u0000\u00e1\u00e2\u0005\u0010\u0000\u0000\u00e2\u00e4\u0003<\u001e"+
		"\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e5\u0001\u0000\u0000\u0000\u00e5\u00e6\u0005\u001a\u0000"+
		"\u0000\u00e6+\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\u0007\u0000\u0000"+
		"\u00e8\u00e9\u0005\u0018\u0000\u0000\u00e9\u00ec\u0003\u0012\t\u0000\u00ea"+
		"\u00eb\u0005\u0010\u0000\u0000\u00eb\u00ed\u0003<\u001e\u0000\u00ec\u00ea"+
		"\u0001\u0000\u0000\u0000\u00ec\u00ed\u0001\u0000\u0000\u0000\u00ed\u00ee"+
		"\u0001\u0000\u0000\u0000\u00ee\u00ef\u0005\u001a\u0000\u0000\u00ef-\u0001"+
		"\u0000\u0000\u0000\u00f0\u00f1\u0005\b\u0000\u0000\u00f1\u00f2\u0005\u0018"+
		"\u0000\u0000\u00f2\u00f5\u0005\u0015\u0000\u0000\u00f3\u00f4\u0005\u0010"+
		"\u0000\u0000\u00f4\u00f6\u0003<\u001e\u0000\u00f5\u00f3\u0001\u0000\u0000"+
		"\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000\u00f6\u00f7\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f8\u0005\u001a\u0000\u0000\u00f8/\u0001\u0000\u0000\u0000"+
		"\u00f9\u00fa\u0005\b\u0000\u0000\u00fa\u00fb\u0005\u0018\u0000\u0000\u00fb"+
		"\u00fe\u0003\u0012\t\u0000\u00fc\u00fd\u0005\u0010\u0000\u0000\u00fd\u00ff"+
		"\u0003<\u001e\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001"+
		"\u0000\u0000\u0000\u00ff\u0100\u0001\u0000\u0000\u0000\u0100\u0101\u0005"+
		"\u001a\u0000\u0000\u01011\u0001\u0000\u0000\u0000\u0102\u0103\u0005\n"+
		"\u0000\u0000\u0103\u0104\u0005\u0018\u0000\u0000\u0104\u0107\u0005\u0015"+
		"\u0000\u0000\u0105\u0106\u0005\u0010\u0000\u0000\u0106\u0108\u0003<\u001e"+
		"\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001\u0000\u0000"+
		"\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u0109\u010a\u0005\u001a\u0000"+
		"\u0000\u010a3\u0001\u0000\u0000\u0000\u010b\u010c\u0005\n\u0000\u0000"+
		"\u010c\u010d\u0005\u0018\u0000\u0000\u010d\u0110\u0003\u0012\t\u0000\u010e"+
		"\u010f\u0005\u0010\u0000\u0000\u010f\u0111\u0003<\u001e\u0000\u0110\u010e"+
		"\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111\u0112"+
		"\u0001\u0000\u0000\u0000\u0112\u0113\u0005\u001a\u0000\u0000\u01135\u0001"+
		"\u0000\u0000\u0000\u0114\u0115\u0005\u000b\u0000\u0000\u0115\u0116\u0005"+
		"\u0018\u0000\u0000\u0116\u0117\u0005\u0015\u0000\u0000\u0117\u0118\u0005"+
		"\u0010\u0000\u0000\u0118\u011b\u0005\u001d\u0000\u0000\u0119\u011a\u0005"+
		"\u0010\u0000\u0000\u011a\u011c\u0005\u001d\u0000\u0000\u011b\u0119\u0001"+
		"\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011d\u0001"+
		"\u0000\u0000\u0000\u011d\u011e\u0005\u001a\u0000\u0000\u011e7\u0001\u0000"+
		"\u0000\u0000\u011f\u0120\u0005\u0004\u0000\u0000\u0120\u0121\u0005\u0018"+
		"\u0000\u0000\u0121\u0122\u0005\u0016\u0000\u0000\u0122\u0123\u0005\u001a"+
		"\u0000\u0000\u01239\u0001\u0000\u0000\u0000\u0124\u0125\u0005\u0005\u0000"+
		"\u0000\u0125\u0126\u0005\u0018\u0000\u0000\u0126\u0127\u0005\u0016\u0000"+
		"\u0000\u0127\u0128\u0005\u001a\u0000\u0000\u0128;\u0001\u0000\u0000\u0000"+
		"\u0129\u012a\u0007\u0000\u0000\u0000\u012a=\u0001\u0000\u0000\u0000\u012b"+
		"\u012c\u0007\u0001\u0000\u0000\u012c?\u0001\u0000\u0000\u0000\u0015CN"+
		"ry\u0082\u008b\u009b\u00a4\u00a6\u00b8\u00bf\u00c8\u00d1\u00da\u00e3\u00ec"+
		"\u00f5\u00fe\u0107\u0110\u011b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}