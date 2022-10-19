
from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token
from src.transpilers import toString
import copy
import rich

class RemoveSppClasses(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    def transform(self, parseTree):
        self.string = toString(parseTree)
        while f"_{self.counter}" in self.string: self.counter += 1
        self.unique = f"_{self.counter}"
        self.counter += 1
        return super().transform(parseTree)

    def __default__(self, data, children, meta):
        return {"tree": Tree(data, [child["tree"] if isinstance(child,dict) else child for child in children], meta),
                "assignements": [asgn for child in children for asgn in (child["assignements"] if isinstance(child, dict) else [])]} if any(isinstance(child,dict) for child in children) else super().__default__(data, children, meta)

    def spplang_class(self, nodes):

        name = nodes[1]
        fields  = [x for node in nodes if isinstance(node,Tree) and node.data == "spplang_field_declaration" for x in [node.children[1], node.children[2],Token("SEMICOLON",";")]]
        methods = [node for node in nodes if isinstance(node,Tree) and node.data == "spplang_function_definition"]
        methodNames = [method.children[2] for method in methods]
        methodReturnTypes = [Tree(Token("RULE","spplang_rtype"), [Token("__ANON__","->"), method.children[1], Token("RPAR",")")]) for method in methods]
        methodParamTypes  = [[param.children[0] for param in method.children[3].children[1:-1:2]] for method in methods ]
        methodParamTypes = [Tree(Token("RULE","spplang_ptype"),[Token("LPAR","(")] +[x for ptype in methodParamType for x in [ptype, Token("COMMA",",")]][:-1]) for methodParamType in methodParamTypes]
        methodTypes = [Tree(Token("RULE","spplang_pointer"), [Tree(Token("RULE", "spplang_ftype"), [ptype, rtype]), Token("STAR","*")]) for ptype,rtype in zip(methodParamTypes, methodReturnTypes)]
        
        struct = Tree(Token("RULE", "spplang_struct"), [
            Token("STRUCT", "struct"), 
            Tree(Token("RULE","spplang_identifier"), [Token("__ANON__", name.children[0].value)]),
            Token("WITH", "with"),
            *copy.deepcopy(fields),
            *[copy.deepcopy(x) for mtype, mname in zip(methodTypes, methodNames) for x in [mtype, mname, Token("SEMICOLON",";")]],
            Token("SEMICOLON", ";")])

        # ASSIGN FUNCTION TO METHODS IN START FUNCTION
        startMethods = list(filter(lambda x:x.children[2].children[0].value == "start", methods))
        assert len(startMethods) == 1
        start = startMethods[0]
        start.children[5].children = [Tree(Token('RULE', 'spplang_assignement'), [
            Tree(Token('RULE', 'spplang_struct_ref_access'), [Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_0', 'this')]), Token('__ANON__', '&.'), copy.deepcopy(method.children[2])]), 
            Token('EQUAL', '='), 
            Tree(Token('RULE', 'spplang_reference'), [Token('AMPERSAND', '&'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', method.children[2].children[0].value + name.children[0].value)])]), 
            Token('SEMICOLON', ';')]) for method in methods] + start.children[5].children 

        methodCopies = [Transformer().transform(method) for method in methods]
        for method in methodCopies: method.children[2].children[0].value = method.children[2].children[0].value + name.children[0].value
        return {"tree": struct,
                "methods" : methodCopies}

    def spplang_start(self, nodes):
        methods = [node["methods"] if isinstance(node, dict) else [] for node in nodes]
        trees = [node["tree"] if isinstance(node, dict) else node for node in nodes]
        return Tree(Token("RULE","spplang_start"), [x for tree,method in zip(trees,methods) for x in [tree,*method]])

    def spplang_new(self, nodes):
        return Tree(Token('RULE', 'slang_function_call'), [
            Tree(Token("RULE", "slang_reference"), [Token("AMPERSAND","&"), Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', f'start{nodes[1].children[0].value}')])]), 
            Token('LPAR', '('), 
            Tree(Token('RULE', 'slang_expression_sequence'), [
                Tree(Token('RULE', 'slang_struct_value'), [nodes[1], Token('LBRACE', '{'), Token('RBRACE', '}')]), 
                Token('COMMA', ','), 
                nodes[3]]), 
            Token('RPAR', ')')])


    def spplang_function_call(self, nodes):
        if nodes[0].data == "spplang_struct_access":
            return Tree(Token('RULE', 'slang_function_call'), [
                Tree(Token('RULE', 'slang_struct_access'), [
                    Tree(Token('RULE', 'slang_round_parenthesized'), [
                        Token('LPAR', '('), 
                        Tree(Token('RULE', 'slang_auto_assignement'), [
                            Token('AUTO', 'auto'), 
                            Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', self.unique)]), 
                            Token('EQUAL', '='), 
                            nodes[0].children[0]]), 
                        Token('RPAR', ')')]), 
                    Token('DOT', '.'), 
                    nodes[0].children[2]]),
                Token('LPAR', '('), 
                Tree(Token('RULE', 'slang_expression_sequence'), [
                    Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', self.unique)])]), 
                    *([Token("COMMA",",")] if len(nodes) == 4 else []),
                    *nodes[2:-1],
                Token('RPAR', ')')])
        return Tree(Token("RULE","spplang_function_call"), nodes)
 


def removeSppClasses(parseTree):
    return RemoveSppClasses().transform(parseTree)

