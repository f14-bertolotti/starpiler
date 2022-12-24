
from lark          import Token
from lark.tree     import Tree
from lark.visitors import v_args

from src.utils import AppliedTransformer

class Identities(AppliedTransformer):
    pass

for srule in ['slang_struct_declaration', 'slang_array', 'slang_function_call', 'slang_rtype', 'slang_ftype', 'slang_division', 'slang_negative', 'slang_rational', 'slang_less_equal', 'slang_modulo', 'slang_not_equal', 'slang_struct_value', 'slang_global_declaration', 'slang_ptype', 'slang_int32', 'slang_greater_equal', 'slang_double', 'slang_greater', 'slang_ifthen', 'slang_string', 'slang_subtraction', 'slang_stmt_expr', 'slang_auto_assignement', 'slang_less', 'slang_while', 'slang_vararg_parameter', 'slang_multiplication', 'slang_round_parenthesized', 'slang_reference_square_parenthesized', 'slang_cast', 'slang_indexed', 'slang_square_parenthesized', 'slang_return_void', 'slang_size_of', 'slang_expression_sequence', 'slang_void', 'slang_parameter_seq_decl', 'slang_reference', 'slang_int8', 'slang_block', 'slang_function_declaration', 'slang_parameter_declaration', 'slang_pointer', 'slang_function_definition', 'slang_identifier', 'slang_int64', 'slang_equality', 'slang_integer', 'slang_struct_ref_access', 'slang_start', 'slang_return', 'slang_parameter_seq_def', 'slang_tname', 'slang_addition', 'slang_assignement', 'slang_declaration_assignment', 'slang_struct_access', 'slang_statement', 'slang_parameter_definition']:
    def make(srule):
        @v_args(meta=True)
        def f(self, meta, children): 
            self.applied = True
            return Tree(Token("RULE", "spp" + srule[1:]), children, meta)
        f.__name__ = srule
        return f

    setattr(Identities, srule, make(srule))


def identities(parseTree):
    return Identities().transform(parseTree)
