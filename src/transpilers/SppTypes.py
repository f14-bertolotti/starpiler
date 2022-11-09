from lark.visitors import v_args, Visitor, Transformer, Interpreter
from lark.tree import Tree
from lark import Token
from src.semantics.types import Double, Int64, Int32, Int8, Void, Pointer, SType, FType
from src.syntax.spplang import lang as spplang
from pathlib import Path

class NativeTypes(Visitor):
    def __init__(self, namespace, *args, **kwargs):
        self.namespace = namespace
        super().__init__(*args, **kwargs)

    def spplang_ftype(self, tree):
        tree.meta.type = FType(tree.children[0].meta.type, tree.children[1].meta.type)

    def spplang_ptype(self, tree):
        tree.meta.type = [node.meta.type for node in tree.children if isinstance(node, Tree)]

    def spplang_rtype(self, tree):
        tree.meta.type = tree.children[1].meta.type

    def spplang_pointer(self, tree):
        tree.meta.type = Pointer(tree.children[0].meta.type)

    def spplang_tname(self, tree):
        tree.meta.type = self.namespace[tree.children[0].children[0].value]

    def spplang_void(self, tree):
        tree.meta.type = Void()

    def spplang_int8(self, tree):
        tree.meta.type = Int8()

    def spplang_int32(self, tree):
        tree.meta.type = Int32()

    def spplang_int64(self, tree):
        tree.meta.type = Int64()

    def spplang_double(self, tree):
        tree.meta.type = Double()

    def spplang_identfier(self, tree):
        if tree.children[0].value in self.namespace: tree.meta.type = tree.children[0].value

