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

    def slang_start(self, nodes):
        return Tree(Token("RULE", "slang_start"), [Tree(Token('RULE', 'slang_global_assignement'), [Token('DEF', 'def'), a]) if a.data == "slang_auto_assignement" else a for n in nodes for a in ((n["assignements"] if isinstance(n,dict) else [])+[n["tree"] if isinstance(n,dict) else n])])

    def slang_block(self, nodes):
        return Tree(Token("RULE", "slang_block"), [assignement for node in nodes for assignement in (node["assignements"] if isinstance(node, dict) else []) + [node["tree"] if isinstance(node, dict) else node]])

    def slang_global_assignement(self, nodes):
        return {"tree" : Tree(Token('RULE', 'slang_global_assignement'), [Token('DEF', 'def'), nodes[1]["tree"] if isinstance(nodes[1], dict) else nodes[1]]),
                "assignements" : nodes[1]["assignements"] if isinstance(nodes[1], dict) else []}

    def slang_statement(self, nodes):
        return {"tree": Tree(Token("RULE", "slang_statement"), [nodes[0]["tree"] if isinstance(nodes[0], dict) else nodes[0], Token("SEMICOLON",";")]),
                "assignements" : nodes[0]["assignements"] if isinstance(nodes[0],dict) else []}

    def slang_function_call(self, nodes):
        return {"tree":Tree(Token("RULE", "slang_function_call"), [nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0], Token("LPAR", "("), nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2], Token("RPAR", ")")]) if len(nodes) == 4 else \
                       Tree(Token("RULE", "slang_function_call"), [nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0], Token("LPAR", "("), Token("RPAR", ")")]),
                "assignements":[asgn for node in nodes for asgn in (node["assignements"] if isinstance(node,dict) else [])]}

    def slang_expression_sequence(self, nodes):
        exprs = [node["tree"] if isinstance(node, dict) else node for node in nodes]
        asgns = [assignement for node in nodes for assignement in (node["assignements"] if isinstance(node, dict) else [])]
        return {"tree" : Tree(Token("RULE","slang_expression_sequence"), exprs), 
                "assignements" : asgns}

    def slang_return(self, nodes):
        expr = nodes[1][        "tree"] if isinstance(nodes[1], dict) else nodes[1]
        asgn = nodes[1]["assignements"] if isinstance(nodes[1], dict) else [] 

        return {"tree": Tree(Token("RULE", "slang_return"), [Token("RETURN", "return"), expr, Token("SEMICOLON",";")]),
                "assignements": asgn}

    def slang_ifthen(self, nodes):
        expr = nodes[1][        "tree"] if isinstance(nodes[1], dict) else nodes[1]
        asgn = nodes[1]["assignements"] if isinstance(nodes[1], dict) else []
        return {"tree" : Tree(Token("RULE", "slang_ifthen"), [Token("IF", "if"), expr, Token("DO", "do"), nodes[3], Token("SEMICOLON", ";")]),
                "assignements" : asgn}

    def slang_while(self, nodes):
        expr = nodes[1][        "tree"] if isinstance(nodes[1], dict) else nodes[1]
        asgn = nodes[1]["assignements"] if isinstance(nodes[1], dict) else []
        lastexpr = [Tree(Token("RULE", "slang_assignement"), [
            Tree(Token("RULE", "slang_reference"), [Token("AMPERSAND", "&"), nodes[1]["assignements"][-1].children[1]]), 
            Token("EQUAL", "="), 
            nodes[1]["assignements"][-1].children[3], Token("SEMICOLON", ";")])] if isinstance(nodes[1], dict) else []

        nodes[3].children = nodes[3].children + nodes[1]["assignements"][:-1] + lastexpr

        return {"tree": Tree(Token("RULE", "slang_while"), [Token("WHILE", "while"), expr, Token("DO","do"), nodes[3], Token("SEMICOLON",";")]),
                "assignements": asgn}

    def slang_declaration_assignment(self, nodes):
        expr = nodes[3][        "tree"] if isinstance(nodes[3], dict) else nodes[3]
        asgn = nodes[3]["assignements"] if isinstance(nodes[3], dict) else []
        return {"tree":Tree(Token("RULE", "slang_declaration_assignment"), [nodes[0], nodes[1], Token("EQUAL", "="), expr, Token("SEMICOLON", ";")]),
                "assignements":asgn}

    def slang_auto_assignement(self, nodes):
        return {"tree":Tree(Token('RULE', 'slang_auto_assignement'), [Token('AUTO', 'auto'), nodes[1], Token('EQUAL', '='), nodes[3]["tree"] if isinstance(nodes[3], dict) else nodes[3], Token('SEMICOLON', ';')]),
                "assignements": nodes[3]["assignements"] if isinstance(nodes[3], dict) else []}


    def slang_assignement(self, nodes):
        lexpr = nodes[0][        "tree"] if isinstance(nodes[0], dict) else nodes[0]
        rexpr = nodes[2][        "tree"] if isinstance(nodes[2], dict) else nodes[2]
        lasgn = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rasgn = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        return {"tree": Tree(Token("RULE", "slang_assignement"), [lexpr, Token("EQUAL", "="), rexpr, Token("SEMICOLON", ";")]),
                "assignements": rasgn + lasgn}

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
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_addition"), [leftTree, Token("PLUS", "+"), rightTree]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_multiplication(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_multiplication"), [leftTree, Token("STAR", "*"), rightTree]), 
                                     Token("SEMICOLON", ";")])]}


    def slang_division(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_division"), [leftTree, Token("SLASH", "/"), rightTree]), 
                                     Token("SEMICOLON", ";")])]}


    def slang_subtraction(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_subtraction"), [leftTree, Token("MINUS", "-"), rightTree]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_not_equal(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_not_equal"), [leftTree, Token("__ANON__", "!="), rightTree]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_equality(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_equality"), [leftTree, Token("__ANON__", "=="), rightTree]), 
                                     Token("SEMICOLON", ";")])]}
    
    def slang_less(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_less"), [leftTree, Token("LESSTHAN", "<"), rightTree]), 
                                     Token("SEMICOLON", ";")])]}
 
    def slang_less_equal(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_less_equal"), [leftTree, Token("__ANON__", "<="), rightTree]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_greater(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_greater"), [leftTree, Token("MORETHAN", ">"), rightTree]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_greater_equal(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0],dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2],dict) else nodes[2]
        return {"tree": newIdentifier, 
                "assignements" : leftAssignements + rightAssignements +  
                                 [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_greater_equal"), [leftTree, Token("__ANON__", ">="), rightTree]), 
                                     Token("SEMICOLON", ";")])]}



    def slang_cast(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        assignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        tree = nodes[0]["tree"] if isinstance(nodes[0], dict) else nodes[0]
        return {"tree" : newIdentifier,
                "assignements" : assignements + [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_cast"), [tree, Token("AS", "as"), nodes[2]]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_array(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        assignements  = [asgn for node in nodes[1::2] for asgn in (node["assignements"] if isinstance(node,dict) else [])] 
        trees = [node["tree"] if isinstance(node, dict) else node for node in nodes]
        return {"tree" : newIdentifier, 
                "assignements" : assignements + [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_array"), trees), 
                                     Token("SEMICOLON", ";")])]}

    def slang_struct_value(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        assignements  = [asgn for node in nodes[4::4] for asgn in (node["assignements"] if isinstance(node,dict) else [])] 
        trees = [node["tree"] if isinstance(node, dict) else node for node in nodes]
        return {"tree": newIdentifier,
                "assignements" : assignements + [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_struct_value"), trees), 
                                     Token("SEMICOLON", ";")])]}

    def slang_struct_access(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        leftAssignements  = nodes[0]["assignements"] if isinstance(nodes[0], dict) else []
        rightAssignements = nodes[2]["assignements"] if isinstance(nodes[2], dict) else []
        leftTree  = nodes[0]["tree"] if isinstance(nodes[0], dict) else nodes[0]
        rightTree = nodes[2]["tree"] if isinstance(nodes[2], dict) else nodes[2]
        return {"tree":newIdentifier,
                "assignements": leftAssignements + rightAssignements + [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_struct_access"), [leftTree, Token("DOT","."), rightTree]), 
                                     Token("SEMICOLON", ";")])]}

    def slang_indexed(self, nodes):
        newIdentifier = Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.register.unregistered())])
        assignements = [asgn for node in nodes for asgn in (node["assignements"] if isinstance(node,dict) else [])]
        trees = [node["tree"] if isinstance(node,dict) else node for node in nodes]
        return {"tree":newIdentifier, 
                "assignements": assignements + [Tree(Token("RULE", "slang_auto_assignement"), [
                                     Token("AUTO", "auto"), 
                                     newIdentifier, 
                                     Token("EQUAL", "="), 
                                     Tree(Token("RULE", "slang_indexed"), trees), 
                                     Token("SEMICOLON", ";")])]} 





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

    result = FlattenExpressionTransformer().transform(parseTree)
    return result 

    


