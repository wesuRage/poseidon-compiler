from Parser import Parser

class Checker:
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

  def eval(self, node):
    handler = self.getNodeHandler(node["NodeType"])
    return handler(self, node)


  def eval_Program(self, node):
    for stmt in node["body"]:
      self.eval(stmt)
  #Expressao
  def eval_VarDeclaration(self, node):
    return node

  def eval_NumericLiteral(self, node):
    return node
  
  def eval_Identifier(self, node):
    return node

  def eval_BinaryExpr(self, node):
    left = node["left"]
    right = node["right"]

    ltype = self.eval(left)
    rtype = self.eval(right)

    if not self.supportsOp(ltype, node["operator"]):
      raise TypeError(f"'{ltype}' doesnt supports operation '{node['operator']}'")
    
    if ltype == "null" or rtype == "null":
      raise TypeError("Operations with null values are not allowed.")
    #por enquanto é isso
    return "number"
  
  def supportsOp(self, type, op):
    typedef = self.typedefs[type]

    return typedef["has" + op]

parser = Parser()
checker = Checker()

tree = parser.produceAST("""resv dois;
                         dois = 2;""")