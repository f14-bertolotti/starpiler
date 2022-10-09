

from src.syntax.slang import identifier
from src.syntax.slang import rational
from src.syntax.slang import integer
from src.syntax.slang import string

from src.syntax import getClonerVisitor
from src.syntax import getChangePrefixVisitor

identifier = identifier.visit(getClonerVisitor(identifier)) \
                       .visit(getChangePrefixVisitor("slang_", "spplang_"))
rational = rational.visit(getClonerVisitor(rational)) \
                   .visit(getChangePrefixVisitor("slang_", "spplang_"))
integer = integer.visit(getClonerVisitor(integer)) \
                 .visit(getChangePrefixVisitor("slang_", "spplang_"))
string = string.visit(getClonerVisitor(string)) \
               .visit(getChangePrefixVisitor("slang_", "spplang_"))

