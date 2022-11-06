from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getMatchesVisitor
from src.syntax import getClonerVisitor

from src.syntax.slang import expression as slangExpression
from src.syntax.spplang import native, identifier, integer, rational, string


expressionIdentifier = P(name = "spplang_expression_identifier", rules=[identifier])
expression = slangExpression.visit(getClonerVisitor(slangExpression)) \
                            .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                            .visit(getFindAndReplaceVisitor("slang_identifier" , expressionIdentifier)) \
                            .visit(getFindAndReplaceVisitor("slang_integer"    , integer)) \
                            .visit(getFindAndReplaceVisitor("slang_rational"   , rational)) \
                            .visit(getFindAndReplaceVisitor("slang_string"     , string)) \
                            .visit(getChangePrefixVisitor("slang_"             , "spplang_")) \

expressionSequence = expression.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_expression_sequence"))[0]
structValue = expression.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_struct_value"))[0] 
structValue.rules[0].rule[0] = identifier
structValue.rules[0].rule[2] = identifier
structValue.rules[0].rule[5].rule[1] = identifier
structValue.rules[1].rule[0] = identifier

declarationAssignement = expression.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_declaration_assignment"))[0] 
declarationAssignement.rules[0].rule[1] = identifier
autoAssignement = expression.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_auto_assignement"))[0] 
autoAssignement.rules[0].rule[1] = identifier



newExpression = P(name = "spplang_new" , rules = [R(T("new"), identifier, T("("), T(")")),
                                                  R(T("new"), identifier, T("("), expressionSequence, T(")"))])

expression.append(newExpression)
