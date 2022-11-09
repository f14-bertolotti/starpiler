from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Lark, Token

from src.syntax.slang import functionCall, functionDeclaration, globalAssignement
from src.syntax import Language

functionCallLang      = Lark(Language(       functionCall).toLark(), keep_all_tokens=True)
globalAssignementLang = Lark(Language(  globalAssignement).toLark(), keep_all_tokens=True)
funDeclarationLang    = Lark(Language(functionDeclaration).toLark(), keep_all_tokens=True)

class SppNewToS(Transformer):

    @v_args(meta=True)
    def spplang_start(self, meta, nodes):
        globalAssignements = [node for node in nodes if isinstance(node, Tree) and node.data == "spplang_global_assignement"]
        if not any(ass.children[2].children[0].value == "__malloc" for ass in globalAssignements):
            nodes.insert(0,    funDeclarationLang.parse("def int8* malloc(int64);"))
            nodes.insert(1, globalAssignementLang.parse("def auto __malloc = &malloc;"))
        if not any(ass.children[2].children[0].value == "__memcpy" for ass in globalAssignements):
            nodes.insert(0,    funDeclarationLang.parse("def int8* memcpy(int8*, int8*, int64);"))
            nodes.insert(1, globalAssignementLang.parse("def auto __memcpy = &memcpy;"))
        return Tree(Token("RULE","spplang_start"), nodes, meta)

    @v_args(meta=True)
    def spplang_new(self, meta, nodes):
        newexpr = functionCallLang.parse(f"(auto __ = &__memcpy(&__malloc(size of {nodes[1].children[0].value}), {nodes[1].children[0].value}" + "{}" + f"as int8*, size of {nodes[1].children[0].value}) as {nodes[1].children[0].value}*).start(__)")
        if len(nodes) == 5: newexpr.children[2].children += [Token("COMMA",",")] + nodes[3].children
        return newexpr

def sppNewToS(parseTree):
    return SppNewToS().transform(parseTree)

