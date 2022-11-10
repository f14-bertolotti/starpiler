from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Lark, Token

from src.semantics.types import Pointer
class SppStructAccessToS(Transformer):

    @v_args(meta=True)
    def spplang_struct_access(self, meta, nodes):
        if not isinstance(nodes[0].meta.type, Pointer) or \
           nodes[2].children[0].value not in nodes[0].meta.type.base: 
            raise ValueError(f"Type {nodes[0].meta.type.base} has not identifier {nodes[2].children[0].value}")
        return Tree(Token("RULE","spplang_struct_access"), nodes, meta)

    @v_args(meta=True)
    def spplang_function_call(self, meta, nodes):

        if nodes[0].data == "spplang_struct_access" and \
           len(nodes[0].meta.type.base.ptypes) > 0  and \
           nodes[0].meta.type.base.ptypes[0] == nodes[0].children[0].meta.type: # non-static method
    
            basicCall = Tree(Token("RULE", "slang_function_call"), [
                Tree(Token("RULE", "slang_struct_access"), [
                    Tree(Token("RULE", "slang_round_parenthesized"), [
                        Token("LPAR", "("),
                        Tree(Token("RULE", "slang_auto_assignement"), [
                            Token("AUTO", "auto"),
                            Tree(Token("RULE","slang_identifier"), [Token("__ANON__", "__")]),
                            Token("EQUAL", "="),
                            nodes[0].children[0]
                        ], nodes[0].children[0].meta),
                        Token("RPAR",")")
                    ]),
                    Token("DOT", "."),
                    nodes[0].children[2]
                ], nodes[0].children[2].meta),
                Token("LPAR", "("),
                Tree(Token("RULE", "slang_expression_sequence"), [
                    Tree(Token("RULE","slang_identifier"), [Token("__ANON__", "__")])
                ]),
                Token("RPAR", ")")
            ], meta)
            if len(nodes) == 4: basicCall.children[2].children += [Token("COMMA",",")] + nodes[2].children
            return basicCall
        
        return Tree(Token("RULE","slang_function_call"), nodes, meta)

def sppStructAccessToS(parseTree):
    return SppStructAccessToS().transform(parseTree)

