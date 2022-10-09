
from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor

from src.syntax.slang import expression as slangExpression
from src.syntax.spplang import native, identifier, integer, rational, string

expression = slangExpression.visit(getClonerVisitor(slangExpression)) \
                            .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                            .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                            .visit(getFindAndReplaceVisitor("slang_integer"    , integer)) \
                            .visit(getFindAndReplaceVisitor("slang_rational"   , rational)) \
                            .visit(getFindAndReplaceVisitor("slang_string"     , string)) \
                            .visit(getChangePrefixVisitor("slang_"             , "spplang_"))

