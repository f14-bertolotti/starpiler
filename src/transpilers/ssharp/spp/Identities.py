from lark          import Token
from lark.tree     import Tree
from lark.visitors import v_args

from src.utils import AppliedTransformer

class Identities(AppliedTransformer): 

    @v_args(meta=True)
    def ssharplang_class_access(self, meta, nodes):
        return Tree(Token("RULE","spplang_struct_access"), nodes, meta)

for spprule in ["ssharplang_start", "ssharplang_identifier", "ssharplang_block", "ssharplang_integer", "ssharplang_int64", "ssharplang_return", "ssharplang_declaration_assignment", "ssharplang_expression_sequence"]:
    srule = "spp" + spprule[6:]
    def make(spprule):
        @v_args(meta=True)
        def f(self, meta, children): 
            self.applied = True
            return Tree(Token("RULE", "spp" + spprule[6:]), children, meta)
        f.__name__ = spprule
        return f

    setattr(Identities, spprule, make(spprule))


def identities(parseTree):
    return Identities().transform(parseTree)
