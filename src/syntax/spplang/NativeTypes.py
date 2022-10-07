from src.syntax.slang import native as slang_native
from src.syntax import getChangePrefixVisitor

native = slang_native
native.visit(getChangePrefixVisitor("slang_", "spplang_"))

