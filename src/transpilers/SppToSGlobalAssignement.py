from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token

class SppToSGlobalAssignement(Transformer):

    @v_args(meta=True)
    def spplang_global_assignement(self, meta, nodes):
        nodes.pop(-1)
        nodes.pop(0)
        return Tree(Token("RULE", "slang_global_assignement"), [
            Token("DEF","def"),
            Tree(Token("RULE", "slang_declaration_assignment"), nodes),
            Token("SEMICOLON",";")
        ], meta)

def sppToSGlobalAssignement(parseTree):
    return SppToSGlobalAssignement().transform(parseTree)