class ExpressionType(NativeTypes):
    def __init__(self, namespace, *args, **kwargs):
        super().__init__(namespace, *args, **kwargs)

    def spplang_integer(self, tree):
        tree.meta.type = Int64()

    def spplang_rational(self, tree):
        tree.meta.type = Double()
    
    def spplang_array(self, tree):
        tree.meta.type = Pointer(tree.children[1].meta.type)

    def spplang_reference(self, tree):
        tree.meta.type = Pointer(tree.children[1].meta.type)

    def spplang_identifier(self, tree):
        if tree.children[0].value in self.namespace: 
            tree.meta.type = self.namespace[tree.children[0].value]

    def spplang_function_call(self, tree):
        if not isinstance(tree.children[0].meta.type,Pointer) and \
           not isinstance(tree.children[0].meta.type.base, FType) : 
            raise ValueError(f"Not a callable called in {tree.meta.start_pos}, {tree.meta.end_pos}")
        tree.meta.type = tree.children[0].meta.type.base.rtype 

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
            tree.meta.type = self.namespace[tree.children[0].value]
        elif len(tree.children) == 4:
            idsAndExpr = [node for node in tree.children if isinstance(node,Tree) and node.data in {"spplang_identifier","spplang_expression"}]
            name2expr = {n[0]:n[1].meta.type for i in range(0, len(idsAndExpr)//2) for n in tree.children[i*2:(i+1)*2]}
            tree.meta.type = self.namespace[tree.children[0].value]
        else:
            raise ValueError("Invalid spplang_struct_value tree")

    def spplang_struct_access(self, tree):
        tree.meta.type = tree.children[0].meta.type.base[tree.children[2].children[0].value]

    def spplang_struct_ref_access(self, tree):
        tree.meta.type = Pointer(tree.children[0].meta.type.base[tree.children[2].children[0].value])

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

class ClassType(NativeTypes):
    def __init__(self, namespace, *args, **kwargs):
        super().__init__(namespace, *args, **kwargs)

    def spplang_method_definition(self, tree):
        tree.meta.type = Pointer(FType([node.meta.type for node in tree.children[3].children if isinstance(node,Tree) and node.data == "spplang_parameter_definition"], 
                                       tree.children[1].meta.type))

    def spplang_parameter_definition(self, tree):
        tree.meta.type = tree.children[0].meta.type
 
    def spplang_field_definition(self, tree):
        tree.meta.type = tree.children[1].meta.type

    def spplang_field_declaration(self, tree):
        tree.meta.type = tree.children[1].meta.type

class FunctionDeclarationType(NativeTypes):
    def __init__(self, namespace, *args, **kwargs):
        super().__init__(namespace, *args, **kwargs)

    def spplang_parameter_declaration(self, tree):
        if tree.children[0].data != "spplang_vararg_parameter": tree.meta.type = tree.children[0].meta.type

class FunctionDefinitionType(NativeTypes):
    def __init__(self, namespace, *args, **kwargs):
        super().__init__(namespace, *args, **kwargs)

    def spplang_parameter_definition(self, tree):
        if tree.children[0].data != "spplang_vararg_parameter": tree.meta.type = tree.children[0].meta.type

class NameSpace(Interpreter):
    def __init__(self, *args, **kwargs):
        self.currentNameSpace = dict()
        super().__init__(*args, **kwargs)

    def spplang_class(self, tree):
        tree.meta.type = self.currentNameSpace[tree.children[1].children[0].value] = SType(tree.children[1].children[0].value,dict())
        ClassType(self.currentNameSpace).visit(tree)

        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        for node in tree.children[3:-1]:
            if isinstance(node, Tree) and node.data in {"spplang_method_definition", "spplang_field_definition", "spplang_field_declaration"}:
                tree.meta.type[node.children[2].children[0].value] = node.meta.type
                self.currentNameSpace[node.children[2].children[0].value] = node.meta.type
            else: raise ValueError(f"Unexpected node {node}")

        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_function_declaration(self, tree):
        FunctionDeclarationType(self.currentNameSpace).visit(tree)
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = \
            FType([node.children[0].meta.type for node in tree.children[3].children if isinstance(node,Tree) and \
                                                                                       node.data == "spplang_parameter_declaration" and \
                                                                                       node.children[0].data != "spplang_vararg_parameter"], 
                  tree.children[1].meta.type, 
                  vararg = any([isinstance(node,Tree) and node.data == "spplang_vararg_parameter" for node in tree.children[3].children]))



    def spplang_global_assignement(self, tree):
        NativeTypes(self.currentNameSpace).visit(tree)
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = tree.children[1].meta.type
        
    def spplang_function_definition(self, tree):
        FunctionDefinitionType(self.currentNameSpace).visit(tree)
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = FType([node.meta.type for node in tree.children[3].children if isinstance(node, Tree)],
                                                                                           tree.children[1].meta.type)
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace, **{node.children[1].children[0].value : node.meta.type for node in tree.children[3].children if isinstance(node,Tree) and node.data == "spplang_parameter_definition"}}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_method_definition(self, tree):
        FunctionDefinitionType(self.currentNameSpace).visit(tree)
        tree.meta.type = self.currentNameSpace[tree.children[2].children[0].value] = tree.children[1].meta.type
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace, **{node.children[1].children[0].value : node.meta.type for node in tree.children[3].children if isinstance(node,Tree) and node.data == "spplang_parameter_definition"}}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_import(self, tree):
        path = tree.children[1].children[0].value[1:-1]
        oldname = tree.children[3].children[0].value
        newname = tree.children[5].children[0].value
        importTree = spplang.parse(Path(path).read_text())
        namespace = NameSpace()
        namespace.visit(importTree)
        namespace.currentNameSpace[oldname].name = newname
        tree.meta.type = namespace.currentNameSpace[oldname]

    def spplang_ifthen(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_while(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_stmt_expr(self, tree):
        tree.meta.type = ExpressionType(self.currentNameSpace).visit(tree.children[0]).meta.type

    def spplang_return(self, tree):
        tree.meta.type = ExpressionType(self.currentNameSpace).visit(tree.children[1]).meta.type

def sppTypes(parseTree):
    parseTree = Transformer().transform(parseTree)
    NameSpace().visit(parseTree)
    return parseTree
 



