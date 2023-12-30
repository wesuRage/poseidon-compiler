from Lexer import *

class Parser: 
  def __init__(self):
    self.tokens = []

  def not_eof(self):
    return self.tokens[0]["type"] != "EOF" 
  
  def at(self):
    return self.tokens[0]
  
  def eat(self):
    return self.tokens.pop(0)
  
  def expect(self, tokenType, error):
    prev = self.eat()

    if prev is None or prev["type"] != tokenType:
      raise SyntaxError(error)

  def produceAST(self, sourceCode):
    self.tokens = Lexer().Tokenize(sourceCode)
    program = {
      "kind": "Program",
      "body": []
    }

    while self.not_eof():
      program["body"].append(self.parse_stmt())

    return program
  
  def parse_stmt(self):
    return self.parse_expr()
  
  def parse_expr(self):
    return self.parse_additive_expr()
  
  def parse_additive_expr(self):
    left = self.parse_multiplicative_expr()

    while self.at()["value"] == "+" or self.at()["value"] == "-":
      operator = self.eat()["value"]
      right = self.parse_multiplicative_expr()
      left = {
        "kind": "BinaryExpr",
        "left": left,
        "right": right,
        "operator": operator
      }

    return left

  def parse_multiplicative_expr(self):
    left = self.parse_primary_expr()

    while self.at()["value"] == "*" or self.at()["value"] == "/":
      operator = self.eat()["value"]
      right = self.parse_primary_expr()
      left = {
        "kind": "BinaryExpr",
        "left": left,
        "right": right,
        "operator": operator
      }

    return left
  
  def parse_primary_expr(self):
    tk = self.at()["type"]

    match tk:
      case "IDENTIFIER":
        return {"kind": "Identifier", "symbol": self.eat()["value"]}
      
      case "NUMBER":
        return {"kind": "NumericLiteral", "value": float(self.eat()["value"])}
      
      case "NULL":
        self.eat()
        return {"kind": "NullLiteral", "value": "null"}
      
      case "OPAREN":
        self.eat()
        value = self.parse_expr()
        self.expect("CPAREN", "Unexpected token inside parenthesised expression. Expected closing parenthesis.")
        return value
      
      case _:
        raise SyntaxError(f"Failed to parse: \"{self.eat()['value']}\"")
