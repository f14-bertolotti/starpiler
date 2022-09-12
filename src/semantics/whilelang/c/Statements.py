
#statement   = Production(name="stmt")
#concat      = Production(name="cat", rules=[Rule(statement, "\";\"", statement)])
#assignement = Production(name="assign", rules=[Rule(identifier, "\"=\"", expression)])
#whileloop   = Production(name="while", rules=[Rule("\"while\"", expression, "\"{\"", statement, "\"}\"")])
#ifcondition = Production(name="if", rules=[Rule("\"if\"", expression, "\"{\"", statement, "\"}\"")])
#statement   = statement.append(concat).append(assignement).append(whileloop).append(ifcondition)

def concat(self, tree):
    return f"{tree[0].children[0]}{tree[1].children[0]}"

def assignement(self, tree):
    return f"{tree[0]}={tree[1].children[0]};"

def whileloop(self, tree):
    return f"while({tree[0].children[0]})" + "{" + tree[1].children[0] + "}"

def ifcondition(self, tree):
    return f"if({tree[0].children[0]})" + "{" + tree[1].children[0] + "}"

