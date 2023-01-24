from lark import Tree, Token
from src.semantics.types import *
from src.utils import SmallMeta

LinkedNodeType = SType("LinkedNode", {})
LinkedNodeType["next"] = Pointer(LinkedNodeType)
LinkedNodeType["element"] = Pointer(Int8())
LinkedNodeType["bsize"] = Int64()
LinkedNodeType["marked"] = Int64()
LinkedNodeType["start"] = Pointer(FType([Pointer(LinkedNodeType), Pointer(Int8()), Int64()], Pointer(LinkedNodeType)))
LinkedNodeType["isLast"] = Pointer(FType([Pointer(LinkedNodeType)], Int64()))
LinkedNodeType["getLast"] = Pointer(FType([Pointer(LinkedNodeType)],Pointer(LinkedNodeType)))
LinkedNodeType["size"] = Pointer(FType([Pointer(LinkedNodeType)],Int64()))
LinkedNodeType["append"] = Pointer(FType([Pointer(LinkedNodeType),Pointer(LinkedNodeType)],Pointer(LinkedNodeType))) 
LinkedNodeType["print"] = Pointer(FType([Pointer(LinkedNodeType)],Pointer(LinkedNodeType)))
LinkedNodeType["printAll"] = Pointer(FType([Pointer(LinkedNodeType)],Pointer(LinkedNodeType)))
LinkedNodeType["fromElementPointer"] = Pointer(FType([Pointer(LinkedNodeType),Pointer(Int8())],Pointer(LinkedNodeType)))
LinkedNodeType["end"] = Pointer(FType([Pointer(LinkedNodeType)], Void()))

GCType = SType("GC", {})
GCType["node"] = Pointer(LinkedNodeType)
GCType["roots"] = Pointer(LinkedNodeType)
GCType["start"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["push"] = Pointer(FType([Pointer(GCType), Pointer(Int8()), Int64()], Pointer(GCType)))
GCType["pop"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["mark_root"] = Pointer(FType([Pointer(GCType), Pointer(Int8())], Pointer(GCType)))
GCType["mark"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["unmark"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["sweep"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["end"] = Pointer(FType([Pointer(GCType)], Void()))



importMalloc = \
Tree(Token('RULE', 'spplang_import'), [
    Token('FROM', 'from'), 
    Tree(Token('RULE', 'spplang_string'), [Token('__ANON__', '"src/testing/spplang/programs/gc/GC.spp"')]), 
    Token('IMPORT', 'import'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'malloc')]), 
    Token('AS', 'as'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__malloc__')]), 
    Token('SEMICOLON', ';')])

importMemcpy = \
Tree(Token('RULE', 'spplang_import'), [
    Token('FROM', 'from'), 
    Tree(Token('RULE', 'spplang_string'), [Token('__ANON__', '"src/testing/spplang/programs/gc/GC.spp"')]), 
    Token('IMPORT', 'import'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'memcpy')]), 
    Token('AS', 'as'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpy__')]), 
    Token('SEMICOLON', ';')])

gcImport = \
Tree(Token("RULE", "spplang_import"), [
    Token("FROM", "from"), 
    Tree(Token("RULE", "spplang_string"), [Token("__ANON__", "\"src/testing/spplang/programs/gc/GC.spp\"")]), 
    Token("IMPORT", "import"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "GC")]), 
    Token("AS", "as"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "GC")]), 
    Token("SEMICOLON", ";")], SmallMeta(type=GCType))

gcRefImport = \
Tree(Token("RULE", "spplang_import"), [
    Token("FROM", "from"), 
    Tree(Token("RULE", "spplang_string"), [Token("__ANON__", "\"src/testing/spplang/programs/gc/GC.spp\"")]), 
    Token("IMPORT", "import"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "gc")]), 
    Token("AS", "as"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "gc")]), 
    Token("SEMICOLON", ";")], SmallMeta(type=GCType))
