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
		WAIT=12, TEXT=13, POSITION=14, REGEX=15, COMMA=16, LABEL=17, USE=18, SEQUENCE=19, 
		DETECTOR=20, ID=21, STRING=22, ESC=23, ORPAR=24, EQ=25, CRPAR=26, OCPAR=27, 
		CCPAR=28, INT=29, FLOAT=30, WS=31;
	public static final int
		RULE_root = 0, RULE_stmt = 1, RULE_createDetector = 2, RULE_useDetector = 3, 
		RULE_createSelectorByPosition = 4, RULE_createSelectorByLabel = 5, RULE_createSelectorByText = 6, 
		RULE_createSelectorByRegex = 7, RULE_createOperation = 8, RULE_selector = 9, 
		RULE_selectorByLabel = 10, RULE_selectorByText = 11, RULE_selectorByRegex = 12, 
		RULE_selectorByPosition = 13, RULE_selectorOrder = 14, RULE_createSequence = 15, 
		RULE_runOperation = 16, RULE_operation = 17, RULE_wait = 18, RULE_waitSelector = 19, 
		RULE_mousePress = 20, RULE_mousePressSelector = 21, RULE_mouseClick = 22, 
		RULE_mouseClickSelector = 23, RULE_mouseDoubleClick = 24, RULE_mouseDoubleClickSelector = 25, 
		RULE_mouseRelease = 26, RULE_mouseReleaseSelector = 27, RULE_mouseScroll = 28, 
		RULE_keyPress = 29, RULE_keyRelease = 30, RULE_mouseButton = 31, RULE_number = 32;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
			"createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
			"createOperation", "selector", "selectorByLabel", "selectorByText", "selectorByRegex", 
			"selectorByPosition", "selectorOrder", "createSequence", "runOperation", 
			"operation", "wait", "waitSelector", "mousePress", "mousePressSelector", 
			"mouseClick", "mouseClickSelector", "mouseDoubleClick", "mouseDoubleClickSelector", 
			"mouseRelease", "mouseReleaseSelector", "mouseScroll", "keyPress", "keyRelease", 
			"mouseButton", "number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'left'", "'right'", "'middle'", "'keyPress'", "'keyRelease'", 
			"'keyType'", "'mouseClick'", "'mouseDoubleClick'", "'mousePress'", "'mouseRelease'", 
			"'mouseScroll'", "'wait'", "'text'", "'position'", "'regex'", "','", 
			"'label'", "'use'", "'sequence'", "'detector'", null, null, null, "'('", 
			"'='", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", "KEY_RELEASE", "KEY_TYPE", 
			"MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", "MOUSE_PRESS", "MOUSE_RELEASE", 
			"MOUSE_SCROLL", "WAIT", "TEXT", "POSITION", "REGEX", "COMMA", "LABEL", 
			"USE", "SEQUENCE", "DETECTOR", "ID", "STRING", "ESC", "ORPAR", "EQ", 
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
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2367408L) != 0)) {
				{
				{
				setState(66);
				stmt();
				}
				}
				setState(71);
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
			setState(81);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				createDetector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				useDetector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(74);
				createSelectorByLabel();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(75);
				createSelectorByText();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(76);
				createSelectorByRegex();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(77);
				createSelectorByPosition();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(78);
				createOperation();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(79);
				createSequence();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(80);
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
			setState(83);
			match(ID);
			setState(84);
			match(EQ);
			setState(85);
			match(DETECTOR);
			setState(86);
			match(ORPAR);
			setState(87);
			match(STRING);
			setState(88);
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
			setState(90);
			match(USE);
			setState(91);
			match(ID);
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ORPAR) {
				{
				setState(92);
				match(ORPAR);
				setState(93);
				match(FLOAT);
				setState(94);
				match(CRPAR);
				}
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
			setState(97);
			match(ID);
			setState(98);
			match(EQ);
			setState(99);
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
			setState(101);
			match(ID);
			setState(102);
			match(EQ);
			setState(103);
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
			setState(105);
			match(ID);
			setState(106);
			match(EQ);
			setState(107);
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
			setState(109);
			match(ID);
			setState(110);
			match(EQ);
			setState(111);
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
	public static class CreateOperationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
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
			setState(113);
			match(ID);
			setState(114);
			match(EQ);
			setState(115);
			operation();
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
			setState(121);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LABEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(117);
				selectorByLabel();
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				selectorByText();
				}
				break;
			case REGEX:
				enterOuterAlt(_localctx, 3);
				{
				setState(119);
				selectorByRegex();
				}
				break;
			case POSITION:
				enterOuterAlt(_localctx, 4);
				{
				setState(120);
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
			setState(123);
			match(LABEL);
			setState(124);
			match(ORPAR);
			setState(125);
			match(STRING);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(126);
				match(COMMA);
				setState(127);
				selectorOrder();
				}
			}

			setState(130);
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
			setState(132);
			match(TEXT);
			setState(133);
			match(ORPAR);
			setState(134);
			match(STRING);
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(135);
				match(COMMA);
				setState(136);
				selectorOrder();
				}
			}

			setState(139);
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
			setState(141);
			match(REGEX);
			setState(142);
			match(ORPAR);
			setState(143);
			match(STRING);
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(144);
				match(COMMA);
				setState(145);
				selectorOrder();
				}
			}

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
			setState(150);
			match(POSITION);
			setState(151);
			match(ORPAR);
			setState(152);
			number();
			setState(153);
			match(COMMA);
			setState(154);
			number();
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
			setState(157);
			match(INT);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(158);
				match(COMMA);
				setState(159);
				match(INT);
				}
				}
				setState(164);
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
	public static class CreateSequenceContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GrammarParser.ID, i);
		}
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode SEQUENCE() { return getToken(GrammarParser.SEQUENCE, 0); }
		public TerminalNode OCPAR() { return getToken(GrammarParser.OCPAR, 0); }
		public TerminalNode CCPAR() { return getToken(GrammarParser.CCPAR, 0); }
		public List<OperationContext> operation() {
			return getRuleContexts(OperationContext.class);
		}
		public OperationContext operation(int i) {
			return getRuleContext(OperationContext.class,i);
		}
		public CreateSequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createSequence; }
	}

	public final CreateSequenceContext createSequence() throws RecognitionException {
		CreateSequenceContext _localctx = new CreateSequenceContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_createSequence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			match(ID);
			setState(166);
			match(EQ);
			setState(167);
			match(SEQUENCE);
			setState(168);
			match(OCPAR);
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2105264L) != 0)) {
				{
				setState(171);
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
					setState(169);
					operation();
					}
					break;
				case ID:
					{
					setState(170);
					match(ID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(176);
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
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public RunOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_runOperation; }
	}

	public final RunOperationContext runOperation() throws RecognitionException {
		RunOperationContext _localctx = new RunOperationContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_runOperation);
		try {
			setState(180);
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
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				operation();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(179);
				match(ID);
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
		public KeyPressContext keyPress() {
			return getRuleContext(KeyPressContext.class,0);
		}
		public KeyReleaseContext keyRelease() {
			return getRuleContext(KeyReleaseContext.class,0);
		}
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_operation);
		try {
			setState(195);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(182);
				wait();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				waitSelector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(184);
				mousePress();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(185);
				mousePressSelector();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(186);
				mouseReleaseSelector();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(187);
				mouseClick();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(188);
				mouseClickSelector();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(189);
				mouseDoubleClick();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(190);
				mouseDoubleClickSelector();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(191);
				mouseRelease();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(192);
				mouseScroll();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(193);
				keyPress();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(194);
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
		enterRule(_localctx, 36, RULE_wait);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(WAIT);
			setState(198);
			match(ORPAR);
			setState(199);
			match(ID);
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(200);
				match(COMMA);
				setState(201);
				match(INT);
				}
			}

			setState(204);
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
		enterRule(_localctx, 38, RULE_waitSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			match(WAIT);
			setState(207);
			match(ORPAR);
			setState(208);
			selector();
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(209);
				match(COMMA);
				setState(210);
				match(INT);
				}
			}

			setState(213);
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
		enterRule(_localctx, 40, RULE_mousePress);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(MOUSE_PRESS);
			setState(216);
			match(ORPAR);
			setState(217);
			match(ID);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(218);
				match(COMMA);
				setState(219);
				mouseButton();
				}
			}

			setState(222);
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
		enterRule(_localctx, 42, RULE_mousePressSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(MOUSE_PRESS);
			setState(225);
			match(ORPAR);
			setState(226);
			selector();
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(227);
				match(COMMA);
				setState(228);
				mouseButton();
				}
			}

			setState(231);
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
		enterRule(_localctx, 44, RULE_mouseClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(MOUSE_CLICK);
			setState(234);
			match(ORPAR);
			setState(235);
			match(ID);
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(236);
				match(COMMA);
				setState(237);
				mouseButton();
				}
			}

			setState(240);
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
		enterRule(_localctx, 46, RULE_mouseClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(MOUSE_CLICK);
			setState(243);
			match(ORPAR);
			setState(244);
			selector();
			setState(247);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(245);
				match(COMMA);
				setState(246);
				mouseButton();
				}
			}

			setState(249);
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
		enterRule(_localctx, 48, RULE_mouseDoubleClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(MOUSE_DOUBLE_CLICK);
			setState(252);
			match(ORPAR);
			setState(253);
			match(ID);
			setState(256);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(254);
				match(COMMA);
				setState(255);
				mouseButton();
				}
			}

			setState(258);
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
		enterRule(_localctx, 50, RULE_mouseDoubleClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(MOUSE_DOUBLE_CLICK);
			setState(261);
			match(ORPAR);
			setState(262);
			selector();
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(263);
				match(COMMA);
				setState(264);
				mouseButton();
				}
			}

			setState(267);
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
		enterRule(_localctx, 52, RULE_mouseRelease);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			match(MOUSE_RELEASE);
			setState(270);
			match(ORPAR);
			setState(271);
			match(ID);
			setState(274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(272);
				match(COMMA);
				setState(273);
				mouseButton();
				}
			}

			setState(276);
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
		enterRule(_localctx, 54, RULE_mouseReleaseSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			match(MOUSE_RELEASE);
			setState(279);
			match(ORPAR);
			setState(280);
			selector();
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(281);
				match(COMMA);
				setState(282);
				mouseButton();
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
		enterRule(_localctx, 56, RULE_mouseScroll);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			match(MOUSE_SCROLL);
			setState(288);
			match(ORPAR);
			setState(289);
			match(ID);
			setState(290);
			match(COMMA);
			setState(291);
			match(INT);
			setState(294);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(292);
				match(COMMA);
				setState(293);
				match(INT);
				}
			}

			setState(296);
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
		enterRule(_localctx, 58, RULE_keyPress);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			match(KEY_PRESS);
			setState(299);
			match(ORPAR);
			setState(300);
			match(STRING);
			setState(301);
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
		enterRule(_localctx, 60, RULE_keyRelease);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			match(KEY_RELEASE);
			setState(304);
			match(ORPAR);
			setState(305);
			match(STRING);
			setState(306);
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
		enterRule(_localctx, 62, RULE_mouseButton);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
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
		enterRule(_localctx, 64, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
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
		"\u0004\u0001\u001f\u0139\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0005\u0000D"+
		"\b\u0000\n\u0000\f\u0000G\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001R\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003`\b\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\tz\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u0081\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000b\u008a\b\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u0093\b\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0005\u000e\u00a1\b\u000e\n\u000e\f\u000e\u00a4"+
		"\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0005\u000f\u00ac\b\u000f\n\u000f\f\u000f\u00af\t\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0003\u0010\u00b5\b\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0003\u0011\u00c4\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0003\u0012\u00cb\b\u0012\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00d4\b\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u00dd\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00e6\b\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0003\u0016\u00ef\b\u0016\u0001\u0016\u0001\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00f8\b\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0003\u0018\u0101\b\u0018\u0001\u0018\u0001\u0018\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u010a\b\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0003\u001a\u0113\b\u001a\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u011c\b\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u0127\b\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0001\u001f\u0001 \u0001 \u0001 \u0000\u0000!\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"02468:<>@\u0000\u0002\u0001\u0000\u0001\u0003\u0001\u0000\u001d\u001e"+
		"\u0142\u0000E\u0001\u0000\u0000\u0000\u0002Q\u0001\u0000\u0000\u0000\u0004"+
		"S\u0001\u0000\u0000\u0000\u0006Z\u0001\u0000\u0000\u0000\ba\u0001\u0000"+
		"\u0000\u0000\ne\u0001\u0000\u0000\u0000\fi\u0001\u0000\u0000\u0000\u000e"+
		"m\u0001\u0000\u0000\u0000\u0010q\u0001\u0000\u0000\u0000\u0012y\u0001"+
		"\u0000\u0000\u0000\u0014{\u0001\u0000\u0000\u0000\u0016\u0084\u0001\u0000"+
		"\u0000\u0000\u0018\u008d\u0001\u0000\u0000\u0000\u001a\u0096\u0001\u0000"+
		"\u0000\u0000\u001c\u009d\u0001\u0000\u0000\u0000\u001e\u00a5\u0001\u0000"+
		"\u0000\u0000 \u00b4\u0001\u0000\u0000\u0000\"\u00c3\u0001\u0000\u0000"+
		"\u0000$\u00c5\u0001\u0000\u0000\u0000&\u00ce\u0001\u0000\u0000\u0000("+
		"\u00d7\u0001\u0000\u0000\u0000*\u00e0\u0001\u0000\u0000\u0000,\u00e9\u0001"+
		"\u0000\u0000\u0000.\u00f2\u0001\u0000\u0000\u00000\u00fb\u0001\u0000\u0000"+
		"\u00002\u0104\u0001\u0000\u0000\u00004\u010d\u0001\u0000\u0000\u00006"+
		"\u0116\u0001\u0000\u0000\u00008\u011f\u0001\u0000\u0000\u0000:\u012a\u0001"+
		"\u0000\u0000\u0000<\u012f\u0001\u0000\u0000\u0000>\u0134\u0001\u0000\u0000"+
		"\u0000@\u0136\u0001\u0000\u0000\u0000BD\u0003\u0002\u0001\u0000CB\u0001"+
		"\u0000\u0000\u0000DG\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000"+
		"EF\u0001\u0000\u0000\u0000F\u0001\u0001\u0000\u0000\u0000GE\u0001\u0000"+
		"\u0000\u0000HR\u0003\u0004\u0002\u0000IR\u0003\u0006\u0003\u0000JR\u0003"+
		"\n\u0005\u0000KR\u0003\f\u0006\u0000LR\u0003\u000e\u0007\u0000MR\u0003"+
		"\b\u0004\u0000NR\u0003\u0010\b\u0000OR\u0003\u001e\u000f\u0000PR\u0003"+
		" \u0010\u0000QH\u0001\u0000\u0000\u0000QI\u0001\u0000\u0000\u0000QJ\u0001"+
		"\u0000\u0000\u0000QK\u0001\u0000\u0000\u0000QL\u0001\u0000\u0000\u0000"+
		"QM\u0001\u0000\u0000\u0000QN\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000QP\u0001\u0000\u0000\u0000R\u0003\u0001\u0000\u0000\u0000ST\u0005"+
		"\u0015\u0000\u0000TU\u0005\u0019\u0000\u0000UV\u0005\u0014\u0000\u0000"+
		"VW\u0005\u0018\u0000\u0000WX\u0005\u0016\u0000\u0000XY\u0005\u001a\u0000"+
		"\u0000Y\u0005\u0001\u0000\u0000\u0000Z[\u0005\u0012\u0000\u0000[_\u0005"+
		"\u0015\u0000\u0000\\]\u0005\u0018\u0000\u0000]^\u0005\u001e\u0000\u0000"+
		"^`\u0005\u001a\u0000\u0000_\\\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000"+
		"\u0000`\u0007\u0001\u0000\u0000\u0000ab\u0005\u0015\u0000\u0000bc\u0005"+
		"\u0019\u0000\u0000cd\u0003\u001a\r\u0000d\t\u0001\u0000\u0000\u0000ef"+
		"\u0005\u0015\u0000\u0000fg\u0005\u0019\u0000\u0000gh\u0003\u0014\n\u0000"+
		"h\u000b\u0001\u0000\u0000\u0000ij\u0005\u0015\u0000\u0000jk\u0005\u0019"+
		"\u0000\u0000kl\u0003\u0016\u000b\u0000l\r\u0001\u0000\u0000\u0000mn\u0005"+
		"\u0015\u0000\u0000no\u0005\u0019\u0000\u0000op\u0003\u0018\f\u0000p\u000f"+
		"\u0001\u0000\u0000\u0000qr\u0005\u0015\u0000\u0000rs\u0005\u0019\u0000"+
		"\u0000st\u0003\"\u0011\u0000t\u0011\u0001\u0000\u0000\u0000uz\u0003\u0014"+
		"\n\u0000vz\u0003\u0016\u000b\u0000wz\u0003\u0018\f\u0000xz\u0003\u001a"+
		"\r\u0000yu\u0001\u0000\u0000\u0000yv\u0001\u0000\u0000\u0000yw\u0001\u0000"+
		"\u0000\u0000yx\u0001\u0000\u0000\u0000z\u0013\u0001\u0000\u0000\u0000"+
		"{|\u0005\u0011\u0000\u0000|}\u0005\u0018\u0000\u0000}\u0080\u0005\u0016"+
		"\u0000\u0000~\u007f\u0005\u0010\u0000\u0000\u007f\u0081\u0003\u001c\u000e"+
		"\u0000\u0080~\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000"+
		"\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0083\u0005\u001a\u0000\u0000"+
		"\u0083\u0015\u0001\u0000\u0000\u0000\u0084\u0085\u0005\r\u0000\u0000\u0085"+
		"\u0086\u0005\u0018\u0000\u0000\u0086\u0089\u0005\u0016\u0000\u0000\u0087"+
		"\u0088\u0005\u0010\u0000\u0000\u0088\u008a\u0003\u001c\u000e\u0000\u0089"+
		"\u0087\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u001a\u0000\u0000\u008c"+
		"\u0017\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u000f\u0000\u0000\u008e"+
		"\u008f\u0005\u0018\u0000\u0000\u008f\u0092\u0005\u0016\u0000\u0000\u0090"+
		"\u0091\u0005\u0010\u0000\u0000\u0091\u0093\u0003\u001c\u000e\u0000\u0092"+
		"\u0090\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093"+
		"\u0094\u0001\u0000\u0000\u0000\u0094\u0095\u0005\u001a\u0000\u0000\u0095"+
		"\u0019\u0001\u0000\u0000\u0000\u0096\u0097\u0005\u000e\u0000\u0000\u0097"+
		"\u0098\u0005\u0018\u0000\u0000\u0098\u0099\u0003@ \u0000\u0099\u009a\u0005"+
		"\u0010\u0000\u0000\u009a\u009b\u0003@ \u0000\u009b\u009c\u0005\u001a\u0000"+
		"\u0000\u009c\u001b\u0001\u0000\u0000\u0000\u009d\u00a2\u0005\u001d\u0000"+
		"\u0000\u009e\u009f\u0005\u0010\u0000\u0000\u009f\u00a1\u0005\u001d\u0000"+
		"\u0000\u00a0\u009e\u0001\u0000\u0000\u0000\u00a1\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a3\u001d\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a6\u0005\u0015\u0000\u0000\u00a6\u00a7\u0005\u0019\u0000"+
		"\u0000\u00a7\u00a8\u0005\u0013\u0000\u0000\u00a8\u00ad\u0005\u001b\u0000"+
		"\u0000\u00a9\u00ac\u0003\"\u0011\u0000\u00aa\u00ac\u0005\u0015\u0000\u0000"+
		"\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ac\u00af\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00b0\u0001\u0000\u0000\u0000"+
		"\u00af\u00ad\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005\u001c\u0000\u0000"+
		"\u00b1\u001f\u0001\u0000\u0000\u0000\u00b2\u00b5\u0003\"\u0011\u0000\u00b3"+
		"\u00b5\u0005\u0015\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000\u00b4"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b5!\u0001\u0000\u0000\u0000\u00b6\u00c4"+
		"\u0003$\u0012\u0000\u00b7\u00c4\u0003&\u0013\u0000\u00b8\u00c4\u0003("+
		"\u0014\u0000\u00b9\u00c4\u0003*\u0015\u0000\u00ba\u00c4\u00036\u001b\u0000"+
		"\u00bb\u00c4\u0003,\u0016\u0000\u00bc\u00c4\u0003.\u0017\u0000\u00bd\u00c4"+
		"\u00030\u0018\u0000\u00be\u00c4\u00032\u0019\u0000\u00bf\u00c4\u00034"+
		"\u001a\u0000\u00c0\u00c4\u00038\u001c\u0000\u00c1\u00c4\u0003:\u001d\u0000"+
		"\u00c2\u00c4\u0003<\u001e\u0000\u00c3\u00b6\u0001\u0000\u0000\u0000\u00c3"+
		"\u00b7\u0001\u0000\u0000\u0000\u00c3\u00b8\u0001\u0000\u0000\u0000\u00c3"+
		"\u00b9\u0001\u0000\u0000\u0000\u00c3\u00ba\u0001\u0000\u0000\u0000\u00c3"+
		"\u00bb\u0001\u0000\u0000\u0000\u00c3\u00bc\u0001\u0000\u0000\u0000\u00c3"+
		"\u00bd\u0001\u0000\u0000\u0000\u00c3\u00be\u0001\u0000\u0000\u0000\u00c3"+
		"\u00bf\u0001\u0000\u0000\u0000\u00c3\u00c0\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c3\u00c2\u0001\u0000\u0000\u0000\u00c4"+
		"#\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\f\u0000\u0000\u00c6\u00c7"+
		"\u0005\u0018\u0000\u0000\u00c7\u00ca\u0005\u0015\u0000\u0000\u00c8\u00c9"+
		"\u0005\u0010\u0000\u0000\u00c9\u00cb\u0005\u001d\u0000\u0000\u00ca\u00c8"+
		"\u0001\u0000\u0000\u0000\u00ca\u00cb\u0001\u0000\u0000\u0000\u00cb\u00cc"+
		"\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005\u001a\u0000\u0000\u00cd%\u0001"+
		"\u0000\u0000\u0000\u00ce\u00cf\u0005\f\u0000\u0000\u00cf\u00d0\u0005\u0018"+
		"\u0000\u0000\u00d0\u00d3\u0003\u0012\t\u0000\u00d1\u00d2\u0005\u0010\u0000"+
		"\u0000\u00d2\u00d4\u0005\u001d\u0000\u0000\u00d3\u00d1\u0001\u0000\u0000"+
		"\u0000\u00d3\u00d4\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000"+
		"\u0000\u00d5\u00d6\u0005\u001a\u0000\u0000\u00d6\'\u0001\u0000\u0000\u0000"+
		"\u00d7\u00d8\u0005\t\u0000\u0000\u00d8\u00d9\u0005\u0018\u0000\u0000\u00d9"+
		"\u00dc\u0005\u0015\u0000\u0000\u00da\u00db\u0005\u0010\u0000\u0000\u00db"+
		"\u00dd\u0003>\u001f\u0000\u00dc\u00da\u0001\u0000\u0000\u0000\u00dc\u00dd"+
		"\u0001\u0000\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00df"+
		"\u0005\u001a\u0000\u0000\u00df)\u0001\u0000\u0000\u0000\u00e0\u00e1\u0005"+
		"\t\u0000\u0000\u00e1\u00e2\u0005\u0018\u0000\u0000\u00e2\u00e5\u0003\u0012"+
		"\t\u0000\u00e3\u00e4\u0005\u0010\u0000\u0000\u00e4\u00e6\u0003>\u001f"+
		"\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e7\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\u001a\u0000"+
		"\u0000\u00e8+\u0001\u0000\u0000\u0000\u00e9\u00ea\u0005\u0007\u0000\u0000"+
		"\u00ea\u00eb\u0005\u0018\u0000\u0000\u00eb\u00ee\u0005\u0015\u0000\u0000"+
		"\u00ec\u00ed\u0005\u0010\u0000\u0000\u00ed\u00ef\u0003>\u001f\u0000\u00ee"+
		"\u00ec\u0001\u0000\u0000\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef"+
		"\u00f0\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005\u001a\u0000\u0000\u00f1"+
		"-\u0001\u0000\u0000\u0000\u00f2\u00f3\u0005\u0007\u0000\u0000\u00f3\u00f4"+
		"\u0005\u0018\u0000\u0000\u00f4\u00f7\u0003\u0012\t\u0000\u00f5\u00f6\u0005"+
		"\u0010\u0000\u0000\u00f6\u00f8\u0003>\u001f\u0000\u00f7\u00f5\u0001\u0000"+
		"\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001\u0000"+
		"\u0000\u0000\u00f9\u00fa\u0005\u001a\u0000\u0000\u00fa/\u0001\u0000\u0000"+
		"\u0000\u00fb\u00fc\u0005\b\u0000\u0000\u00fc\u00fd\u0005\u0018\u0000\u0000"+
		"\u00fd\u0100\u0005\u0015\u0000\u0000\u00fe\u00ff\u0005\u0010\u0000\u0000"+
		"\u00ff\u0101\u0003>\u001f\u0000\u0100\u00fe\u0001\u0000\u0000\u0000\u0100"+
		"\u0101\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000\u0000\u0102"+
		"\u0103\u0005\u001a\u0000\u0000\u01031\u0001\u0000\u0000\u0000\u0104\u0105"+
		"\u0005\b\u0000\u0000\u0105\u0106\u0005\u0018\u0000\u0000\u0106\u0109\u0003"+
		"\u0012\t\u0000\u0107\u0108\u0005\u0010\u0000\u0000\u0108\u010a\u0003>"+
		"\u001f\u0000\u0109\u0107\u0001\u0000\u0000\u0000\u0109\u010a\u0001\u0000"+
		"\u0000\u0000\u010a\u010b\u0001\u0000\u0000\u0000\u010b\u010c\u0005\u001a"+
		"\u0000\u0000\u010c3\u0001\u0000\u0000\u0000\u010d\u010e\u0005\n\u0000"+
		"\u0000\u010e\u010f\u0005\u0018\u0000\u0000\u010f\u0112\u0005\u0015\u0000"+
		"\u0000\u0110\u0111\u0005\u0010\u0000\u0000\u0111\u0113\u0003>\u001f\u0000"+
		"\u0112\u0110\u0001\u0000\u0000\u0000\u0112\u0113\u0001\u0000\u0000\u0000"+
		"\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0115\u0005\u001a\u0000\u0000"+
		"\u01155\u0001\u0000\u0000\u0000\u0116\u0117\u0005\n\u0000\u0000\u0117"+
		"\u0118\u0005\u0018\u0000\u0000\u0118\u011b\u0003\u0012\t\u0000\u0119\u011a"+
		"\u0005\u0010\u0000\u0000\u011a\u011c\u0003>\u001f\u0000\u011b\u0119\u0001"+
		"\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011d\u0001"+
		"\u0000\u0000\u0000\u011d\u011e\u0005\u001a\u0000\u0000\u011e7\u0001\u0000"+
		"\u0000\u0000\u011f\u0120\u0005\u000b\u0000\u0000\u0120\u0121\u0005\u0018"+
		"\u0000\u0000\u0121\u0122\u0005\u0015\u0000\u0000\u0122\u0123\u0005\u0010"+
		"\u0000\u0000\u0123\u0126\u0005\u001d\u0000\u0000\u0124\u0125\u0005\u0010"+
		"\u0000\u0000\u0125\u0127\u0005\u001d\u0000\u0000\u0126\u0124\u0001\u0000"+
		"\u0000\u0000\u0126\u0127\u0001\u0000\u0000\u0000\u0127\u0128\u0001\u0000"+
		"\u0000\u0000\u0128\u0129\u0005\u001a\u0000\u0000\u01299\u0001\u0000\u0000"+
		"\u0000\u012a\u012b\u0005\u0004\u0000\u0000\u012b\u012c\u0005\u0018\u0000"+
		"\u0000\u012c\u012d\u0005\u0016\u0000\u0000\u012d\u012e\u0005\u001a\u0000"+
		"\u0000\u012e;\u0001\u0000\u0000\u0000\u012f\u0130\u0005\u0005\u0000\u0000"+
		"\u0130\u0131\u0005\u0018\u0000\u0000\u0131\u0132\u0005\u0016\u0000\u0000"+
		"\u0132\u0133\u0005\u001a\u0000\u0000\u0133=\u0001\u0000\u0000\u0000\u0134"+
		"\u0135\u0007\u0000\u0000\u0000\u0135?\u0001\u0000\u0000\u0000\u0136\u0137"+
		"\u0007\u0001\u0000\u0000\u0137A\u0001\u0000\u0000\u0000\u0017EQ_y\u0080"+
		"\u0089\u0092\u00a2\u00ab\u00ad\u00b4\u00c3\u00ca\u00d3\u00dc\u00e5\u00ee"+
		"\u00f7\u0100\u0109\u0112\u011b\u0126";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}