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
    def slang_declaration_assignment(self, nodes):
        return Tree(Token("Rule","slang_declaration_assignment"
    def transform(self, *args, **kwargs):
        super().transform(*args, **kwargs)
        return self


class FlattenExpressionTransformer(Transformer): 

    def __default__(self, tree, children, meta):
        assert tree.value.startswith("slang_") or tree.value == "start"
        return {"tree":super().__default__(tree, children, meta)}

    def transform(self, *args, **kwargs):
        self.register = Register().transform(*args, **kwargs)
        return super().transform(*args, **kwargs)

    def slang_block(self, nodes):
        return Tree(Token("RULE", "slang_block"), [stmt for node in nodes for stmt in node["asgn"] + [node["tree"]]])

    def slang_return(self, nodes):
        return {"tree": Tree(Token('RULE', 'slang_return'), 
                             [Token('RETURN', 'return'), 
                              nodes[1][-1].children[1], 
                              Token('SEMICOLON', ';')]),
                "asgn": nodes[1]}
                             

    def slang_round_parenthesized(self, nodes):
        return nodes[1]

    def slang_addition(self, nodes):
        if nodes[0].isAtomic and nodes[1].isAtomic:
            return Tree(Token('RULE', 'slang_declaration_assignment'), 
                                    [nodes[0][0].children[0], 
                                     Tree(Token('RULE', 'slang_identifier'), [Token('__ANON_{self.counter}', self.register.unregistered())]),
                                     Token('EQUAL', '='), 
                                     Tree(Token('RULE', 'slang_addition'), [nodes[0][-1].children[1], Token('PLUS', '+'), nodes[2][-1].children[1]]), 
                                     Token('SEMICOLON', ';')])
        return nodes[0] + nodes[2] + []


    def slang_identifier(self, nodes):
        result = Tree(Token("RULE", "slang_integer"), nodes)
        result.isAtomic = True
        return result


    def slang_integer(self, nodes):
        result = Tree(Token("RULE", "slang_integer"), nodes)
        result.isAtomic = True
        return result

class ToSringTransformer(Transformer):
        
    def __default__(self, data, children, meta):
        result = super().__default__(data, children, meta)
        result.string = " ".join([child.value if isinstance(child, Token) else child.string for child in children]) 
        return result
        
    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs).string

def flattenExpression(parseTree):

    transformer = FlattenExpressionTransformer()
    transformed = transformer.transform(parseTree)
    rich.print(transformed)
    print(ToSringTransformer().transform(transformed))

    

flattenExpression(lang.parse("def int64 start() does return (2 + 2) + 1;;"))
#flattenExpression(lang.parse("""def int64 start() does 
#                                    int64 x = 10; 
#                                    int64 y = 11; 
#                                    return x+y*y;
#                                ;"""))


