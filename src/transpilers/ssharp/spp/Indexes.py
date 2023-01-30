from lark import Tree, Token
from src.utils import AppliedTransformer

class Indexes(AppliedTransformer):
    
    def reset(self):
        self.applied = False
        return self

    def ssharplang_indexed(self, nodes):
        self.applied = True
        # TODO THIS MAY NOT WORK FOR ARRAY OF NATIVES TYPES
        return \
        Tree(Token('RULE', 'spplang_indexed'), [
            nodes[0], 
            Tree(Token('RULE', 'spplang_reference_square_parenthesized'), [
                Token('__ANON__', '&['), 
                nodes[1].children[1], 
                Token('RSQB', ']')])])

indexesTransformer = Indexes()
def indexes(parseTree):
    return indexesTransformer.reset().transform(parseTree)
