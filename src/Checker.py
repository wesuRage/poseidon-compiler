from Parser import Parser 

class Checker(Parser):
  def __init__(self) -> None:
    super().__init__()

    self.typedefs = {
      'number': {
        'type': 'native',
        'has+': True,
        'has-': True,
        'has/': True,
        'has*': True,
        'has%': True,
      },
      'null': {
        'type': 'native',
        'has+': False,
        'has-': False,
        'has/': False,
        'has*': False,
        'has%': False
      }

    }
  def getNodeHandler(self, nodetype):
    return Checker.__dict__["eval_" + nodetype]

  def eval_Program(self, sourceCode):
    tree = self.produceAST(sourceCode)
    for stmt in tree["body"]:
      return self.getNodeHandler(stmt["NodeType"])(self, stmt)
  #Expressao
  def eval_NumericLiteral(self, node):
    return 3

  def eval_BinaryExpr(self, node):
    left = node["left"]
    right = node["right"]

    ltype = self.getNodeHandler(left["NodeType"])(self, left)
    rtype = self.getNodeHandler(right["NodeType"])(self, right)

    if not self.supportsOp(ltype, node["operator"]):
      raise TypeError(f"'{ltype}' doesnt supports operation '{node['operator']}'")
    
    if ltype == "null" or rtype == "null":
      raise TypeError("Operations with null values are not allowed.")
    #por enquanto é isso
    return "number"
  
  def supportsOp(self, type, op):
    typedef = self.typedefs[type]

    return typedef["has" + op]
  
  def eval_NullLiteral(self, node):
    return "null"

print(Checker().eval_Program("3 * 4 + 1"))