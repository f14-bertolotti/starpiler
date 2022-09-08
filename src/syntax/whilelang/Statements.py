from src.syntax import Production, Language, Rule
from src.syntax.whilelang import expression, identifier, signedInteger


statement   = Production(name="stmt")
concat      = Production(name="cat", rules=[Rule(statement, "\";\"", statement)])
assignement = Production(name="assign", rules=[Rule(identifier, "\"=\"", expression)])
whileloop   = Production(name="while", rules=[Rule("\"while\"", expression, "\"{\"", statement, "\"}\"")])
ifcondition = Production(name="if", rules=[Rule("\"if\"", expression, "\"{\"", statement, "\"}\"")])
statement   = statement.append(concat).append(assignement).append(whileloop).append(ifcondition)


