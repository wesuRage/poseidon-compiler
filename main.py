import json
from src.Lexer import Lexer
from src.Parser import Parser

lex = Lexer()
yacc = Parser()

with open("main.px", "r") as f:
  code = "".join(f.readlines())
  
tokens = lex.Tokenize(code)
parsing = yacc.produceAST(tokens) 
print(json.dumps(parsing, indent=2))
