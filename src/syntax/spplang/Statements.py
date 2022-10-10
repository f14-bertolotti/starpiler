from src.syntax.slang import statement as slangStatement
from src.syntax.spplang import expression, native, identifier

from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor
from src.syntax import getMatchesVisitor


statement = slangStatement.visit(getClonerVisitor(slangStatement)) \
                          .visit(getFindAndReplaceVisitor("slang_expression", expression)) \
                          .visit(getFindAndReplaceVisitor("slang_type", native)) \
                          .visit(getFindAndReplaceVisitor("slang_identifier", identifier)) \
                          .visit(getChangePrefixVisitor("slang_","spplang_"))

block = P(name="spplang_block", rules = [R(statement, mod="*")])
statement.visit(getFindAndReplaceVisitor("spplang_block", block))

declarationAssignement = statement.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_declaration_assignment"))[0]
