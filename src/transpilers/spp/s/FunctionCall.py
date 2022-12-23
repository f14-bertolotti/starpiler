from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token

class FunctionCall(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res

    @v_args(meta=True)
    def slang_function_call(self, meta, nodes):

        if not (nodes[0].data == "slang_struct_access" and \
                len(nodes[0].meta.type.base.ptypes) > 0  and \
                nodes[0].meta.type.base.ptypes[0] == nodes[0].meta.type): # static method
            
            self.applied = True
            return Tree(Token("RULE","slang_function_call"), nodes, meta)
        

def functionCall(parseTree):
    return FunctionCall().transform(parseTree)

