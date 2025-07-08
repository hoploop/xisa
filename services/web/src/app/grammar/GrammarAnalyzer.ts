import { CharStream, CharStreams, CommonTokenStream } from 'antlr4';
import GrammarLexer from './GrammarLexer';
import GrammarParser from './GrammarParser';


export class GrammarAnalyzer {
  public analyze(source: string) {
    const chars = new CharStream(source); // replace this with a FileStream as required
    const lexer = new GrammarLexer(chars);
    const tokens = new CommonTokenStream(lexer);
    const parser = new GrammarParser(tokens);
    const tree = parser.root();
  }

  public highlight(code: string) {
    const inputStream = CharStreams.fromString(code);
    const lexer = new GrammarLexer(inputStream);
    const tokenStream = new CommonTokenStream(lexer);
    tokenStream.fill();

    const tokens = tokenStream.tokens;
    tokens.forEach(token => {
      console.log(token.text, token.type);
      // Map token.type to CSS class or Monaco theme token
    });
  }
}
