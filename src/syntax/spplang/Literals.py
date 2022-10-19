from src.syntax import Production as P
from src.syntax import Terminal as T
from src.syntax import Rule as R

from src.syntax.slang import rational
from src.syntax.slang import integer
from src.syntax.slang import string

from src.syntax import getClonerVisitor
from src.syntax import getChangePrefixVisitor


identifier = P(name = "spplang_identifier", rules = [R(T("(?!size|of|new|auto|return|if|while)[a-z_A-Z]\w*", regex=True))]) 
rational = rational.visit(getClonerVisitor(rational)) \
                   .visit(getChangePrefixVisitor("slang_", "spplang_"))
integer = integer.visit(getClonerVisitor(integer)) \
                 .visit(getChangePrefixVisitor("slang_", "spplang_"))
string = string.visit(getClonerVisitor(string)) \
               .visit(getChangePrefixVisitor("slang_", "spplang_"))

