import lark
from lark import Tree, Token
from src.utils import AppliedTransformer
from src.utils import NotAppliedException

def reference(nodes):

    if not nodes[0].data.value.startswith("ssharplang_"): raise ValueError("subtree translated")

    if nodes[0].data == "ssharplang_identifier":
        
        nodes[0] = Tree(Token('RULE', 'spplang_reference'), [
            Token('AMPERSAND', '&'), 
            nodes[0]])
    
    elif nodes[0].data == "ssharplang_class_access":
    
        nodes[0] = Tree(Token('RULE', 'spplang_struct_ref_access'), [
            nodes[0].children[0], 
            Token('__ANON__', '&.'), 
            nodes[0].children[2]])
    
    elif nodes[0].data == "ssharplang_indexed":

        nodes[0] = Tree(Token('RULE', 'spplang_indexed'), [
            nodes[0].children[0], 
            Tree(Token('RULE', 'spplang_reference_square_parenthesized'), [
                Token('__ANON__', '&['), 
                nodes[0].children[1].children[1], 
                Token('RSQB', ']')])])
    
    return nodes


class Assignements(AppliedTransformer):

    def transform(self, *args, **kwargs):
        try: 
            res = super().transform(*args, **kwargs)
            if not self.applied: raise ValueError()
            return res
        except lark.exceptions.VisitError: raise NotAppliedException
        except ValueError: raise NotAppliedException

    def ssharplang_assignement(self, nodes):
        self.applied = True
        return Tree(Token("RULE", "spplang_stmt_expr"), [
            Tree(Token("RULE", "spplang_assignement"), reference(nodes[:-1])),
            nodes[-1]
        ])

    def ssharplang_auto_assignement(self, nodes):
        self.applied = True
        return Tree(Token("RULE", "spplang_stmt_expr"), [
            Tree(Token("RULE", "spplang_auto_assignement"), nodes),
            nodes[-1]
        ])

    def ssharplang_declaration_assignment(self, nodes):
        self.applied = True
        return Tree(Token("RULE", "spplang_stmt_expr"), [
            Tree(Token("RULE", "spplang_auto_assignement"), [Token("__ANON__","auto"), *nodes[1:-1]]),
            nodes[-1]
        ])


def assignements(parseTree) -> Tree:
    return Assignements().transform(parseTree)
