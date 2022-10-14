from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getMatchesVisitor
from src.syntax import getClonerVisitor

from src.syntax.slang import expression as slangExpression
from src.syntax.spplang import native, identifier, integer, rational, string


qualification = P(name = "spplang_qualification", rules = [R(identifier, R(T("."), identifier, mod="+"))])
reference     = P(name = "slang_reference"      , rules=[R(T("&"), qualification)])
expression = slangExpression.visit(getClonerVisitor(slangExpression)) \
                            .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                            .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                            .visit(getFindAndReplaceVisitor("slang_integer"    , integer)) \
                            .visit(getFindAndReplaceVisitor("slang_rational"   , rational)) \
                            .visit(getFindAndReplaceVisitor("slang_string"     , string)) \
                            .visit(getFindAndReplaceVisitor("slang_reference"  , reference)) \
                            .visit(getChangePrefixVisitor("slang_"             , "spplang_"))
newExpression = P(name = "spplang_new", rules = [R(T("new"), identifier)])

expression.append(qualification)
expression.append(newExpression)
