from lark.visitors import v_args, Transformer
from lark.tree     import Tree
from lark          import Lark, Token

from src.syntax.slang import functionCall, functionDeclaration, globalAssignement
from src.syntax       import Language
from src.utils        import NotAppliedException

import copy

functionCallLang      = Lark(Language(       functionCall).toLark(), keep_all_tokens=True)
globalAssignementLang = Lark(Language(  globalAssignement).toLark(), keep_all_tokens=True)
funDeclarationLang    = Lark(Language(functionDeclaration).toLark(), keep_all_tokens=True)

mallocDeclaration =    funDeclarationLang.parse("def int8* malloc(int64);")
mallocAssignement = globalAssignementLang.parse("def (int64 -> int8*)* __malloc = &malloc;")
memcpyDeclaration =    funDeclarationLang.parse("def int8* memcpy(int8*, int8*, int64);")
memcpyAssignement = globalAssignementLang.parse("def (int8*, int8*, int64 -> int8*)* __memcpy = &memcpy;")

newexpression = functionCallLang.parse("(auto __ = __memcpy(__malloc(size of _), _{} as int8*, size of _) as _*).start(__)")

class News(Transformer):

    def __init__(self, *args, **kwargs):
        self.is_spplang_new  = False
        self.additional_decl = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if self.is_spplang_new and not self.additional_decl: raise NotAppliedException() 
        return res 


    @v_args(meta=True)
    def spplang_start(self, meta, nodes):
        globalAssignements = [node for node in nodes if isinstance(node, Tree) and node.data == "slang_global_assignement"]
        if self.is_spplang_new and not any(ass.children[1].children[1].children[0].value == "__malloc" for ass in globalAssignements):
            self.additional_decl = True
            nodes.insert(0, mallocDeclaration)
            nodes.insert(1, mallocAssignement)
        if self.is_spplang_new and not any(ass.children[1].children[1].children[0].value == "__memcpy" for ass in globalAssignements):
            self.additional_decl = True
            nodes.insert(0, memcpyDeclaration)
            nodes.insert(1, memcpyAssignement)
        return Tree(Token("RULE","spplang_start"), nodes, meta)

    @v_args(meta=True)
    def spplang_new(self, meta, nodes):
        newexpr = copy.deepcopy(newexpression)
        newexpr.children[0].children[0].children[1].children[3].children[0].children[2].children[0].children[2].children[0].children[2].children[0] = Token("__ANON__", nodes[1].children[0].value)
        newexpr.children[0].children[0].children[1].children[3].children[0].children[2].children[2].children[0].children[0] = Token("__ANON__", nodes[1].children[0].value)
        newexpr.children[0].children[0].children[1].children[3].children[0].children[2].children[4].children[2].children[0] = Token("__ANON__", nodes[1].children[0].value)
        newexpr.children[0].children[0].children[1].children[3].children[2].children[0].children[0] = Token("__ANON__", nodes[1].children[0].value)
        newexpr.meta.type = meta.type
        if len(nodes) == 5: newexpr.children[2].children += [Token("COMMA",",")] + nodes[3].children
        self.is_spplang_new = True
        return newexpr

def news(parseTree):
    if parseTree.data != "spplang_start": raise ValueError("top level insertions may be required")
    return News().transform(parseTree)

