import re

class Lexer:
  def __init__(self):
    self.tokens = {
      "(": "OPAREN",
      ")": "CPAREN",
      "{": "OBRACE",
      "}": "CBRACE",
      "[": "OBRACKET",
      "]": "CBRACKET",
      ",": "COMMA",
      ".": "DOT",
      ":": "COLON",
      ";": "SEMICOLON",
      "=": "EQUALS",
      "=>": "ARROW",
      ">": "GT",
      "<": "LT",
      "-": "MINUS",
      "+": "PLUS",
      "/": "DIV",
      "*": "MUL",
      "%": "MOD",
      "\\": "BACKSLASH",
      "_": "UNDERLINE",
      "\"": "DQUOTES",
      "'": "SQUOTES",
      "|": "BAR",
      "!": "EXCLAMATION",
      "?": "INTERROGRATION",
      "&": "AND",
      "null": "NULL"
    }

    self.tokensList = []

  def Tokenize(self, sourceCode: str) -> list:
    tokens_regex = re.compile(r'\w+|.')
    src = tokens_regex.findall(sourceCode)

    for lexeme in src:
      token_type = self.tokens.get(lexeme)
      if token_type:
        self.tokensList.append({"value": lexeme, "type": self.tokens[lexeme]})
      elif lexeme.isdigit():
        self.tokensList.append({"value": lexeme, "type": "NUMBER"})
      elif lexeme.isidentifier():
        self.tokensList.append({"value": lexeme, "type": "IDENTIFIER"})
      elif lexeme != " ":
        raise ValueError(f"Erro léxico: Lexema inesperado: {lexeme}")

    self.tokensList.append({"value": "EOF", "type": "EOF"})
    return self.tokensList
