
from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token
from src.transpilers import toString
import copy
import rich

class UniqueGenerator:
    def __init__(self, program):
        self.program = program
        self.counter = 0
    def __next__(self):
        while f"_{self.counter}_" in self.program: self.counter += 1
        self.counter += 1
        return f"_{self.counter-1}_"

class RemoveSppClasses(Transformer):

    def transform(self, parseTree):
        self.ugen = UniqueGenerator(toString(parseTree))
        self.unique0 = next(self.ugen)
        self.classname2startname = dict()
        return super().transform(parseTree)


    def spplang_start(self, nodes):
        return Tree(Token("RULE","spplang_start"), [sub for node in nodes for sub in (node if isinstance(node,list) else [node])])

    def spplang_class(self, nodes):

        name = nodes[1]
        fields  = [x for node in nodes if isinstance(node,Tree) and node.data == "spplang_field_declaration" for x in [node.children[1], node.children[2], Token("SEMICOLON",";")]]
        methods = [node for node in nodes if isinstance(node,Tree) and node.data == "spplang_function_definition"]
        methodNames = [method.children[2].children[0] for method in methods]
        methodReturnTypes = [Tree(Token("RULE","spplang_rtype"), [Token("__ANON__","->"), method.children[1], Token("RPAR",")")]) for method in methods]
        methodParamTypes  = [[param.children[0] for param in method.children[3].children[1:-1:2]] for method in methods ]
        methodParamTypes = [Tree(Token("RULE","spplang_ptype"),[Token("LPAR","(")] +[x for ptype in methodParamType for x in [ptype, Token("COMMA",",")]][:-1]) for methodParamType in methodParamTypes]
        methodTypes = [Tree(Token("RULE","spplang_pointer"), [Tree(Token("RULE", "spplang_ftype"), [ptype, rtype]), Token("STAR","*")]) for ptype,rtype in zip(methodParamTypes, methodReturnTypes)]
        uniqueNames = [next(self.ugen) for _ in range(len(methods))]
        
        struct = Tree(Token("RULE", "slang_struct"), [
            Token("STRUCT", "struct"), 
            name, 
            Token("WITH", "with"), 
            *copy.deepcopy(fields),
            *[Tree(Token("RULE", "slang_struct_definition"), [
                mtype, 
                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", mname)]), 
                Token("EQUAL", "="), 
                Tree(Token("RULE", "slang_reference"), [Token("AMPERSAND", "&"), Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", muniq+mname)])]),
                Token("SEMICOLON", ";")]) for mname,mtype,muniq in zip(methodNames, methodTypes, uniqueNames)], 
            Token("SEMICOLON", ";")])

        methodCopies = [Transformer().transform(method) for method in methods]
        for method,unique in zip(methodCopies,uniqueNames): method.children[2].children[0] = Token("__ANON__", unique + method.children[2].children[0].value)
        
        return [struct, *methodCopies]

    def spplang_new(self, nodes):
        rest = Tree(Token("RULE", "slang_function_call"), [
            Tree(Token("RULE", "slang_struct_access"), [
                Tree(Token("RULE", "slang_round_parenthesized"), [
                    Token("LPAR", "("), 
                    Tree(Token("RULE", "slang_auto_assignement"), [
                        Token("__ANON__", "auto"),
                        Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                        Token("EQUAL", "="), 
                        Tree(Token("RULE", "slang_struct_value"), [
                            nodes[1], 
                            Token("LBRACE", "{"), 
                            Token("RBRACE", "}")])]), 
                    Token("RPAR", ")")]), 
                Token("DOT", "."), 
                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", "start")])]), 
            Token("LPAR", "("), 
            Tree(Token("RULE", "slang_expression_sequence"), [
                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                *([] if len(nodes) == 4 else [Token("COMMA", ","), *nodes[3].children])]),
            Token("RPAR", ")")])
        return rest



    def spplang_function_call(self, nodes):
        if nodes[0].data == "spplang_struct_access":
            return Tree(Token("RULE", "slang_function_call"), [
                Tree(Token("RULE", "slang_struct_access"), [
                    Tree(Token("RULE", "slang_round_parenthesized"), [
                        Token("LPAR", "("), 
                        Tree(Token("RULE", "slang_auto_assignement"), [
                            Token("AUTO", "auto"), 
                            Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                            Token("EQUAL", "="), 
                            nodes[0].children[0]]), 
                        Token("RPAR", ")")]), 
                    Token("DOT", "."), 
                    nodes[0].children[2]]),
                Token("LPAR", "("), 
                Tree(Token("RULE", "slang_expression_sequence"), [
                    Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)])]), 
                    *([Token("COMMA",",")] if len(nodes) == 4 else []),
                    *nodes[2:-1],
                Token("RPAR", ")")])

        return Tree(Token("RULE","slang_function_call"), nodes)
 


def removeSppClasses(parseTree):
    res = RemoveSppClasses().transform(parseTree)
    return res


