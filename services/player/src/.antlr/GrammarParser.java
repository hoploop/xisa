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
		RULE_createAndUseDetector = 4, RULE_createSelectorByPosition = 5, RULE_createSelectorByLabel = 6, 
		RULE_createSelectorByText = 7, RULE_createSelectorByRegex = 8, RULE_createOperation = 9, 
		RULE_selector = 10, RULE_selectorByLabel = 11, RULE_selectorByText = 12, 
		RULE_selectorByRegex = 13, RULE_selectorByPosition = 14, RULE_selectorByImage = 15, 
		RULE_selectorOrder = 16, RULE_createSequence = 17, RULE_runOperation = 18, 
		RULE_operation = 19, RULE_wait = 20, RULE_waitSelector = 21, RULE_mousePress = 22, 
		RULE_mousePressSelector = 23, RULE_mouseClick = 24, RULE_mouseClickSelector = 25, 
		RULE_mouseDoubleClick = 26, RULE_mouseDoubleClickSelector = 27, RULE_mouseRelease = 28, 
		RULE_mouseReleaseSelector = 29, RULE_mouseScroll = 30, RULE_mouseScrollSelector = 31, 
		RULE_keyCombo = 32, RULE_keyComboSelector = 33, RULE_keyPress = 34, RULE_keyRelease = 35, 
		RULE_keyType = 36, RULE_keyPressSelector = 37, RULE_keyReleaseSelector = 38, 
		RULE_keyTypeSelector = 39, RULE_mouseButton = 40, RULE_number = 41;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "stmt", "createDetector", "useDetector", "createAndUseDetector", 
			"createSelectorByPosition", "createSelectorByLabel", "createSelectorByText", 
			"createSelectorByRegex", "createOperation", "selector", "selectorByLabel", 
			"selectorByText", "selectorByRegex", "selectorByPosition", "selectorByImage", 
			"selectorOrder", "createSequence", "runOperation", "operation", "wait", 
			"waitSelector", "mousePress", "mousePressSelector", "mouseClick", "mouseClickSelector", 
			"mouseDoubleClick", "mouseDoubleClickSelector", "mouseRelease", "mouseReleaseSelector", 
			"mouseScroll", "mouseScrollSelector", "keyCombo", "keyComboSelector", 
			"keyPress", "keyRelease", "keyType", "keyPressSelector", "keyReleaseSelector", 
			"keyTypeSelector", "mouseButton", "number"
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
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 75628416L) != 0)) {
				{
				{
				setState(84);
				stmt();
				}
				}
				setState(89);
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
			setState(98);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				createDetector();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				createSelectorByLabel();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				createSelectorByText();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(93);
				createSelectorByRegex();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(94);
				createSelectorByPosition();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(95);
				createOperation();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(96);
				createSequence();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(97);
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
			setState(100);
			match(ID);
			setState(101);
			match(EQ);
			setState(102);
			match(DETECTOR);
			setState(103);
			match(ORPAR);
			setState(104);
			match(STRING);
			setState(105);
			match(CRPAR);
			setState(106);
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
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
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
			setState(108);
			match(USE);
			setState(109);
			match(ORPAR);
			setState(110);
			match(ID);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(111);
				match(COMMA);
				setState(112);
				match(FLOAT);
				}
			}

			setState(115);
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
	public static class CreateAndUseDetectorContext extends ParserRuleContext {
		public TerminalNode USE() { return getToken(GrammarParser.USE, 0); }
		public TerminalNode ORPAR() { return getToken(GrammarParser.ORPAR, 0); }
		public TerminalNode STRING() { return getToken(GrammarParser.STRING, 0); }
		public TerminalNode CRPAR() { return getToken(GrammarParser.CRPAR, 0); }
		public TerminalNode COMMA() { return getToken(GrammarParser.COMMA, 0); }
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public CreateAndUseDetectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_createAndUseDetector; }
	}

	public final CreateAndUseDetectorContext createAndUseDetector() throws RecognitionException {
		CreateAndUseDetectorContext _localctx = new CreateAndUseDetectorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_createAndUseDetector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(USE);
			setState(118);
			match(ORPAR);
			setState(119);
			match(STRING);
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(120);
				match(COMMA);
				setState(121);
				match(FLOAT);
				}
			}

			setState(124);
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
		enterRule(_localctx, 10, RULE_createSelectorByPosition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(ID);
			setState(127);
			match(EQ);
			setState(128);
			selectorByPosition();
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
		enterRule(_localctx, 12, RULE_createSelectorByLabel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(ID);
			setState(132);
			match(EQ);
			setState(133);
			selectorByLabel();
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
		enterRule(_localctx, 14, RULE_createSelectorByText);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(ID);
			setState(137);
			match(EQ);
			setState(138);
			selectorByText();
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
		enterRule(_localctx, 16, RULE_createSelectorByRegex);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(ID);
			setState(142);
			match(EQ);
			setState(143);
			selectorByRegex();
			setState(144);
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
		enterRule(_localctx, 18, RULE_createOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(ID);
			setState(147);
			match(EQ);
			setState(148);
			operation();
			setState(149);
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
		enterRule(_localctx, 20, RULE_selector);
		try {
			setState(156);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LABEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				selectorByLabel();
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				selectorByText();
				}
				break;
			case REGEX:
				enterOuterAlt(_localctx, 3);
				{
				setState(153);
				selectorByRegex();
				}
				break;
			case POSITION:
				enterOuterAlt(_localctx, 4);
				{
				setState(154);
				selectorByPosition();
				}
				break;
			case IMAGE:
				enterOuterAlt(_localctx, 5);
				{
				setState(155);
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
		enterRule(_localctx, 22, RULE_selectorByLabel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(LABEL);
			setState(159);
			match(ORPAR);
			setState(160);
			match(STRING);
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(161);
				match(COMMA);
				setState(162);
				selectorOrder();
				}
			}

			setState(165);
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
		enterRule(_localctx, 24, RULE_selectorByText);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(TEXT);
			setState(168);
			match(ORPAR);
			setState(169);
			match(STRING);
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(170);
				match(COMMA);
				setState(171);
				selectorOrder();
				}
			}

			setState(174);
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
		enterRule(_localctx, 26, RULE_selectorByRegex);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(REGEX);
			setState(177);
			match(ORPAR);
			setState(178);
			match(STRING);
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(179);
				match(COMMA);
				setState(180);
				selectorOrder();
				}
			}

			setState(183);
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
		enterRule(_localctx, 28, RULE_selectorByPosition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(POSITION);
			setState(186);
			match(ORPAR);
			setState(187);
			number();
			setState(188);
			match(COMMA);
			setState(189);
			number();
			setState(190);
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
		enterRule(_localctx, 30, RULE_selectorByImage);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(IMAGE);
			setState(193);
			match(ORPAR);
			setState(194);
			match(STRING);
			setState(195);
			match(COMMA);
			setState(196);
			match(FLOAT);
			setState(199);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(197);
				match(COMMA);
				setState(198);
				selectorOrder();
				}
				break;
			}
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(201);
				match(COMMA);
				setState(202);
				match(GRAY);
				}
			}

			setState(205);
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
		enterRule(_localctx, 32, RULE_selectorOrder);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(INT);
			setState(212);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(208);
					match(COMMA);
					setState(209);
					match(INT);
					}
					} 
				}
				setState(214);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
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
		enterRule(_localctx, 34, RULE_createSequence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(ID);
			setState(216);
			match(EQ);
			setState(217);
			match(SEQUENCE);
			setState(218);
			match(OCPAR);
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 75628416L) != 0)) {
				{
				{
				setState(219);
				stmt();
				}
				}
				setState(224);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(225);
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
		enterRule(_localctx, 36, RULE_runOperation);
		try {
			setState(232);
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
			case USE:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				operation();
				setState(228);
				match(DCOMMA);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(230);
				match(ID);
				setState(231);
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
		public UseDetectorContext useDetector() {
			return getRuleContext(UseDetectorContext.class,0);
		}
		public CreateAndUseDetectorContext createAndUseDetector() {
			return getRuleContext(CreateAndUseDetectorContext.class,0);
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
		enterRule(_localctx, 38, RULE_operation);
		try {
			setState(256);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				wait();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(235);
				waitSelector();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(236);
				useDetector();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(237);
				createAndUseDetector();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(238);
				mousePress();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(239);
				mousePressSelector();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(240);
				mouseReleaseSelector();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(241);
				mouseClick();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(242);
				mouseClickSelector();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(243);
				mouseDoubleClick();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(244);
				mouseDoubleClickSelector();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(245);
				mouseRelease();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(246);
				mouseScroll();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(247);
				mouseScrollSelector();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(248);
				keyPress();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(249);
				keyRelease();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(250);
				keyType();
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(251);
				keyCombo();
				}
				break;
			case 19:
				enterOuterAlt(_localctx, 19);
				{
				setState(252);
				keyComboSelector();
				}
				break;
			case 20:
				enterOuterAlt(_localctx, 20);
				{
				setState(253);
				keyPressSelector();
				}
				break;
			case 21:
				enterOuterAlt(_localctx, 21);
				{
				setState(254);
				keyReleaseSelector();
				}
				break;
			case 22:
				enterOuterAlt(_localctx, 22);
				{
				setState(255);
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
		enterRule(_localctx, 40, RULE_wait);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(WAIT);
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
				match(INT);
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
		enterRule(_localctx, 42, RULE_waitSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(WAIT);
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
				match(INT);
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
		enterRule(_localctx, 44, RULE_mousePress);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			match(MOUSE_PRESS);
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
		enterRule(_localctx, 46, RULE_mousePressSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(285);
			match(MOUSE_PRESS);
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
		enterRule(_localctx, 48, RULE_mouseClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			match(MOUSE_CLICK);
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
		enterRule(_localctx, 50, RULE_mouseClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			match(MOUSE_CLICK);
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
		enterRule(_localctx, 52, RULE_mouseDoubleClick);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			match(MOUSE_DOUBLE_CLICK);
			setState(313);
			match(ORPAR);
			setState(314);
			match(ID);
			setState(317);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(315);
				match(COMMA);
				setState(316);
				mouseButton();
				}
			}

			setState(319);
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
		enterRule(_localctx, 54, RULE_mouseDoubleClickSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			match(MOUSE_DOUBLE_CLICK);
			setState(322);
			match(ORPAR);
			setState(323);
			selector();
			setState(326);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(324);
				match(COMMA);
				setState(325);
				mouseButton();
				}
			}

			setState(328);
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
		enterRule(_localctx, 56, RULE_mouseRelease);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(330);
			match(MOUSE_RELEASE);
			setState(331);
			match(ORPAR);
			setState(332);
			match(ID);
			setState(335);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(333);
				match(COMMA);
				setState(334);
				mouseButton();
				}
			}

			setState(337);
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
		enterRule(_localctx, 58, RULE_mouseReleaseSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(339);
			match(MOUSE_RELEASE);
			setState(340);
			match(ORPAR);
			setState(341);
			selector();
			setState(344);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(342);
				match(COMMA);
				setState(343);
				mouseButton();
				}
			}

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
		enterRule(_localctx, 60, RULE_mouseScroll);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(MOUSE_SCROLL);
			setState(349);
			match(ORPAR);
			setState(350);
			match(ID);
			setState(351);
			match(COMMA);
			setState(352);
			match(INT);
			setState(355);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(353);
				match(COMMA);
				setState(354);
				match(INT);
				}
			}

			setState(357);
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
		enterRule(_localctx, 62, RULE_mouseScrollSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(MOUSE_SCROLL);
			setState(360);
			match(ORPAR);
			setState(361);
			selector();
			setState(362);
			match(COMMA);
			setState(363);
			match(INT);
			setState(366);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(364);
				match(COMMA);
				setState(365);
				match(INT);
				}
			}

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
		enterRule(_localctx, 64, RULE_keyCombo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			match(KEY_COMBO);
			setState(371);
			match(ORPAR);
			setState(372);
			match(ID);
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
		enterRule(_localctx, 66, RULE_keyComboSelector);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			match(KEY_COMBO);
			setState(383);
			match(ORPAR);
			setState(384);
			selector();
			setState(385);
			match(STRING);
			setState(388); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(386);
				match(COMMA);
				setState(387);
				match(STRING);
				}
				}
				setState(390); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			setState(392);
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
		enterRule(_localctx, 68, RULE_keyPress);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			match(KEY_PRESS);
			setState(395);
			match(ORPAR);
			setState(396);
			match(ID);
			setState(397);
			match(COMMA);
			setState(398);
			match(STRING);
			setState(399);
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
		enterRule(_localctx, 70, RULE_keyRelease);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			match(KEY_RELEASE);
			setState(402);
			match(ORPAR);
			setState(403);
			match(ID);
			setState(404);
			match(COMMA);
			setState(405);
			match(STRING);
			setState(406);
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
		enterRule(_localctx, 72, RULE_keyType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(408);
			match(KEY_TYPE);
			setState(409);
			match(ORPAR);
			setState(410);
			match(ID);
			setState(411);
			match(COMMA);
			setState(412);
			match(STRING);
			setState(413);
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
		enterRule(_localctx, 74, RULE_keyPressSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			match(KEY_PRESS);
			setState(416);
			match(ORPAR);
			setState(417);
			selector();
			setState(418);
			match(COMMA);
			setState(419);
			match(STRING);
			setState(420);
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
		enterRule(_localctx, 76, RULE_keyReleaseSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(422);
			match(KEY_RELEASE);
			setState(423);
			match(ORPAR);
			setState(424);
			selector();
			setState(425);
			match(COMMA);
			setState(426);
			match(STRING);
			setState(427);
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
		enterRule(_localctx, 78, RULE_keyTypeSelector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429);
			match(KEY_TYPE);
			setState(430);
			match(ORPAR);
			setState(431);
			selector();
			setState(432);
			match(COMMA);
			setState(433);
			match(STRING);
			setState(434);
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
		enterRule(_localctx, 80, RULE_mouseButton);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(436);
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
		enterRule(_localctx, 82, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
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
		"\u0004\u0001$\u01b9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"(\u0007(\u0002)\u0007)\u0001\u0000\u0005\u0000V\b\u0000\n\u0000\f\u0000"+
		"Y\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001c\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003r\b\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004{\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u009d\b\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00a4\b\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00ad\b\f\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00b6\b\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00c8\b\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u00cc\b\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0005\u0010\u00d3\b\u0010\n\u0010\f\u0010\u00d6"+
		"\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005"+
		"\u0011\u00dd\b\u0011\n\u0011\f\u0011\u00e0\t\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012"+
		"\u00e9\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013"+
		"\u0101\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0003\u0014\u0108\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0111\b\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u011a\b\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0123\b\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u012c\b\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u0135\b\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0003\u001a\u013e\b\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u0147\b\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0003\u001c\u0150\b\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0159\b\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0003\u001e\u0164\b\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0003\u001f\u016f\b\u001f\u0001\u001f\u0001\u001f\u0001 "+
		"\u0001 \u0001 \u0001 \u0001 \u0001 \u0004 \u0179\b \u000b \f \u017a\u0001"+
		" \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0004!\u0185\b!\u000b"+
		"!\f!\u0186\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0001\"\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001$\u0001"+
		"$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001%\u0001%\u0001%\u0001%\u0001"+
		"%\u0001%\u0001%\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001"+
		"\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0001"+
		")\u0001)\u0001)\u0000\u0000*\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPR"+
		"\u0000\u0002\u0001\u0000\u0003\u0005\u0001\u0000\"#\u01c7\u0000W\u0001"+
		"\u0000\u0000\u0000\u0002b\u0001\u0000\u0000\u0000\u0004d\u0001\u0000\u0000"+
		"\u0000\u0006l\u0001\u0000\u0000\u0000\bu\u0001\u0000\u0000\u0000\n~\u0001"+
		"\u0000\u0000\u0000\f\u0083\u0001\u0000\u0000\u0000\u000e\u0088\u0001\u0000"+
		"\u0000\u0000\u0010\u008d\u0001\u0000\u0000\u0000\u0012\u0092\u0001\u0000"+
		"\u0000\u0000\u0014\u009c\u0001\u0000\u0000\u0000\u0016\u009e\u0001\u0000"+
		"\u0000\u0000\u0018\u00a7\u0001\u0000\u0000\u0000\u001a\u00b0\u0001\u0000"+
		"\u0000\u0000\u001c\u00b9\u0001\u0000\u0000\u0000\u001e\u00c0\u0001\u0000"+
		"\u0000\u0000 \u00cf\u0001\u0000\u0000\u0000\"\u00d7\u0001\u0000\u0000"+
		"\u0000$\u00e8\u0001\u0000\u0000\u0000&\u0100\u0001\u0000\u0000\u0000("+
		"\u0102\u0001\u0000\u0000\u0000*\u010b\u0001\u0000\u0000\u0000,\u0114\u0001"+
		"\u0000\u0000\u0000.\u011d\u0001\u0000\u0000\u00000\u0126\u0001\u0000\u0000"+
		"\u00002\u012f\u0001\u0000\u0000\u00004\u0138\u0001\u0000\u0000\u00006"+
		"\u0141\u0001\u0000\u0000\u00008\u014a\u0001\u0000\u0000\u0000:\u0153\u0001"+
		"\u0000\u0000\u0000<\u015c\u0001\u0000\u0000\u0000>\u0167\u0001\u0000\u0000"+
		"\u0000@\u0172\u0001\u0000\u0000\u0000B\u017e\u0001\u0000\u0000\u0000D"+
		"\u018a\u0001\u0000\u0000\u0000F\u0191\u0001\u0000\u0000\u0000H\u0198\u0001"+
		"\u0000\u0000\u0000J\u019f\u0001\u0000\u0000\u0000L\u01a6\u0001\u0000\u0000"+
		"\u0000N\u01ad\u0001\u0000\u0000\u0000P\u01b4\u0001\u0000\u0000\u0000R"+
		"\u01b6\u0001\u0000\u0000\u0000TV\u0003\u0002\u0001\u0000UT\u0001\u0000"+
		"\u0000\u0000VY\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001"+
		"\u0000\u0000\u0000X\u0001\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000"+
		"\u0000Zc\u0003\u0004\u0002\u0000[c\u0003\f\u0006\u0000\\c\u0003\u000e"+
		"\u0007\u0000]c\u0003\u0010\b\u0000^c\u0003\n\u0005\u0000_c\u0003\u0012"+
		"\t\u0000`c\u0003\"\u0011\u0000ac\u0003$\u0012\u0000bZ\u0001\u0000\u0000"+
		"\u0000b[\u0001\u0000\u0000\u0000b\\\u0001\u0000\u0000\u0000b]\u0001\u0000"+
		"\u0000\u0000b^\u0001\u0000\u0000\u0000b_\u0001\u0000\u0000\u0000b`\u0001"+
		"\u0000\u0000\u0000ba\u0001\u0000\u0000\u0000c\u0003\u0001\u0000\u0000"+
		"\u0000de\u0005\u001a\u0000\u0000ef\u0005\u001e\u0000\u0000fg\u0005\u0019"+
		"\u0000\u0000gh\u0005\u001d\u0000\u0000hi\u0005\u001b\u0000\u0000ij\u0005"+
		"\u001f\u0000\u0000jk\u0005\u0015\u0000\u0000k\u0005\u0001\u0000\u0000"+
		"\u0000lm\u0005\u0017\u0000\u0000mn\u0005\u001d\u0000\u0000nq\u0005\u001a"+
		"\u0000\u0000op\u0005\u0014\u0000\u0000pr\u0005#\u0000\u0000qo\u0001\u0000"+
		"\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0005"+
		"\u001f\u0000\u0000t\u0007\u0001\u0000\u0000\u0000uv\u0005\u0017\u0000"+
		"\u0000vw\u0005\u001d\u0000\u0000wz\u0005\u001b\u0000\u0000xy\u0005\u0014"+
		"\u0000\u0000y{\u0005#\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001\u0000"+
		"\u0000\u0000{|\u0001\u0000\u0000\u0000|}\u0005\u001f\u0000\u0000}\t\u0001"+
		"\u0000\u0000\u0000~\u007f\u0005\u001a\u0000\u0000\u007f\u0080\u0005\u001e"+
		"\u0000\u0000\u0080\u0081\u0003\u001c\u000e\u0000\u0081\u0082\u0005\u0015"+
		"\u0000\u0000\u0082\u000b\u0001\u0000\u0000\u0000\u0083\u0084\u0005\u001a"+
		"\u0000\u0000\u0084\u0085\u0005\u001e\u0000\u0000\u0085\u0086\u0003\u0016"+
		"\u000b\u0000\u0086\u0087\u0005\u0015\u0000\u0000\u0087\r\u0001\u0000\u0000"+
		"\u0000\u0088\u0089\u0005\u001a\u0000\u0000\u0089\u008a\u0005\u001e\u0000"+
		"\u0000\u008a\u008b\u0003\u0018\f\u0000\u008b\u008c\u0005\u0015\u0000\u0000"+
		"\u008c\u000f\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u001a\u0000\u0000"+
		"\u008e\u008f\u0005\u001e\u0000\u0000\u008f\u0090\u0003\u001a\r\u0000\u0090"+
		"\u0091\u0005\u0015\u0000\u0000\u0091\u0011\u0001\u0000\u0000\u0000\u0092"+
		"\u0093\u0005\u001a\u0000\u0000\u0093\u0094\u0005\u001e\u0000\u0000\u0094"+
		"\u0095\u0003&\u0013\u0000\u0095\u0096\u0005\u0015\u0000\u0000\u0096\u0013"+
		"\u0001\u0000\u0000\u0000\u0097\u009d\u0003\u0016\u000b\u0000\u0098\u009d"+
		"\u0003\u0018\f\u0000\u0099\u009d\u0003\u001a\r\u0000\u009a\u009d\u0003"+
		"\u001c\u000e\u0000\u009b\u009d\u0003\u001e\u000f\u0000\u009c\u0097\u0001"+
		"\u0000\u0000\u0000\u009c\u0098\u0001\u0000\u0000\u0000\u009c\u0099\u0001"+
		"\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009b\u0001"+
		"\u0000\u0000\u0000\u009d\u0015\u0001\u0000\u0000\u0000\u009e\u009f\u0005"+
		"\u0016\u0000\u0000\u009f\u00a0\u0005\u001d\u0000\u0000\u00a0\u00a3\u0005"+
		"\u001b\u0000\u0000\u00a1\u00a2\u0005\u0014\u0000\u0000\u00a2\u00a4\u0003"+
		" \u0010\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a6\u0005\u001f"+
		"\u0000\u0000\u00a6\u0017\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005\u0011"+
		"\u0000\u0000\u00a8\u00a9\u0005\u001d\u0000\u0000\u00a9\u00ac\u0005\u001b"+
		"\u0000\u0000\u00aa\u00ab\u0005\u0014\u0000\u0000\u00ab\u00ad\u0003 \u0010"+
		"\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ac\u00ad\u0001\u0000\u0000"+
		"\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\u001f\u0000"+
		"\u0000\u00af\u0019\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005\u0013\u0000"+
		"\u0000\u00b1\u00b2\u0005\u001d\u0000\u0000\u00b2\u00b5\u0005\u001b\u0000"+
		"\u0000\u00b3\u00b4\u0005\u0014\u0000\u0000\u00b4\u00b6\u0003 \u0010\u0000"+
		"\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000\u0000\u0000"+
		"\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005\u001f\u0000\u0000"+
		"\u00b8\u001b\u0001\u0000\u0000\u0000\u00b9\u00ba\u0005\u0012\u0000\u0000"+
		"\u00ba\u00bb\u0005\u001d\u0000\u0000\u00bb\u00bc\u0003R)\u0000\u00bc\u00bd"+
		"\u0005\u0014\u0000\u0000\u00bd\u00be\u0003R)\u0000\u00be\u00bf\u0005\u001f"+
		"\u0000\u0000\u00bf\u001d\u0001\u0000\u0000\u0000\u00c0\u00c1\u0005\u0006"+
		"\u0000\u0000\u00c1\u00c2\u0005\u001d\u0000\u0000\u00c2\u00c3\u0005\u001b"+
		"\u0000\u0000\u00c3\u00c4\u0005\u0014\u0000\u0000\u00c4\u00c7\u0005#\u0000"+
		"\u0000\u00c5\u00c6\u0005\u0014\u0000\u0000\u00c6\u00c8\u0003 \u0010\u0000"+
		"\u00c7\u00c5\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000\u0000\u0000"+
		"\u00c8\u00cb\u0001\u0000\u0000\u0000\u00c9\u00ca\u0005\u0014\u0000\u0000"+
		"\u00ca\u00cc\u0005\u0002\u0000\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000"+
		"\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000\u0000"+
		"\u00cd\u00ce\u0005\u001f\u0000\u0000\u00ce\u001f\u0001\u0000\u0000\u0000"+
		"\u00cf\u00d4\u0005\"\u0000\u0000\u00d0\u00d1\u0005\u0014\u0000\u0000\u00d1"+
		"\u00d3\u0005\"\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000\u00d3\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d5"+
		"\u0001\u0000\u0000\u0000\u00d5!\u0001\u0000\u0000\u0000\u00d6\u00d4\u0001"+
		"\u0000\u0000\u0000\u00d7\u00d8\u0005\u001a\u0000\u0000\u00d8\u00d9\u0005"+
		"\u001e\u0000\u0000\u00d9\u00da\u0005\u0018\u0000\u0000\u00da\u00de\u0005"+
		" \u0000\u0000\u00db\u00dd\u0003\u0002\u0001\u0000\u00dc\u00db\u0001\u0000"+
		"\u0000\u0000\u00dd\u00e0\u0001\u0000\u0000\u0000\u00de\u00dc\u0001\u0000"+
		"\u0000\u0000\u00de\u00df\u0001\u0000\u0000\u0000\u00df\u00e1\u0001\u0000"+
		"\u0000\u0000\u00e0\u00de\u0001\u0000\u0000\u0000\u00e1\u00e2\u0005!\u0000"+
		"\u0000\u00e2#\u0001\u0000\u0000\u0000\u00e3\u00e4\u0003&\u0013\u0000\u00e4"+
		"\u00e5\u0005\u0015\u0000\u0000\u00e5\u00e9\u0001\u0000\u0000\u0000\u00e6"+
		"\u00e7\u0005\u001a\u0000\u0000\u00e7\u00e9\u0005\u0015\u0000\u0000\u00e8"+
		"\u00e3\u0001\u0000\u0000\u0000\u00e8\u00e6\u0001\u0000\u0000\u0000\u00e9"+
		"%\u0001\u0000\u0000\u0000\u00ea\u0101\u0003(\u0014\u0000\u00eb\u0101\u0003"+
		"*\u0015\u0000\u00ec\u0101\u0003\u0006\u0003\u0000\u00ed\u0101\u0003\b"+
		"\u0004\u0000\u00ee\u0101\u0003,\u0016\u0000\u00ef\u0101\u0003.\u0017\u0000"+
		"\u00f0\u0101\u0003:\u001d\u0000\u00f1\u0101\u00030\u0018\u0000\u00f2\u0101"+
		"\u00032\u0019\u0000\u00f3\u0101\u00034\u001a\u0000\u00f4\u0101\u00036"+
		"\u001b\u0000\u00f5\u0101\u00038\u001c\u0000\u00f6\u0101\u0003<\u001e\u0000"+
		"\u00f7\u0101\u0003>\u001f\u0000\u00f8\u0101\u0003D\"\u0000\u00f9\u0101"+
		"\u0003F#\u0000\u00fa\u0101\u0003H$\u0000\u00fb\u0101\u0003@ \u0000\u00fc"+
		"\u0101\u0003B!\u0000\u00fd\u0101\u0003J%\u0000\u00fe\u0101\u0003L&\u0000"+
		"\u00ff\u0101\u0003N\'\u0000\u0100\u00ea\u0001\u0000\u0000\u0000\u0100"+
		"\u00eb\u0001\u0000\u0000\u0000\u0100\u00ec\u0001\u0000\u0000\u0000\u0100"+
		"\u00ed\u0001\u0000\u0000\u0000\u0100\u00ee\u0001\u0000\u0000\u0000\u0100"+
		"\u00ef\u0001\u0000\u0000\u0000\u0100\u00f0\u0001\u0000\u0000\u0000\u0100"+
		"\u00f1\u0001\u0000\u0000\u0000\u0100\u00f2\u0001\u0000\u0000\u0000\u0100"+
		"\u00f3\u0001\u0000\u0000\u0000\u0100\u00f4\u0001\u0000\u0000\u0000\u0100"+
		"\u00f5\u0001\u0000\u0000\u0000\u0100\u00f6\u0001\u0000\u0000\u0000\u0100"+
		"\u00f7\u0001\u0000\u0000\u0000\u0100\u00f8\u0001\u0000\u0000\u0000\u0100"+
		"\u00f9\u0001\u0000\u0000\u0000\u0100\u00fa\u0001\u0000\u0000\u0000\u0100"+
		"\u00fb\u0001\u0000\u0000\u0000\u0100\u00fc\u0001\u0000\u0000\u0000\u0100"+
		"\u00fd\u0001\u0000\u0000\u0000\u0100\u00fe\u0001\u0000\u0000\u0000\u0100"+
		"\u00ff\u0001\u0000\u0000\u0000\u0101\'\u0001\u0000\u0000\u0000\u0102\u0103"+
		"\u0005\u0010\u0000\u0000\u0103\u0104\u0005\u001d\u0000\u0000\u0104\u0107"+
		"\u0005\u001a\u0000\u0000\u0105\u0106\u0005\u0014\u0000\u0000\u0106\u0108"+
		"\u0005\"\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001"+
		"\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u0109\u010a\u0005"+
		"\u001f\u0000\u0000\u010a)\u0001\u0000\u0000\u0000\u010b\u010c\u0005\u0010"+
		"\u0000\u0000\u010c\u010d\u0005\u001d\u0000\u0000\u010d\u0110\u0003\u0014"+
		"\n\u0000\u010e\u010f\u0005\u0014\u0000\u0000\u010f\u0111\u0005\"\u0000"+
		"\u0000\u0110\u010e\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000"+
		"\u0000\u0111\u0112\u0001\u0000\u0000\u0000\u0112\u0113\u0005\u001f\u0000"+
		"\u0000\u0113+\u0001\u0000\u0000\u0000\u0114\u0115\u0005\r\u0000\u0000"+
		"\u0115\u0116\u0005\u001d\u0000\u0000\u0116\u0119\u0005\u001a\u0000\u0000"+
		"\u0117\u0118\u0005\u0014\u0000\u0000\u0118\u011a\u0003P(\u0000\u0119\u0117"+
		"\u0001\u0000\u0000\u0000\u0119\u011a\u0001\u0000\u0000\u0000\u011a\u011b"+
		"\u0001\u0000\u0000\u0000\u011b\u011c\u0005\u001f\u0000\u0000\u011c-\u0001"+
		"\u0000\u0000\u0000\u011d\u011e\u0005\r\u0000\u0000\u011e\u011f\u0005\u001d"+
		"\u0000\u0000\u011f\u0122\u0003\u0014\n\u0000\u0120\u0121\u0005\u0014\u0000"+
		"\u0000\u0121\u0123\u0003P(\u0000\u0122\u0120\u0001\u0000\u0000\u0000\u0122"+
		"\u0123\u0001\u0000\u0000\u0000\u0123\u0124\u0001\u0000\u0000\u0000\u0124"+
		"\u0125\u0005\u001f\u0000\u0000\u0125/\u0001\u0000\u0000\u0000\u0126\u0127"+
		"\u0005\u000b\u0000\u0000\u0127\u0128\u0005\u001d\u0000\u0000\u0128\u012b"+
		"\u0005\u001a\u0000\u0000\u0129\u012a\u0005\u0014\u0000\u0000\u012a\u012c"+
		"\u0003P(\u0000\u012b\u0129\u0001\u0000\u0000\u0000\u012b\u012c\u0001\u0000"+
		"\u0000\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d\u012e\u0005\u001f"+
		"\u0000\u0000\u012e1\u0001\u0000\u0000\u0000\u012f\u0130\u0005\u000b\u0000"+
		"\u0000\u0130\u0131\u0005\u001d\u0000\u0000\u0131\u0134\u0003\u0014\n\u0000"+
		"\u0132\u0133\u0005\u0014\u0000\u0000\u0133\u0135\u0003P(\u0000\u0134\u0132"+
		"\u0001\u0000\u0000\u0000\u0134\u0135\u0001\u0000\u0000\u0000\u0135\u0136"+
		"\u0001\u0000\u0000\u0000\u0136\u0137\u0005\u001f\u0000\u0000\u01373\u0001"+
		"\u0000\u0000\u0000\u0138\u0139\u0005\f\u0000\u0000\u0139\u013a\u0005\u001d"+
		"\u0000\u0000\u013a\u013d\u0005\u001a\u0000\u0000\u013b\u013c\u0005\u0014"+
		"\u0000\u0000\u013c\u013e\u0003P(\u0000\u013d\u013b\u0001\u0000\u0000\u0000"+
		"\u013d\u013e\u0001\u0000\u0000\u0000\u013e\u013f\u0001\u0000\u0000\u0000"+
		"\u013f\u0140\u0005\u001f\u0000\u0000\u01405\u0001\u0000\u0000\u0000\u0141"+
		"\u0142\u0005\f\u0000\u0000\u0142\u0143\u0005\u001d\u0000\u0000\u0143\u0146"+
		"\u0003\u0014\n\u0000\u0144\u0145\u0005\u0014\u0000\u0000\u0145\u0147\u0003"+
		"P(\u0000\u0146\u0144\u0001\u0000\u0000\u0000\u0146\u0147\u0001\u0000\u0000"+
		"\u0000\u0147\u0148\u0001\u0000\u0000\u0000\u0148\u0149\u0005\u001f\u0000"+
		"\u0000\u01497\u0001\u0000\u0000\u0000\u014a\u014b\u0005\u000e\u0000\u0000"+
		"\u014b\u014c\u0005\u001d\u0000\u0000\u014c\u014f\u0005\u001a\u0000\u0000"+
		"\u014d\u014e\u0005\u0014\u0000\u0000\u014e\u0150\u0003P(\u0000\u014f\u014d"+
		"\u0001\u0000\u0000\u0000\u014f\u0150\u0001\u0000\u0000\u0000\u0150\u0151"+
		"\u0001\u0000\u0000\u0000\u0151\u0152\u0005\u001f\u0000\u0000\u01529\u0001"+
		"\u0000\u0000\u0000\u0153\u0154\u0005\u000e\u0000\u0000\u0154\u0155\u0005"+
		"\u001d\u0000\u0000\u0155\u0158\u0003\u0014\n\u0000\u0156\u0157\u0005\u0014"+
		"\u0000\u0000\u0157\u0159\u0003P(\u0000\u0158\u0156\u0001\u0000\u0000\u0000"+
		"\u0158\u0159\u0001\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000\u0000"+
		"\u015a\u015b\u0005\u001f\u0000\u0000\u015b;\u0001\u0000\u0000\u0000\u015c"+
		"\u015d\u0005\u000f\u0000\u0000\u015d\u015e\u0005\u001d\u0000\u0000\u015e"+
		"\u015f\u0005\u001a\u0000\u0000\u015f\u0160\u0005\u0014\u0000\u0000\u0160"+
		"\u0163\u0005\"\u0000\u0000\u0161\u0162\u0005\u0014\u0000\u0000\u0162\u0164"+
		"\u0005\"\u0000\u0000\u0163\u0161\u0001\u0000\u0000\u0000\u0163\u0164\u0001"+
		"\u0000\u0000\u0000\u0164\u0165\u0001\u0000\u0000\u0000\u0165\u0166\u0005"+
		"\u001f\u0000\u0000\u0166=\u0001\u0000\u0000\u0000\u0167\u0168\u0005\u000f"+
		"\u0000\u0000\u0168\u0169\u0005\u001d\u0000\u0000\u0169\u016a\u0003\u0014"+
		"\n\u0000\u016a\u016b\u0005\u0014\u0000\u0000\u016b\u016e\u0005\"\u0000"+
		"\u0000\u016c\u016d\u0005\u0014\u0000\u0000\u016d\u016f\u0005\"\u0000\u0000"+
		"\u016e\u016c\u0001\u0000\u0000\u0000\u016e\u016f\u0001\u0000\u0000\u0000"+
		"\u016f\u0170\u0001\u0000\u0000\u0000\u0170\u0171\u0005\u001f\u0000\u0000"+
		"\u0171?\u0001\u0000\u0000\u0000\u0172\u0173\u0005\t\u0000\u0000\u0173"+
		"\u0174\u0005\u001d\u0000\u0000\u0174\u0175\u0005\u001a\u0000\u0000\u0175"+
		"\u0178\u0005\u001b\u0000\u0000\u0176\u0177\u0005\u0014\u0000\u0000\u0177"+
		"\u0179\u0005\u001b\u0000\u0000\u0178\u0176\u0001\u0000\u0000\u0000\u0179"+
		"\u017a\u0001\u0000\u0000\u0000\u017a\u0178\u0001\u0000\u0000\u0000\u017a"+
		"\u017b\u0001\u0000\u0000\u0000\u017b\u017c\u0001\u0000\u0000\u0000\u017c"+
		"\u017d\u0005\u001f\u0000\u0000\u017dA\u0001\u0000\u0000\u0000\u017e\u017f"+
		"\u0005\t\u0000\u0000\u017f\u0180\u0005\u001d\u0000\u0000\u0180\u0181\u0003"+
		"\u0014\n\u0000\u0181\u0184\u0005\u001b\u0000\u0000\u0182\u0183\u0005\u0014"+
		"\u0000\u0000\u0183\u0185\u0005\u001b\u0000\u0000\u0184\u0182\u0001\u0000"+
		"\u0000\u0000\u0185\u0186\u0001\u0000\u0000\u0000\u0186\u0184\u0001\u0000"+
		"\u0000\u0000\u0186\u0187\u0001\u0000\u0000\u0000\u0187\u0188\u0001\u0000"+
		"\u0000\u0000\u0188\u0189\u0005\u001f\u0000\u0000\u0189C\u0001\u0000\u0000"+
		"\u0000\u018a\u018b\u0005\u0007\u0000\u0000\u018b\u018c\u0005\u001d\u0000"+
		"\u0000\u018c\u018d\u0005\u001a\u0000\u0000\u018d\u018e\u0005\u0014\u0000"+
		"\u0000\u018e\u018f\u0005\u001b\u0000\u0000\u018f\u0190\u0005\u001f\u0000"+
		"\u0000\u0190E\u0001\u0000\u0000\u0000\u0191\u0192\u0005\n\u0000\u0000"+
		"\u0192\u0193\u0005\u001d\u0000\u0000\u0193\u0194\u0005\u001a\u0000\u0000"+
		"\u0194\u0195\u0005\u0014\u0000\u0000\u0195\u0196\u0005\u001b\u0000\u0000"+
		"\u0196\u0197\u0005\u001f\u0000\u0000\u0197G\u0001\u0000\u0000\u0000\u0198"+
		"\u0199\u0005\b\u0000\u0000\u0199\u019a\u0005\u001d\u0000\u0000\u019a\u019b"+
		"\u0005\u001a\u0000\u0000\u019b\u019c\u0005\u0014\u0000\u0000\u019c\u019d"+
		"\u0005\u001b\u0000\u0000\u019d\u019e\u0005\u001f\u0000\u0000\u019eI\u0001"+
		"\u0000\u0000\u0000\u019f\u01a0\u0005\u0007\u0000\u0000\u01a0\u01a1\u0005"+
		"\u001d\u0000\u0000\u01a1\u01a2\u0003\u0014\n\u0000\u01a2\u01a3\u0005\u0014"+
		"\u0000\u0000\u01a3\u01a4\u0005\u001b\u0000\u0000\u01a4\u01a5\u0005\u001f"+
		"\u0000\u0000\u01a5K\u0001\u0000\u0000\u0000\u01a6\u01a7\u0005\n\u0000"+
		"\u0000\u01a7\u01a8\u0005\u001d\u0000\u0000\u01a8\u01a9\u0003\u0014\n\u0000"+
		"\u01a9\u01aa\u0005\u0014\u0000\u0000\u01aa\u01ab\u0005\u001b\u0000\u0000"+
		"\u01ab\u01ac\u0005\u001f\u0000\u0000\u01acM\u0001\u0000\u0000\u0000\u01ad"+
		"\u01ae\u0005\b\u0000\u0000\u01ae\u01af\u0005\u001d\u0000\u0000\u01af\u01b0"+
		"\u0003\u0014\n\u0000\u01b0\u01b1\u0005\u0014\u0000\u0000\u01b1\u01b2\u0005"+
		"\u001b\u0000\u0000\u01b2\u01b3\u0005\u001f\u0000\u0000\u01b3O\u0001\u0000"+
		"\u0000\u0000\u01b4\u01b5\u0007\u0000\u0000\u0000\u01b5Q\u0001\u0000\u0000"+
		"\u0000\u01b6\u01b7\u0007\u0001\u0000\u0000\u01b7S\u0001\u0000\u0000\u0000"+
		"\u001cWbqz\u009c\u00a3\u00ac\u00b5\u00c7\u00cb\u00d4\u00de\u00e8\u0100"+
		"\u0107\u0110\u0119\u0122\u012b\u0134\u013d\u0146\u014f\u0158\u0163\u016e"+
		"\u017a\u0186";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}