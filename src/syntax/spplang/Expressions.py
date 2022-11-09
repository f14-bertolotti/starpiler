from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getMatchesVisitor
from src.syntax import getClonerVisitor

from src.syntax.slang import expression as slangExpression
from src.syntax.spplang import native, identifier, integer, rational, string


expression = slangExpression.visit(getClonerVisitor(slangExpression)) \
                            .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                            .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                            .visit(getFindAndReplaceVisitor("slang_integer"    , integer)) \
                            .visit(getFindAndReplaceVisitor("slang_rational"   , rational)) \
                            .visit(getFindAndReplaceVisitor("slang_string"     , string)) \
                            .visit(getChangePrefixVisitor("slang_"             , "spplang_")) \

expressionSequence = expression.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_expression_sequence"))[0]


newExpression = P(name = "spplang_new" , rules = [R(T("new"), identifier, T("("), T(")")),
                                                  R(T("new"), identifier, T("("), expressionSequence, T(")"))])

expression.append(newExpression)
