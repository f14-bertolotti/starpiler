from lark          import Token
from lark.tree     import Tree
from lark.visitors import v_args

from src.utils import AppliedTransformer

class Identities(AppliedTransformer): 
    pass

for spprule in ["ssharplang_start", "ssharplang_function_call", "ssharplang_less", "ssharplang_multiplication", "ssharplang_equality", "ssharplang_addition", "ssharplang_round_parenthesized", "ssharplang_stmt_expr", "ssharplang_square_parenthesized", "ssharplang_identifier", "ssharplang_tname", "ssharplang_block", "ssharplang_integer", "ssharplang_int64", "ssharplang_return", "ssharplang_declaration_assignment", "ssharplang_expression_sequence"]:
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
