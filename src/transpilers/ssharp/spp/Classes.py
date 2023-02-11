from lark import Tree, Token
from src.utils import AppliedTransformer

class Classes(AppliedTransformer):

    def reset(self):
        self.applied = False
        return self

    def ssharplang_class_definition(self, nodes):
        
        if nodes[1].children[0].value == "FFI":
            return Tree(Token("RULE","ssharplang_class_definition"), nodes)

        self.applied = True
        return Tree(Token('RULE', 'spplang_class'), [
                Token('CLASS', 'class'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[1].children[0].value)]), 
                Token('WITH', 'with'), 
                *nodes[3:-1],
                Token('SEMICOLON', ';')])

classesTransformer = Classes()
def classes(parseTree):
    return classesTransformer.reset().transform(parseTree)



