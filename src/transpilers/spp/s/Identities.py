
from lark import Token
from lark.tree import Tree
from lark.visitors import v_args, Transformer
import copy

class Identities(Transformer):
    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res

for spprule in ['spplang_start', 'spplang_struct_declaration', 'spplang_array', 'spplang_rtype', 'spplang_ftype', 'spplang_division', 'spplang_negative', 'spplang_rational', 'spplang_less_equal', 'spplang_modulo', 'spplang_not_equal', 'spplang_struct_value', 'spplang_global_declaration', 'spplang_ptype', 'spplang_int32', 'spplang_greater_equal', 'spplang_double', 'spplang_greater', 'spplang_ifthen', 'spplang_string', 'spplang_subtraction', 'spplang_stmt_expr', 'spplang_auto_assignement', 'spplang_less', 'spplang_while', 'spplang_vararg_parameter', 'spplang_multiplication', 'spplang_round_parenthesized', 'spplang_reference_square_parenthesized', 'spplang_cast', 'spplang_indexed', 'spplang_square_parenthesized', 'spplang_return_void', 'spplang_size_of', 'spplang_expression_sequence', 'spplang_void', 'spplang_parameter_seq_decl', 'spplang_reference', 'spplang_int8', 'spplang_block', 'spplang_function_declaration', 'spplang_parameter_declaration', 'spplang_pointer', 'spplang_function_definition', 'spplang_identifier', 'spplang_int64', 'spplang_equality', 'spplang_integer', 'spplang_struct_ref_access', 'spplang_return', 'spplang_parameter_seq_def', 'spplang_tname', 'spplang_addition', 'spplang_assignement', 'spplang_declaration_assignment', 'spplang_struct_access', 'spplang_statement', 'spplang_parameter_definition']:
    srule = "s" + spprule[3:]
    def make(spprule):
        @v_args(meta=True)
        def f(self, meta, children): 
            self.applied = True
            return Tree(Token("RULE", "s" + spprule[3:]), children, meta)
        f.__name__ = spprule
        return f

    setattr(Identities, spprule, make(spprule))


def identities(parseTree):
    return Identities().transform(parseTree)
