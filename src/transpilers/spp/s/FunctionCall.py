from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.utils import AppliedTransformer

class FunctionCall(AppliedTransformer):

    @v_args(meta=True)
    def slang_function_call(self, meta, nodes):

        if not (nodes[0].data == "slang_struct_access" and \
                nodes[0].meta.type != None and \
                hasattr(nodes[0].meta.type, "base") and \
                hasattr(nodes[0].meta.type.base, "ptypes") and \
                len(nodes[0].meta.type.base.ptypes) > 0  and \
                nodes[0].meta.type.base.ptypes[0] == nodes[0].meta.type): # static method
            
            self.applied = True
            return Tree(Token("RULE","slang_function_call"), nodes, meta)
        

def functionCall(parseTree):
    return FunctionCall().transform(parseTree)

