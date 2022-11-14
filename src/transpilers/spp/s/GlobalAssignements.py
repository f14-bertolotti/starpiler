from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token

class GlobalAssignements(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res


    @v_args(meta=True)
    def spplang_global_assignement(self, meta, nodes):
        nodes.pop(-1)
        nodes.pop(0)
        self.applied = True    
        return Tree(Token("RULE", "slang_global_assignement"), [
            Token("DEF","def"),
            Tree(Token("RULE", "slang_declaration_assignment"), nodes),
            Token("SEMICOLON",";")
        ], meta)

def globalAssignements(parseTree):
    return GlobalAssignements().transform(parseTree)
