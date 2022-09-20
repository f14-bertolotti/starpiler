from src.syntax import Production, Language, Rule
from src.syntax.whilelang import expression, identifier, signedInteger


statement   = Production(name="wl_stmt")
concat      = Production(name="wl_cat", rules=[Rule(statement, "\";\"", statement)])
assignement = Production(name="wl_assign", rules=[Rule(identifier, "\"=\"", expression)])
whileloop   = Production(name="wl_while", rules=[Rule("\"while\"", expression, "\"{\"", statement, "\"}\"")])
ifcondition = Production(name="wl_if", rules=[Rule("\"if\"", expression, "\"{\"", statement, "\"}\"")])
statement   = statement.append(concat).append(assignement).append(whileloop).append(ifcondition)


