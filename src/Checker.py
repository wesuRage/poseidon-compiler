from Parser import Parser

class Checker:
  def eval_program(self, program):
    lastEvaluated = {"type": "null", "value": "null"}

    for statement in program["body"]:
      lastEvaluated = self.evaluate(statement)

    return lastEvaluated

  def eval_numeric_binary_expr(self, lhs, rhs, operator):
    pass
    

  def eval_binary_expr(self, binop):
    lhs = self.evaluate(binop["left"])
    rhs = self.evaluate(binop["right"])

    print(rhs)
    if lhs["type"] == "number" and rhs["type"] == "number":
      return self.eval_numeric_binary_expr(lhs, rhs, binop["operator"])
    
    return {"type": "null", "value": "null"}

  def evaluate(self, astNode):
    match astNode["kind"]:
      case "NumericLiteral":
        return {"value": astNode["value"], "type": "number"}
      
      case "BinaryExpr":
        return self.eval_binary_expr(astNode)
      
      case "NullLiteral":
        return {"value": "null", "type": "null"}

      case "Program":
        return self.eval_program(astNode)
      
      case _:
        raise ValueError(f"This astNode hast not ben setup for validation: {astNode}")
      
checker = Parser().produceAST("3 + 2 * 5")
Checker().evaluate(checker)