
from lark import Token
from lark.tree import Tree
from lark.visitors import Transformer

class SppToSIdentities(Transformer):
    def __default__(self, token, children, meta):
        if token not in {"spplang_import", "spplang_field_declaration", "spplang_function_call", "spplang_class", "spplang_new"} and token.startswith("spplang"): print(token)
        return Tree(token,children,meta)

for spprule in ['spplang_greater_equal', 'spplang_double', 'spplang_greater', 'spplang_ifthen', 'spplang_string', 'spplang_subtraction', 'spplang_stmt_expr', 'spplang_auto_assignement', 'spplang_less', 'spplang_while', 'spplang_vararg_parameter', 'spplang_multiplication', 'spplang_round_parenthesized', 'spplang_reference_square_parenthesized', 'spplang_cast', 'spplang_indexed', 'spplang_square_parenthesized', 'spplang_return_void', 'spplang_size_of', 'spplang_expression_sequence', 'spplang_void', 'spplang_parameter_seq_decl', 'spplang_reference', 'spplang_int8', 'spplang_block', 'spplang_function_declaration', 'spplang_parameter_declaration', 'spplang_pointer', 'spplang_function_definition', 'spplang_identifier', 'spplang_int64', 'spplang_equality', 'spplang_integer', 'spplang_struct_ref_access', 'spplang_start', 'spplang_return', 'spplang_parameter_seq_def', 'spplang_tname', 'spplang_addition', 'spplang_assignement', 'spplang_declaration_assignment', 'spplang_struct_access', 'spplang_statement', 'spplang_parameter_definition']:
    srule = "s" + spprule[3:]
    def make(spprule):
        def f(self, children): return Tree(Token("RULE", "s" + spprule[3:]), children)
        f.__name__ = spprule
        return f

    setattr(SppToSIdentities, spprule, make(spprule))


def sppToSIdentities(parseTree):
    return SppToSIdentities().transform(parseTree)