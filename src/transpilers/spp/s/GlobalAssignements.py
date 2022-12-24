from lark.visitors import v_args
from lark.tree     import Tree
from lark          import Token

from src.utils import AppliedTransformer

class GlobalAssignements(AppliedTransformer):

    @v_args(meta=True)
    def spplang_global_assignement(self, meta, nodes):
        self.applied = True    
        return Tree(Token("RULE", "slang_global_assignement"), [
            Token("DEF","def"),
            Tree(Token("RULE", "slang_declaration_assignment"), nodes[1:]),
            Token("SEMICOLON",";")
        ], meta)

def globalAssignements(parseTree):
    return GlobalAssignements().transform(parseTree)
