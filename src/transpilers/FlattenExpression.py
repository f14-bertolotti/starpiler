from src.syntax.slang import lang
from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token

import rich

class Register(Transformer):
    def __init__(self):
        self.counter = 0
        self.registered = set()
        self.name2type = dict()
    def register(self, value): self.registered.add(value)
    def __contains__(self, value): return value in self.registered 
    def unregistered(self):
        while f"var{self.counter}" in self.registered: self.counter += 1
        self.register(f"var{self.counter}")
        return f"var{self.counter}" 
    def slang_identifier(self, nodes):
        self.registered.add(nodes[0].value)
        return Tree(Token("RULE","slang_identifier"), nodes)
    def transform(self, *args, **kwargs):
        super().transform(*args, **kwargs)
        return self


class FlattenExpressionTransformer(Transformer): 

    def __default__(self, tree, children, meta):
        assert tree.value.startswith("slang_") or tree.value == "start"
        return super().__default__(tree, children, meta)

    def transform(self, *args, **kwargs):
        self.register = Register().transform(*args, **kwargs)
        return super().transform(*args, **kwargs)

    def slang_block(self, nodes):
        return Tree(Token("RULE", "slang_block"), [assignement for node in nodes for assignement in (node["assignements"] if isinstance(node, dict) else []) + [node["tree"] if isinstance(node, dict) else node]])

    def slang_return(self, nodes):
        return {"tree": Tree(Token('RULE', 'slang_return'), [Token('RETURN', 'return'), nodes[1]["tree"], Token('SEMICOLON', ';')]),
                "assignements": nodes[1]["assignements"]}

    def slang_round_parenthesized(self, nodes):
        return nodes[1]

    def slang_addition(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token('RULE', 'slang_auto_assignement'), [
                                     Token('AUTO', 'auto'), 
                                     newIdentifier, 
                                     Token('EQUAL', '='), 
                                     Tree(Token('RULE', 'slang_addition'), [leftTree, Token('PLUS', '+'), rightTree]), 
                                     Token('SEMICOLON', ';')])]}
    def slang_multiplication(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token('RULE', 'slang_auto_assignement'), [
                                     Token('AUTO', 'auto'), 
                                     newIdentifier, 
                                     Token('EQUAL', '='), 
                                     Tree(Token('RULE', 'slang_multiplication'), [leftTree, Token('STAR', '*'), rightTree]), 
                                     Token('SEMICOLON', ';')])]}





#class ToSringTransformer(Transformer):
#        
#    def __default__(self, data, children, meta):
#        result = super().__default__(data, children, meta)
#        result.string = " ".join([child.value if isinstance(child, Token) else child.string for child in children]) 
#        return result
#        
#    def transform(self, *args, **kwargs):
#        return super().transform(*args, **kwargs).string
#
def flattenExpression(parseTree):
    return FlattenExpressionTransformer().transform(parseTree)

    

#flattenExpression(lang.parse("def int64 start() does return 2 * 2 + 1;;"))
#flattenExpression(lang.parse("""def int64 start() does 
#                                    int64 x = 10; 
#                                    int64 y = 11; 
#                                    return x+y*y;
#                                ;"""))


