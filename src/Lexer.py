import re

class Lexer:
  def __init__(self):
    self.token_definitions = {
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
      "?": "INTERROGATION",
      "&": "AND",
      "null": "NULL",
      "byte": "BYTE",
      "resb": "RESB",
      "label": "LABEL"
    }

    self.tokens_list = []

  def Tokenize(self, source_code: str) -> list:
    tokens_regex = re.compile(r'\w+|.')
    src = tokens_regex.findall(source_code)

    for lexeme in src:
      token_type = self.token_definitions.get(lexeme)
      if token_type:
        self.tokens_list.append({"value": lexeme, "type": self.token_definitions[lexeme]})
      elif lexeme.isdigit():
        self.tokens_list.append({"value": lexeme, "type": "NUMBER"})
      elif lexeme.isidentifier():
        self.tokens_list.append({"value": lexeme, "type": "IDENTIFIER"})
      elif lexeme != " ":
        raise ValueError(f"Erro léxico: Lexema inesperado: {lexeme}")

    self.tokens_list.append({"value": "EOF", "type": "EOF"})
    return self.tokens_list
