from lark.visitors import v_args, Visitor, Transformer, Interpreter
from lark.tree import Tree
from lark import Token
from src.semantics.types import Double, Int64, Int32, Int8, Void, Pointer, SType, FType
import copy

# TODO check types
class SppType(Visitor):

    def __init__(self, namespace, *args, **kwargs):
        self.namespace = namespace
        super().__init__(*args, **kwargs)

    def spplang_integer(self, tree):
        tree.meta.type = Int64()

    def spplang_rational(self, tree):
        tree.meta.type = Double()
    
    def spplang_array(self, tree):
        # TODO check type consistency
        tree.meta.type = Pointer(tree.children[1].meta.type)

    def spplang_reference(self, tree):
        tree.meta.type = Pointer(tree.children[1].meta.type)

    def spplang_expression_identifier(self, tree):
        if tree.children[0].children[0].value not in self.namespace: raise ValueError(f"Undefined identifier \"{tree.children[0].children[0].value}\" in {tree.meta.start_pos}, {tree.meta.end_pos}")
        tree.meta.type = self.namespace[tree.children[0].children[0].value]

    def spplang_function_call(self, tree):
        if not isinstance(tree.children[0],FType): raise ValueError(f"Not a callable called in {tree.meta.start_pos}, {tree.meta.end_pos}")
    
        if len(tree.children) == 4: # callable with parameters
            if len(tree.children[0].meta.ptype) != len(tree.children[2].type): raise ValueError(f"Incoherent params type number in {tree.meta.start_pos}, {tree.meta.end_pos}")
            if not all(l == r for l,r in zip(tree.children[0].meta.ptype,tree.children[2].type)): raise ValueError(f"Incoherent types in {tree.meta.start_pos}, {tree.meta.end_pos}. Expected: {tree.children[0].meta.ptype}. Got: {tree.children[2].meta.type}")

        if (len(tree.children) == 3 and len(tree.children[0].meta.ptype) != ""): raise ValueError(f"Incoherent params type number in {tree.meta.start_pos}, {tree.meta.end_pos}") 
        
        tree.meta.type = tree.children[0].meta.rtype 
        return Tree(Token("RULE", "spplang_function_call"), tree.children, meta)

    def spplang_cast(self, tree):
        tree.meta.type = tree.children[2].meta.type
        
    def spplang_negative(self, tree):
        tree.meta.type = tree.children[1].meta.type

    def spplang_less_equal(self, tree):
        tree.meta.type = Int64()

    def spplang_less(self, tree):
        tree.meta.type = Int64()

    def spplang_greater_equal(self, tree):
        tree.meta.type = Int64()

    def spplang_greater(self, tree):
        tree.meta.type = Int64()

    def spplang_equality(self, tree):
        tree.meta.type = Int64()

    def spplang_not_equal(self, tree):
        tree.meta.type = Int64()

    def spplang_modulo(self, tree):
        tree.meta.type = tree.children[0].meta.type

    def spplang_division(self, tree):
        tree.meta.type = tree.children[0].meta.type

    def spplang_multiplication(self, tree):
        tree.meta.type = tree.children[0].meta.type

    def spplang_subtraction(self, tree):
        tree.meta.type = tree.children[0].meta.type

    def spplang_addition(self, tree):
        tree.meta.type = tree.children[0].meta.type

    def spplang_assignement(self, tree):
        tree.meta.type = tree.children[0].meta.type.base

    def spplang_declaration_assignment(self, tree):
        self.namespace[tree.children[1].children[0].value] = tree.meta.type = tree.children[0].meta.type

    def spplang_auto_assignment(self, tree):
         self.namespace[tree.children[1].children[0].value] = tree.meta.type = tree.children[4].meta.type

    def spplang_struct_value(self, tree):
        if len(tree.children) == 3: 
            tree.meta.type = self.namespace[tree.children[0].children[0].value]
        elif len(tree.children) == 4:
            idsAndExpr = [node for node in tree.children if isinstance(node,Tree) and node.data in {"spplang_identifier","spplang_expression"}]
            name2expr = {n[0]:n[1].meta.type for i in range(0, len(idsAndExpr)//2) for n in tree.children[i*2:(i+1)*2]}
            tree.meta.type = self.namespace[tree.children[0].children[0].value]
        else:
            raise ValueError("Invalid spplang_struct_value tree")

    def spplang_struct_access(self, tree):
        if tree.children[2].children[0] not in tree.children[0].meta.type: raise ValueError(f"{tree.children[0].meta.type} has no {tree.children[2].children[0]}")
        tree.meta.type = tree.children[0].meta.type[tree.children[1].children[0]]

    def spplang_struct_ref_access(self, tree):
        tree.meta.type = Pointer(self.namespace[tree.children[0].meta.type.base][tree.children[2].children[0].children[0].value])

    def spplang_indexed(self, tree):
        tree.meta.type = tree.children[0].meta.type.base

    def spplang_size_of(self, tree):
        tree.meta.type = Int64()

    def spplang_round_parenthesized(self, tree):
        tree.meta.type = tree.children[1].meta.type

    def spplang_new(self, tree):
        tree.meta.type = self.namespace[tree.children[1].children[0].value]

    def spplang_parameter_declaration(self, tree):
        tree.meta.type = tree.children[0].type

    def spplang_parameter_definition(self, tree):
        self.namespace[tree.children[1].children[0].value] = tree.children[0].meta.type

    def spplang_expression_sequence(self, tree):
        tree.meta.type = [node.meta.type for node in tree.children if isinstance(node,Tree) and node.data=="spplang_expression"]

    def spplang_square_parenthesized(self, tree):
        if tree.children[1].meta.type != Int64: raise ValueError(f"Unexpected type in {tree.meta.start_pos}, {tree.meta.end_pos}. Expected: int64. Got: {tree.children[1].meta.type}")

    def spplang_reference_square_parenthesized(self, tree):
        if tree.children[1].meta.type != Int64: raise ValueError(f"Unexpected type in {tree.meta.start_pos}, {tree.meta.end_pos}. Expected: int64. Got: {tree.children[1].meta.type}")


class SppGlobalTypes(Transformer):

    def __init__(self, *args, **kwargs):
        self.global2type = dict()
        super().__init__(self, *args, **kwargs)

    @v_args(meta=True, inline=True)
    def spplang_ftype(self, meta, ptype, rtype):
        meta.type = FType(ptype, rtype)
        return Tree(Token("RULE","spplang_ftype"), [ptype, rtype], meta)

    @v_args(meta=True, inline=True)
    def spplang_pointer(self, meta, typ, star):
        meta.type = Pointer(typ.meta.type)
        return  Tree(Token("RULE","spplang_pointer"), [typ, star], meta)

    @v_args(meta=True, inline=True)
    def spplang_tname(self, meta, name):
        meta.type = name.children[0].value
        return Tree(Token("RULE","spplang_tname"), [name], meta)

    @v_args(meta=True, inline=True)
    def spplang_void(self, meta, name):
        meta.type = Void()
        return Tree(Token("RULE","spplang_void"), [name], meta)

    @v_args(meta=True, inline=True)
    def spplang_int8(self, meta, name):
        meta.type = Int8()
        return Tree(Token("RULE","spplang_int8"), [name], meta)

    @v_args(meta=True, inline=True)
    def spplang_int32(self, meta, name):
        meta.type = Int32()
        return Tree(Token("RULE","spplang_int32"), [name], meta)

    @v_args(meta=True, inline=True)
    def spplang_int64(self, meta, name):
        meta.type = Int64()
        return Tree(Token("RULE","spplang_int64"), [name], meta)

    @v_args(meta=True, inline=True)
    def spplang_double(self, meta, name):
        meta.type = Double()
        return Tree(Token("RULE","spplang_double"), [name], meta)

    @v_args(meta=True)
    def spplang_class(self, meta, nodes):
        meta.type = SType(nodes[1].children[0].value, {node.children[2].children[0].value:node.children[1].meta.type for node in nodes[3:-1]})
        if nodes[1].children[0].value in self.global2type: raise ValueError(f"Redefined global name \"{nodes[1].children[0].value}\"")
        self.global2type[nodes[1].children[0].value] = meta.type
        return Tree(Token("RULE", "spplang_class"), nodes, meta)

    @v_args(meta=True)
    def spplang_function_definition(self, meta, nodes):
        meta.type = FType([node.children[0].meta.type for node in nodes[3].children if isinstance(node,Tree) and node.data == "spplang_parameter_definition"], nodes[1].meta.type)
        self.global2type[nodes[2].children[0].value] = meta.type
        if nodes[1].children[0].value in self.global2type: raise ValueError(f"Redefined global name \"{nodes[1].children[0].value}\"")
        return Tree(Token("RULE", "spplang_function_definition"), nodes, meta)

    @v_args(meta=True)
    def spplang_global_assignement(self, meta, nodes):
        meta.type = nodes[1].meta.type 
        self.global2type[nodes[2].children[0].value] = meta.type
        if nodes[1].children[0].value in self.global2type: raise ValueError(f"Redefined global name \"{nodes[1].children[0].value}\"")
        return Tree(Token("RULE", "spplang_function_definition"), nodes, meta)

    # TODO import

class NameSpace(Interpreter):
    def __init__(self, globals2type):
        self.currentNameSpace = globals2type
        super().__init__()

    def spplang_class(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace
        
    def spplang_function_definition(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_ifthen(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_while(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_parameter_definition(self, tree):
        tree.meta.type = self.currentNameSpace[tree.children[1].children[0].value] = tree.children[0].meta.type
        self.visit_children(tree)

    def spplang_method_definition(self, tree):
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = FType([node.children[0].meta.type for node in tree.children[3].children if isinstance(node,Tree) and node.data == "spplang_parameter_definition"], tree.children[1].meta.type)
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_field_definition(self, tree):
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = tree.children[1].meta.type

    def spplang_field_declaration(self, tree):
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = tree.children[1].meta.type
        
    def spplang_stmt_expr(self, tree):
        #if tree.children[0].data in {"spplang_declaration_assignment", "spplang_auto_assignment"}:
        #    tree.children[0].meta.type = self.currentNameSpace[tree.children[0].children[1].children[0].children[0].value] = SppType(self.currentNameSpace).visit(tree.children[0].children[3]).meta.type
        #else:
        tree.meta.type = SppType(self.currentNameSpace).visit(tree.children[0]).meta.type


class ToSringTransformer(Transformer):
        
    def __default__(self, data, children, meta):
        result = super().__default__(data, children, meta)
        result.string = " ".join([child.value if isinstance(child, Token) else child.string for child in children]) 
        if hasattr(meta, "type"): result.string = f"[{meta.type} {result.string}]"
        return result
        
    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs).string


def sppTypes(parseTree):
    transformer = SppGlobalTypes()
    parseTree = transformer.transform(parseTree)
    NameSpace(transformer.global2type).visit(parseTree)
    print(ToSringTransformer().transform(parseTree))
    return transformer.global2type
 



