from src.syntax.slang import native as slang_native
from src.syntax.spplang import identifier

from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor

native = slang_native.visit(getClonerVisitor(slang_native)) \
                     .visit(getChangePrefixVisitor("slang_", "spplang_"))
native.append(identifier)

