
from lark.visitors import v_args, Interpreter, Transformer, Visitor
from src.semantics.types import Type, Double, Array, Object, Int64, Int32, Int8, Void, SType, FType
from src.syntax.ssharplang import lang as ssharplang
from lark.tree import Tree
from src.utils import CloneTransformer

from pathlib import Path

@v_args(tree=True)
class Types(Transformer):
    
    def __init__(self, namespace:dict[str,Type], *args, **kwargs):
        self.namespace = namespace
        super().__init__(*args, **kwargs)

    def ssharplang_tname(self, tree):
        tree.meta.type = tree.children[0].meta.type
        return tree

    def ssharplang_integer(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_rational(self, tree):
        tree.meta.type = Double()
        return tree

    def ssharplang_string(self, tree):
        tree.meta.type = Array(Int8())
        return tree

    def ssharplang_void(self, tree):
        tree.meta.type = Void()
        return tree

    def ssharplang_int8(self, tree):
        tree.meta.type = Int8()
        return tree

    def ssharplang_int32(self, tree):
        tree.meta.type = Int32()
        return tree

    def ssharplang_int64(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_double(self, tree):
        tree.meta.type = Double()
        return tree

    def ssharplang_ftype(self, tree):
        tree.meta.type = FType(tree.children[0].meta.type, tree.children[1].meta.type)
        return tree

    def ssharplang_ptype(self, tree):
        tree.meta.type = [child.meta.type for child in tree.children if isinstance(child, Tree)]
        return tree

    def ssharplang_rtype(self, tree):
        tree.meta.type = tree.children[1].meta.type
        return tree

    def ssharplang_atype(self, tree):
        tree.meta.type = Array(tree.children[0].meta.type)
        return tree

    def ssharplang_new_of(self, tree):
        tree.meta.type = Array(tree.children[3].meta.type)
        return tree

    def ssharplang_field_definition(self, tree):
        self.namespace[tree.children[2].children[0].value] = tree.children[2].meta.type = tree.meta.type = tree.children[1].meta.type
        return tree

    def ssharplang_method_definition(self, tree):
        self.namespace[tree.children[2].children[0].value] = tree.meta.type = tree.children[1].meta.type
        return tree

    def ssharplang_identfier(self, tree):
        if tree.children[0].value in self.namespace: tree.meta.type = tree.children[0].value
        return tree

    def ssharplang_array(self, tree):
        tree.meta.type = Array(tree.children[1].meta.type)
        return tree

    def ssharplang_reference(self, tree):
        tree.meta.type = Array(tree.children[1].meta.type)
        return tree

    def ssharplang_identifier(self, tree):
        if tree.children[0].value in self.namespace: tree.meta.type = self.namespace[tree.children[0].value]
        return tree

    def ssharplang_function_call(self, tree):
        if not isinstance(tree.children[0].meta.type, FType) : 
            raise ValueError(f"Not a callable called in {tree.meta}")
        tree.meta.type = tree.children[0].meta.type.rtype 
        return tree

    def ssharplang_cast(self, tree):
        tree.meta.type = tree.children[2].meta.type
        return tree
        
    def ssharplang_negative(self, tree):
        tree.meta.type = tree.children[1].meta.type
        return tree

    def ssharplang_less_equal(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_less(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_greater_equal(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_greater(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_equality(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_not_equal(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_modulo(self, tree):
        tree.meta.type = tree.children[0].meta.type
        return tree

    def ssharplang_division(self, tree):
        tree.meta.type = tree.children[0].meta.type
        return tree

    def ssharplang_multiplication(self, tree):
        tree.meta.type = tree.children[0].meta.type
        return tree

    def ssharplang_subtraction(self, tree):
        tree.meta.type = tree.children[0].meta.type
        return tree

    def ssharplang_addition(self, tree):
        tree.meta.type = tree.children[0].meta.type
        return tree

    def ssharplang_assignement(self, tree):
        if tree.children[0].meta.type == None or tree.children[2].meta.type == None: return tree
        if tree.children[0].meta.type != tree.children[2].meta.type: raise ValueError(f"Type mismatch in {tree.meta}")
        tree.meta.type = tree.children[2].meta.type
        return tree

    def ssharplang_declaration_assignment(self, tree):
        self.namespace[tree.children[1].children[0].value] = tree.children[1].meta.type = tree.children[0].meta.type.base if isinstance(tree.children[0].meta.type, Object) else tree.children[0].meta.type
        return tree

    def ssharplang_auto_assignement(self, tree):
        self.namespace[tree.children[1].children[0].value] = tree.children[1].meta.type = tree.children[3].meta.type
        return tree

    def ssharplang_indexed(self, tree):
        cur = tree.children[0].meta.type
        for node in tree.children:
            if cur == None: raise ValueError("Invalid type")
            if node.data == "ssharplang_square_parenthesized": cur = cur.base
        tree.meta.type = cur
        return tree

    def ssharplang_size_of(self, tree):
        tree.meta.type = Int64()
        return tree

    def ssharplang_new(self, tree):
        if tree.children[1].children[0].value in self.namespace and isinstance(self.namespace[tree.children[1].children[0].value], Object): 
            tree.meta.type = self.namespace[tree.children[1].children[0].value].base
        return tree

    def ssharplang_parameter_definition(self, tree):
        self.namespace[tree.children[1].children[0].value] = tree.children[0].meta.type
        return tree

    def ssharplang_expression_sequence(self, tree):
        tree.meta.type = [node.meta.type for node in tree.children if isinstance(node,Tree) and node.data=="ssharplang_expression"]
        return tree

    def ssharplang_square_parenthesized(self, tree):
        if tree.children[1].meta.type != Int64(): raise ValueError(f"Unexpected type in {tree.meta.start_pos}, {tree.meta.end_pos}. Expected: int64. Got: {tree.children[1].meta.type}")
        return tree

    def ssharplang_round_parenthesized(self, tree):
        tree.meta.type = tree.children[1].meta.type
        return tree

    def ssharplang_class_access(self, tree):
        if tree.children[0].meta.type != None:
            tree.meta.type = tree.children[0].meta.type.base[tree.children[2].children[0].value]
        return tree


class NameSpace(Interpreter):
    cachedPaths: dict[str, Tree] = dict()
    def __init__(self, *args, **kwargs):
        self.currentNameSpace: dict[str, Type] = dict()
        self.declaredClass = False
        super().__init__(*args, **kwargs)

#    def visit(self, parseTree) -> Tree:
#        parseTree = Types({}).transform(parseTree)
#        return super().visit(parseTree)

    def ssharplang_class_definition(self, tree):
#        print("-"*100)
#        print(tree.meta.type)

        if self.declaredClass: raise ValueError("One class per file allowed. Declared multiple classes")
        self.declaredClass = True
        tree.meta.type = self.currentNameSpace[tree.children[1].children[0].value] = tree.children[1].meta.type = Object(SType(tree.children[1].children[0].value, dict()))

        tree = Types(self.currentNameSpace).transform(tree)

        for child in tree.children[3:-1]:
            if isinstance(child, Tree) and child.data in {"ssharplang_method_definition", "ssharplang_field_definition"}:
                self.currentNameSpace[child.children[2].children[0].value] = child.meta.type
                tree.meta.type.base  [child.children[2].children[0].value] = child.meta.type
            else: raise ValueError(f"Unexpected node {child}")

        self.visit_children(tree)

    def ssharplang_method_definition(self, tree):
        namespace = {**self.currentNameSpace, **dict(zip([x.children[0].value for x in tree.children[3].children[1:-1] if isinstance(x,Tree)], tree.meta.type.ptypes))}
        Types(namespace).transform(tree)
        self.visit_children(tree)

    def ssharplang_import(self, tree):
        path = tree.children[1].children[0].value[1:-1]
        oldname = tree.children[3].children[0].value
        newname = tree.children[5].children[0].value

        namespace = NameSpace()
        if path in NameSpace.cachedPaths:
            importTree = NameSpace.cachedPaths[path]
        else:
            importTree = ssharplang.parse(Path(path).read_text())
            NameSpace.cachedPaths[path] = importTree

        namespace.visit(importTree)
        namespace.currentNameSpace[oldname].name = newname
        self.currentNameSpace[newname] = tree.children[3].meta.type = tree.children[5].meta.type = namespace.currentNameSpace[oldname]

    def spplang_ifthen(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        Types(self.currentNameSpace).visit(tree.children[1])
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

    def spplang_while(self, tree):
        self.currentNameSpace, tmpNameSpace = {**self.currentNameSpace}, self.currentNameSpace
        Types(self.currentNameSpace).visit(tree.children[1])
        self.visit_children(tree)
        self.currentNameSpace = tmpNameSpace

def types(parseTree) -> Tree:
    parseTree = CloneTransformer(notypes=True).transform(parseTree)
    NameSpace().visit(parseTree)
    return parseTree
 

