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
		LEFT=1, RIGHT=2, MIDDLE=3, KEY_PRESS=4, KEY_TYPE=5, KEY_RELEASE=6, MOUSE_CLICK=7, 
		MOUSE_DOUBLE_CLICK=8, MOUSE_PRESS=9, MOUSE_RELEASE=10, MOUSE_SCROLL=11, 
		WAIT=12, TEXT=13, POSITION=14, REGEX=15, COMMA=16, DCOMMA=17, LABEL=18, 
		USE=19, SEQUENCE=20, DETECTOR=21, ID=22, STRING=23, ESC=24, ORPAR=25, 
		EQ=26, CRPAR=27, OCPAR=28, CCPAR=29, INT=30, FLOAT=31, WS=32;
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
		RULE_mouseScrollSelector = 29, RULE_keyPress = 30, RULE_keyRelease = 31, 
		RULE_keyType = 32, RULE_keyPressSelector = 33, RULE_keyReleaseSelector = 34, 
		RULE_keyTypeSelector = 35, RULE_mouseButton = 36, RULE_number = 37;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "stmt", "createDetector", "useDetector", "createSelectorByPosition", 
			"createSelectorByLabel", "createSelectorByText", "createSelectorByRegex", 
			"createOperation", "selector", "selectorByLabel", "selectorByText", "selectorByRegex", 
			"selectorByPosition", "selectorOrder", "createSequence", "runOperation", 
			"operation", "wait", "waitSelector", "mousePress", "mousePressSelector", 
			"mouseClick", "mouseClickSelector", "mouseDoubleClick", "mouseDoubleClickSelector", 
			"mouseRelease", "mouseReleaseSelector", "mouseScroll", "mouseScrollSelector", 
			"keyPress", "keyRelease", "keyType", "keyPressSelector", "keyReleaseSelector", 
			"keyTypeSelector", "mouseButton", "number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'left'", "'right'", "'middle'", "'keyPress'", "'keyType'", "'keyRelease'", 
			"'mouseClick'", "'mouseDoubleClick'", "'mousePress'", "'mouseRelease'", 
			"'mouseScroll'", "'wait'", "'text'", "'position'", "'regex'", "','", 
			"';'", "'label'", "'use'", "'sequence'", "'detector'", null, null, null, 
			"'('", "'='", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEFT", "RIGHT", "MIDDLE", "KEY_PRESS", "KEY_TYPE", "KEY_RELEASE", 
			"MOUSE_CLICK", "MOUSE_DOUBLE_CLICK", "MOUSE_PRESS", "MOUSE_RELEASE", 
			"MOUSE_SCROLL", "WAIT", "TEXT", "POSITION", "REGEX", "COMMA", "DCOMMA", 
			"LABEL", "USE", "SEQUENCE", "DETECTOR", "ID", "STRING", "ESC", "ORPAR", 
			"EQ", "CRPAR", "OCPAR", "CCPAR", "INT", "FLOAT", "WS"
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
			setState(79);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4726768L) != 0)) {
				{
				{
				setState(76);
				stmt();
				}
				}
				setState(81);
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
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				createDetector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				useDetector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(84);
				createSelectorByLabel();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(85);
				createSelectorByText();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(86);
				createSelectorByRegex();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(87);
				createSelectorByPosition();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(88);
				createOperation();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(89);
				createSequence();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(90);
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
			setState(93);
			match(ID);
			setState(94);
			match(EQ);
			setState(95);
			match(DETECTOR);
			setState(96);
			match(ORPAR);
			setState(97);
			match(STRING);
			setState(98);
			match(CRPAR);
			setState(99);
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
			setState(101);
			match(USE);
			setState(102);
			match(ID);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ORPAR) {
				{
				setState(103);
				match(ORPAR);
				setState(104);
				match(FLOAT);
				setState(105);
				match(CRPAR);
				}
			}

			setState(108);
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
			setState(110);
			match(ID);
			setState(111);
			match(EQ);
			setState(112);
			selectorByPosition();
			setState(113);
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
			setState(115);
			match(ID);
			setState(116);
			match(EQ);
			setState(117);
			selectorByLabel();
			setState(118);
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
			setState(120);
			match(ID);
			setState(121);
			match(EQ);
			setState(122);
			selectorByText();
			setState(123);
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
			setState(125);
			match(ID);
			setState(126);
			match(EQ);
			setState(127);
			selectorByRegex();
			setState(128);
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
			setState(130);
			match(ID);
			setState(131);
			match(EQ);
			setState(132);
			operation();
			setState(133);
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
		public SelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selector; }
	}

	public final SelectorContext selector() throws RecognitionException {
		SelectorContext _localctx = new SelectorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_selector);
		try {
			setState(139);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LABEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				selectorByLabel();
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				selectorByText();
				}
				break;
			case REGEX:
				enterOuterAlt(_localctx, 3);
				{
				setState(137);
				selectorByRegex();
				}
				break;
			case POSITION:
				enterOuterAlt(_localctx, 4);
				{
				setState(138);
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
			setState(141);
			match(LABEL);
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
			setState(150);
			match(TEXT);
			setState(151);
			match(ORPAR);
			setState(152);
			match(STRING);
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(153);
				match(COMMA);
				setState(154);
				selectorOrder();
				}
			}

			setState(157);
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
			setState(159);
			match(REGEX);
			setState(160);
			match(ORPAR);
			setState(161);
			match(STRING);
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(162);
				match(COMMA);
				setState(163);
				selectorOrder();
				}
			}

			setState(166);
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
			setState(168);
			match(POSITION);
			setState(169);
			match(ORPAR);
			setState(170);
			number();
			setState(171);
			match(COMMA);
			setState(172);
			number();
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
			setState(175);
			match(INT);
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(176);
				match(COMMA);
				setState(177);
				match(INT);
				}
				}
				setState(182);
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
		enterRule(_localctx, 30, RULE_createSequence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(ID);
			setState(184);
			match(EQ);
			setState(185);
			match(SEQUENCE);
			setState(186);
			match(OCPAR);
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4726768L) != 0)) {
				{
				{
				setState(187);
				stmt();
				}
				}
				setState(192);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(193);
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
		enterRule(_localctx, 32, RULE_runOperation);
		try {
			setState(200);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY_PRESS:
			case KEY_TYPE:
			case KEY_RELEASE:
			case MOUSE_CLICK:
			case MOUSE_DOUBLE_CLICK:
			case MOUSE_PRESS:
			case MOUSE_RELEASE:
			case MOUSE_SCROLL:
			case WAIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(195);
				operation();
				setState(196);
				match(DCOMMA);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(198);
				match(ID);
				setState(199);
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
		enterRule(_localctx, 34, RULE_operation);
		try {
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				wait();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(203);
				waitSelector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(204);
				mousePress();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(205);
				mousePressSelector();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(206);
				mouseReleaseSelector();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(207);
				mouseClick();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(208);
				mouseClickSelector();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(209);
				mouseDoubleClick();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(210);
				mouseDoubleClickSelector();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(211);
				mouseRelease();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(212);
				mouseScroll();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(213);
				mouseScrollSelector();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(214);
				keyPress();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(215);
				keyRelease();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(216);
				keyType();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(217);
				keyPressSelector();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(218);
				keyReleaseSelector();
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(219);
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
		enterRule(_localctx, 36, RULE_wait);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(WAIT);
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
				match(INT);
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
			setState(231);
			match(WAIT);
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
				match(INT);
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
			setState(240);
			match(MOUSE_PRESS);
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
			setState(249);
			match(MOUSE_PRESS);
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
			setState(258);
			match(MOUSE_CLICK);
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
			setState(267);
			match(MOUSE_CLICK);
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
			setState(276);
			match(MOUSE_DOUBLE_CLICK);
			setState(277);
			match(ORPAR);
			setState(278);
			match(ID);
			setState(281);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(279);
				match(COMMA);
				setState(280);
				mouseButton();
				}
			}

			setState(283);
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
			setState(285);
			match(MOUSE_DOUBLE_CLICK);
			setState(286);
			match(ORPAR);
			setState(287);
			selector();
			setState(290);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(288);
				match(COMMA);
				setState(289);
				mouseButton();
				}
			}

			setState(292);
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
			setState(294);
			match(MOUSE_RELEASE);
			setState(295);
			match(ORPAR);
			setState(296);
			match(ID);
			setState(299);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(297);
				match(COMMA);
				setState(298);
				mouseButton();
				}
			}

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
			setState(303);
			match(MOUSE_RELEASE);
			setState(304);
			match(ORPAR);
			setState(305);
			selector();
			setState(308);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(306);
				match(COMMA);
				setState(307);
				mouseButton();
				}
			}

			setState(310);
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
			setState(312);
			match(MOUSE_SCROLL);
			setState(313);
			match(ORPAR);
			setState(314);
			match(ID);
			setState(315);
			match(COMMA);
			setState(316);
			match(INT);
			setState(319);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(317);
				match(COMMA);
				setState(318);
				match(INT);
				}
			}

			setState(321);
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
		enterRule(_localctx, 58, RULE_mouseScrollSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(323);
			match(MOUSE_SCROLL);
			setState(324);
			match(ORPAR);
			setState(325);
			selector();
			setState(326);
			match(COMMA);
			setState(327);
			match(INT);
			setState(330);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(328);
				match(COMMA);
				setState(329);
				match(INT);
				}
			}

			setState(332);
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
		enterRule(_localctx, 60, RULE_keyPress);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			match(KEY_PRESS);
			setState(335);
			match(ORPAR);
			setState(336);
			match(ID);
			setState(337);
			match(COMMA);
			setState(338);
			match(STRING);
			setState(339);
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
		enterRule(_localctx, 62, RULE_keyRelease);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			match(KEY_RELEASE);
			setState(342);
			match(ORPAR);
			setState(343);
			match(ID);
			setState(344);
			match(COMMA);
			setState(345);
			match(STRING);
			setState(346);
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
		enterRule(_localctx, 64, RULE_keyType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(KEY_TYPE);
			setState(349);
			match(ORPAR);
			setState(350);
			match(ID);
			setState(351);
			match(COMMA);
			setState(352);
			match(STRING);
			setState(353);
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
		enterRule(_localctx, 66, RULE_keyPressSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			match(KEY_PRESS);
			setState(356);
			match(ORPAR);
			setState(357);
			selector();
			setState(358);
			match(COMMA);
			setState(359);
			match(STRING);
			setState(360);
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
		enterRule(_localctx, 68, RULE_keyReleaseSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			match(KEY_RELEASE);
			setState(363);
			match(ORPAR);
			setState(364);
			selector();
			setState(365);
			match(COMMA);
			setState(366);
			match(STRING);
			setState(367);
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
		enterRule(_localctx, 70, RULE_keyTypeSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(369);
			match(KEY_TYPE);
			setState(370);
			match(ORPAR);
			setState(371);
			selector();
			setState(372);
			match(COMMA);
			setState(373);
			match(STRING);
			setState(374);
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
		enterRule(_localctx, 72, RULE_mouseButton);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
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
		enterRule(_localctx, 74, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
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
		"\u0004\u0001 \u017d\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0001\u0000\u0005\u0000N\b\u0000"+
		"\n\u0000\f\u0000Q\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\\\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003k\b\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0003\t\u008c\b\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u0093\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u009c\b\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00a5\b\f\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00b3\b\u000e\n\u000e\f\u000e"+
		"\u00b6\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0005\u000f\u00bd\b\u000f\n\u000f\f\u000f\u00c0\t\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003"+
		"\u0010\u00c9\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0003\u0011\u00dd\b\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00e4\b\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003"+
		"\u0013\u00ed\b\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00f6\b\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003"+
		"\u0015\u00ff\b\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0108\b\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003"+
		"\u0017\u0111\b\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u011a\b\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003"+
		"\u0019\u0123\b\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u012c\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003"+
		"\u001b\u0135\b\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u0140"+
		"\b\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u014b\b\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001"+
		" \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001"+
		"%\u0000\u0000&\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJ\u0000\u0002\u0001\u0000"+
		"\u0001\u0003\u0001\u0000\u001e\u001f\u0186\u0000O\u0001\u0000\u0000\u0000"+
		"\u0002[\u0001\u0000\u0000\u0000\u0004]\u0001\u0000\u0000\u0000\u0006e"+
		"\u0001\u0000\u0000\u0000\bn\u0001\u0000\u0000\u0000\ns\u0001\u0000\u0000"+
		"\u0000\fx\u0001\u0000\u0000\u0000\u000e}\u0001\u0000\u0000\u0000\u0010"+
		"\u0082\u0001\u0000\u0000\u0000\u0012\u008b\u0001\u0000\u0000\u0000\u0014"+
		"\u008d\u0001\u0000\u0000\u0000\u0016\u0096\u0001\u0000\u0000\u0000\u0018"+
		"\u009f\u0001\u0000\u0000\u0000\u001a\u00a8\u0001\u0000\u0000\u0000\u001c"+
		"\u00af\u0001\u0000\u0000\u0000\u001e\u00b7\u0001\u0000\u0000\u0000 \u00c8"+
		"\u0001\u0000\u0000\u0000\"\u00dc\u0001\u0000\u0000\u0000$\u00de\u0001"+
		"\u0000\u0000\u0000&\u00e7\u0001\u0000\u0000\u0000(\u00f0\u0001\u0000\u0000"+
		"\u0000*\u00f9\u0001\u0000\u0000\u0000,\u0102\u0001\u0000\u0000\u0000."+
		"\u010b\u0001\u0000\u0000\u00000\u0114\u0001\u0000\u0000\u00002\u011d\u0001"+
		"\u0000\u0000\u00004\u0126\u0001\u0000\u0000\u00006\u012f\u0001\u0000\u0000"+
		"\u00008\u0138\u0001\u0000\u0000\u0000:\u0143\u0001\u0000\u0000\u0000<"+
		"\u014e\u0001\u0000\u0000\u0000>\u0155\u0001\u0000\u0000\u0000@\u015c\u0001"+
		"\u0000\u0000\u0000B\u0163\u0001\u0000\u0000\u0000D\u016a\u0001\u0000\u0000"+
		"\u0000F\u0171\u0001\u0000\u0000\u0000H\u0178\u0001\u0000\u0000\u0000J"+
		"\u017a\u0001\u0000\u0000\u0000LN\u0003\u0002\u0001\u0000ML\u0001\u0000"+
		"\u0000\u0000NQ\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001"+
		"\u0000\u0000\u0000P\u0001\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000R\\\u0003\u0004\u0002\u0000S\\\u0003\u0006\u0003\u0000T\\\u0003"+
		"\n\u0005\u0000U\\\u0003\f\u0006\u0000V\\\u0003\u000e\u0007\u0000W\\\u0003"+
		"\b\u0004\u0000X\\\u0003\u0010\b\u0000Y\\\u0003\u001e\u000f\u0000Z\\\u0003"+
		" \u0010\u0000[R\u0001\u0000\u0000\u0000[S\u0001\u0000\u0000\u0000[T\u0001"+
		"\u0000\u0000\u0000[U\u0001\u0000\u0000\u0000[V\u0001\u0000\u0000\u0000"+
		"[W\u0001\u0000\u0000\u0000[X\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000"+
		"\u0000[Z\u0001\u0000\u0000\u0000\\\u0003\u0001\u0000\u0000\u0000]^\u0005"+
		"\u0016\u0000\u0000^_\u0005\u001a\u0000\u0000_`\u0005\u0015\u0000\u0000"+
		"`a\u0005\u0019\u0000\u0000ab\u0005\u0017\u0000\u0000bc\u0005\u001b\u0000"+
		"\u0000cd\u0005\u0011\u0000\u0000d\u0005\u0001\u0000\u0000\u0000ef\u0005"+
		"\u0013\u0000\u0000fj\u0005\u0016\u0000\u0000gh\u0005\u0019\u0000\u0000"+
		"hi\u0005\u001f\u0000\u0000ik\u0005\u001b\u0000\u0000jg\u0001\u0000\u0000"+
		"\u0000jk\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000lm\u0005\u0011"+
		"\u0000\u0000m\u0007\u0001\u0000\u0000\u0000no\u0005\u0016\u0000\u0000"+
		"op\u0005\u001a\u0000\u0000pq\u0003\u001a\r\u0000qr\u0005\u0011\u0000\u0000"+
		"r\t\u0001\u0000\u0000\u0000st\u0005\u0016\u0000\u0000tu\u0005\u001a\u0000"+
		"\u0000uv\u0003\u0014\n\u0000vw\u0005\u0011\u0000\u0000w\u000b\u0001\u0000"+
		"\u0000\u0000xy\u0005\u0016\u0000\u0000yz\u0005\u001a\u0000\u0000z{\u0003"+
		"\u0016\u000b\u0000{|\u0005\u0011\u0000\u0000|\r\u0001\u0000\u0000\u0000"+
		"}~\u0005\u0016\u0000\u0000~\u007f\u0005\u001a\u0000\u0000\u007f\u0080"+
		"\u0003\u0018\f\u0000\u0080\u0081\u0005\u0011\u0000\u0000\u0081\u000f\u0001"+
		"\u0000\u0000\u0000\u0082\u0083\u0005\u0016\u0000\u0000\u0083\u0084\u0005"+
		"\u001a\u0000\u0000\u0084\u0085\u0003\"\u0011\u0000\u0085\u0086\u0005\u0011"+
		"\u0000\u0000\u0086\u0011\u0001\u0000\u0000\u0000\u0087\u008c\u0003\u0014"+
		"\n\u0000\u0088\u008c\u0003\u0016\u000b\u0000\u0089\u008c\u0003\u0018\f"+
		"\u0000\u008a\u008c\u0003\u001a\r\u0000\u008b\u0087\u0001\u0000\u0000\u0000"+
		"\u008b\u0088\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000"+
		"\u008b\u008a\u0001\u0000\u0000\u0000\u008c\u0013\u0001\u0000\u0000\u0000"+
		"\u008d\u008e\u0005\u0012\u0000\u0000\u008e\u008f\u0005\u0019\u0000\u0000"+
		"\u008f\u0092\u0005\u0017\u0000\u0000\u0090\u0091\u0005\u0010\u0000\u0000"+
		"\u0091\u0093\u0003\u001c\u000e\u0000\u0092\u0090\u0001\u0000\u0000\u0000"+
		"\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000"+
		"\u0094\u0095\u0005\u001b\u0000\u0000\u0095\u0015\u0001\u0000\u0000\u0000"+
		"\u0096\u0097\u0005\r\u0000\u0000\u0097\u0098\u0005\u0019\u0000\u0000\u0098"+
		"\u009b\u0005\u0017\u0000\u0000\u0099\u009a\u0005\u0010\u0000\u0000\u009a"+
		"\u009c\u0003\u001c\u000e\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009b"+
		"\u009c\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0005\u001b\u0000\u0000\u009e\u0017\u0001\u0000\u0000\u0000\u009f"+
		"\u00a0\u0005\u000f\u0000\u0000\u00a0\u00a1\u0005\u0019\u0000\u0000\u00a1"+
		"\u00a4\u0005\u0017\u0000\u0000\u00a2\u00a3\u0005\u0010\u0000\u0000\u00a3"+
		"\u00a5\u0003\u001c\u000e\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a7\u0005\u001b\u0000\u0000\u00a7\u0019\u0001\u0000\u0000\u0000\u00a8"+
		"\u00a9\u0005\u000e\u0000\u0000\u00a9\u00aa\u0005\u0019\u0000\u0000\u00aa"+
		"\u00ab\u0003J%\u0000\u00ab\u00ac\u0005\u0010\u0000\u0000\u00ac\u00ad\u0003"+
		"J%\u0000\u00ad\u00ae\u0005\u001b\u0000\u0000\u00ae\u001b\u0001\u0000\u0000"+
		"\u0000\u00af\u00b4\u0005\u001e\u0000\u0000\u00b0\u00b1\u0005\u0010\u0000"+
		"\u0000\u00b1\u00b3\u0005\u001e\u0000\u0000\u00b2\u00b0\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b6\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b5\u0001\u0000\u0000\u0000\u00b5\u001d\u0001\u0000\u0000"+
		"\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005\u0016\u0000"+
		"\u0000\u00b8\u00b9\u0005\u001a\u0000\u0000\u00b9\u00ba\u0005\u0014\u0000"+
		"\u0000\u00ba\u00be\u0005\u001c\u0000\u0000\u00bb\u00bd\u0003\u0002\u0001"+
		"\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bd\u00c0\u0001\u0000\u0000"+
		"\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00be\u00bf\u0001\u0000\u0000"+
		"\u0000\u00bf\u00c1\u0001\u0000\u0000\u0000\u00c0\u00be\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c2\u0005\u001d\u0000\u0000\u00c2\u001f\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c4\u0003\"\u0011\u0000\u00c4\u00c5\u0005\u0011\u0000\u0000"+
		"\u00c5\u00c9\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005\u0016\u0000\u0000"+
		"\u00c7\u00c9\u0005\u0011\u0000\u0000\u00c8\u00c3\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9!\u0001\u0000\u0000\u0000\u00ca"+
		"\u00dd\u0003$\u0012\u0000\u00cb\u00dd\u0003&\u0013\u0000\u00cc\u00dd\u0003"+
		"(\u0014\u0000\u00cd\u00dd\u0003*\u0015\u0000\u00ce\u00dd\u00036\u001b"+
		"\u0000\u00cf\u00dd\u0003,\u0016\u0000\u00d0\u00dd\u0003.\u0017\u0000\u00d1"+
		"\u00dd\u00030\u0018\u0000\u00d2\u00dd\u00032\u0019\u0000\u00d3\u00dd\u0003"+
		"4\u001a\u0000\u00d4\u00dd\u00038\u001c\u0000\u00d5\u00dd\u0003:\u001d"+
		"\u0000\u00d6\u00dd\u0003<\u001e\u0000\u00d7\u00dd\u0003>\u001f\u0000\u00d8"+
		"\u00dd\u0003@ \u0000\u00d9\u00dd\u0003B!\u0000\u00da\u00dd\u0003D\"\u0000"+
		"\u00db\u00dd\u0003F#\u0000\u00dc\u00ca\u0001\u0000\u0000\u0000\u00dc\u00cb"+
		"\u0001\u0000\u0000\u0000\u00dc\u00cc\u0001\u0000\u0000\u0000\u00dc\u00cd"+
		"\u0001\u0000\u0000\u0000\u00dc\u00ce\u0001\u0000\u0000\u0000\u00dc\u00cf"+
		"\u0001\u0000\u0000\u0000\u00dc\u00d0\u0001\u0000\u0000\u0000\u00dc\u00d1"+
		"\u0001\u0000\u0000\u0000\u00dc\u00d2\u0001\u0000\u0000\u0000\u00dc\u00d3"+
		"\u0001\u0000\u0000\u0000\u00dc\u00d4\u0001\u0000\u0000\u0000\u00dc\u00d5"+
		"\u0001\u0000\u0000\u0000\u00dc\u00d6\u0001\u0000\u0000\u0000\u00dc\u00d7"+
		"\u0001\u0000\u0000\u0000\u00dc\u00d8\u0001\u0000\u0000\u0000\u00dc\u00d9"+
		"\u0001\u0000\u0000\u0000\u00dc\u00da\u0001\u0000\u0000\u0000\u00dc\u00db"+
		"\u0001\u0000\u0000\u0000\u00dd#\u0001\u0000\u0000\u0000\u00de\u00df\u0005"+
		"\f\u0000\u0000\u00df\u00e0\u0005\u0019\u0000\u0000\u00e0\u00e3\u0005\u0016"+
		"\u0000\u0000\u00e1\u00e2\u0005\u0010\u0000\u0000\u00e2\u00e4\u0005\u001e"+
		"\u0000\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000"+
		"\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000\u0000\u00e5\u00e6\u0005\u001b"+
		"\u0000\u0000\u00e6%\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\f\u0000"+
		"\u0000\u00e8\u00e9\u0005\u0019\u0000\u0000\u00e9\u00ec\u0003\u0012\t\u0000"+
		"\u00ea\u00eb\u0005\u0010\u0000\u0000\u00eb\u00ed\u0005\u001e\u0000\u0000"+
		"\u00ec\u00ea\u0001\u0000\u0000\u0000\u00ec\u00ed\u0001\u0000\u0000\u0000"+
		"\u00ed\u00ee\u0001\u0000\u0000\u0000\u00ee\u00ef\u0005\u001b\u0000\u0000"+
		"\u00ef\'\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005\t\u0000\u0000\u00f1"+
		"\u00f2\u0005\u0019\u0000\u0000\u00f2\u00f5\u0005\u0016\u0000\u0000\u00f3"+
		"\u00f4\u0005\u0010\u0000\u0000\u00f4\u00f6\u0003H$\u0000\u00f5\u00f3\u0001"+
		"\u0000\u0000\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000\u00f6\u00f7\u0001"+
		"\u0000\u0000\u0000\u00f7\u00f8\u0005\u001b\u0000\u0000\u00f8)\u0001\u0000"+
		"\u0000\u0000\u00f9\u00fa\u0005\t\u0000\u0000\u00fa\u00fb\u0005\u0019\u0000"+
		"\u0000\u00fb\u00fe\u0003\u0012\t\u0000\u00fc\u00fd\u0005\u0010\u0000\u0000"+
		"\u00fd\u00ff\u0003H$\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00fe\u00ff"+
		"\u0001\u0000\u0000\u0000\u00ff\u0100\u0001\u0000\u0000\u0000\u0100\u0101"+
		"\u0005\u001b\u0000\u0000\u0101+\u0001\u0000\u0000\u0000\u0102\u0103\u0005"+
		"\u0007\u0000\u0000\u0103\u0104\u0005\u0019\u0000\u0000\u0104\u0107\u0005"+
		"\u0016\u0000\u0000\u0105\u0106\u0005\u0010\u0000\u0000\u0106\u0108\u0003"+
		"H$\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001\u0000\u0000"+
		"\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u0109\u010a\u0005\u001b\u0000"+
		"\u0000\u010a-\u0001\u0000\u0000\u0000\u010b\u010c\u0005\u0007\u0000\u0000"+
		"\u010c\u010d\u0005\u0019\u0000\u0000\u010d\u0110\u0003\u0012\t\u0000\u010e"+
		"\u010f\u0005\u0010\u0000\u0000\u010f\u0111\u0003H$\u0000\u0110\u010e\u0001"+
		"\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111\u0112\u0001"+
		"\u0000\u0000\u0000\u0112\u0113\u0005\u001b\u0000\u0000\u0113/\u0001\u0000"+
		"\u0000\u0000\u0114\u0115\u0005\b\u0000\u0000\u0115\u0116\u0005\u0019\u0000"+
		"\u0000\u0116\u0119\u0005\u0016\u0000\u0000\u0117\u0118\u0005\u0010\u0000"+
		"\u0000\u0118\u011a\u0003H$\u0000\u0119\u0117\u0001\u0000\u0000\u0000\u0119"+
		"\u011a\u0001\u0000\u0000\u0000\u011a\u011b\u0001\u0000\u0000\u0000\u011b"+
		"\u011c\u0005\u001b\u0000\u0000\u011c1\u0001\u0000\u0000\u0000\u011d\u011e"+
		"\u0005\b\u0000\u0000\u011e\u011f\u0005\u0019\u0000\u0000\u011f\u0122\u0003"+
		"\u0012\t\u0000\u0120\u0121\u0005\u0010\u0000\u0000\u0121\u0123\u0003H"+
		"$\u0000\u0122\u0120\u0001\u0000\u0000\u0000\u0122\u0123\u0001\u0000\u0000"+
		"\u0000\u0123\u0124\u0001\u0000\u0000\u0000\u0124\u0125\u0005\u001b\u0000"+
		"\u0000\u01253\u0001\u0000\u0000\u0000\u0126\u0127\u0005\n\u0000\u0000"+
		"\u0127\u0128\u0005\u0019\u0000\u0000\u0128\u012b\u0005\u0016\u0000\u0000"+
		"\u0129\u012a\u0005\u0010\u0000\u0000\u012a\u012c\u0003H$\u0000\u012b\u0129"+
		"\u0001\u0000\u0000\u0000\u012b\u012c\u0001\u0000\u0000\u0000\u012c\u012d"+
		"\u0001\u0000\u0000\u0000\u012d\u012e\u0005\u001b\u0000\u0000\u012e5\u0001"+
		"\u0000\u0000\u0000\u012f\u0130\u0005\n\u0000\u0000\u0130\u0131\u0005\u0019"+
		"\u0000\u0000\u0131\u0134\u0003\u0012\t\u0000\u0132\u0133\u0005\u0010\u0000"+
		"\u0000\u0133\u0135\u0003H$\u0000\u0134\u0132\u0001\u0000\u0000\u0000\u0134"+
		"\u0135\u0001\u0000\u0000\u0000\u0135\u0136\u0001\u0000\u0000\u0000\u0136"+
		"\u0137\u0005\u001b\u0000\u0000\u01377\u0001\u0000\u0000\u0000\u0138\u0139"+
		"\u0005\u000b\u0000\u0000\u0139\u013a\u0005\u0019\u0000\u0000\u013a\u013b"+
		"\u0005\u0016\u0000\u0000\u013b\u013c\u0005\u0010\u0000\u0000\u013c\u013f"+
		"\u0005\u001e\u0000\u0000\u013d\u013e\u0005\u0010\u0000\u0000\u013e\u0140"+
		"\u0005\u001e\u0000\u0000\u013f\u013d\u0001\u0000\u0000\u0000\u013f\u0140"+
		"\u0001\u0000\u0000\u0000\u0140\u0141\u0001\u0000\u0000\u0000\u0141\u0142"+
		"\u0005\u001b\u0000\u0000\u01429\u0001\u0000\u0000\u0000\u0143\u0144\u0005"+
		"\u000b\u0000\u0000\u0144\u0145\u0005\u0019\u0000\u0000\u0145\u0146\u0003"+
		"\u0012\t\u0000\u0146\u0147\u0005\u0010\u0000\u0000\u0147\u014a\u0005\u001e"+
		"\u0000\u0000\u0148\u0149\u0005\u0010\u0000\u0000\u0149\u014b\u0005\u001e"+
		"\u0000\u0000\u014a\u0148\u0001\u0000\u0000\u0000\u014a\u014b\u0001\u0000"+
		"\u0000\u0000\u014b\u014c\u0001\u0000\u0000\u0000\u014c\u014d\u0005\u001b"+
		"\u0000\u0000\u014d;\u0001\u0000\u0000\u0000\u014e\u014f\u0005\u0004\u0000"+
		"\u0000\u014f\u0150\u0005\u0019\u0000\u0000\u0150\u0151\u0005\u0016\u0000"+
		"\u0000\u0151\u0152\u0005\u0010\u0000\u0000\u0152\u0153\u0005\u0017\u0000"+
		"\u0000\u0153\u0154\u0005\u001b\u0000\u0000\u0154=\u0001\u0000\u0000\u0000"+
		"\u0155\u0156\u0005\u0006\u0000\u0000\u0156\u0157\u0005\u0019\u0000\u0000"+
		"\u0157\u0158\u0005\u0016\u0000\u0000\u0158\u0159\u0005\u0010\u0000\u0000"+
		"\u0159\u015a\u0005\u0017\u0000\u0000\u015a\u015b\u0005\u001b\u0000\u0000"+
		"\u015b?\u0001\u0000\u0000\u0000\u015c\u015d\u0005\u0005\u0000\u0000\u015d"+
		"\u015e\u0005\u0019\u0000\u0000\u015e\u015f\u0005\u0016\u0000\u0000\u015f"+
		"\u0160\u0005\u0010\u0000\u0000\u0160\u0161\u0005\u0017\u0000\u0000\u0161"+
		"\u0162\u0005\u001b\u0000\u0000\u0162A\u0001\u0000\u0000\u0000\u0163\u0164"+
		"\u0005\u0004\u0000\u0000\u0164\u0165\u0005\u0019\u0000\u0000\u0165\u0166"+
		"\u0003\u0012\t\u0000\u0166\u0167\u0005\u0010\u0000\u0000\u0167\u0168\u0005"+
		"\u0017\u0000\u0000\u0168\u0169\u0005\u001b\u0000\u0000\u0169C\u0001\u0000"+
		"\u0000\u0000\u016a\u016b\u0005\u0006\u0000\u0000\u016b\u016c\u0005\u0019"+
		"\u0000\u0000\u016c\u016d\u0003\u0012\t\u0000\u016d\u016e\u0005\u0010\u0000"+
		"\u0000\u016e\u016f\u0005\u0017\u0000\u0000\u016f\u0170\u0005\u001b\u0000"+
		"\u0000\u0170E\u0001\u0000\u0000\u0000\u0171\u0172\u0005\u0005\u0000\u0000"+
		"\u0172\u0173\u0005\u0019\u0000\u0000\u0173\u0174\u0003\u0012\t\u0000\u0174"+
		"\u0175\u0005\u0010\u0000\u0000\u0175\u0176\u0005\u0017\u0000\u0000\u0176"+
		"\u0177\u0005\u001b\u0000\u0000\u0177G\u0001\u0000\u0000\u0000\u0178\u0179"+
		"\u0007\u0000\u0000\u0000\u0179I\u0001\u0000\u0000\u0000\u017a\u017b\u0007"+
		"\u0001\u0000\u0000\u017bK\u0001\u0000\u0000\u0000\u0017O[j\u008b\u0092"+
		"\u009b\u00a4\u00b4\u00be\u00c8\u00dc\u00e3\u00ec\u00f5\u00fe\u0107\u0110"+
		"\u0119\u0122\u012b\u0134\u013f\u014a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}