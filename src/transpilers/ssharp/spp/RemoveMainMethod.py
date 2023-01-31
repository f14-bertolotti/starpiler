
from lark import Token, Tree
from src.utils import AppliedTransformer

class RemoveMainMethod(AppliedTransformer):

    def reset(self):
        self.applied = False
        return self

    def ssharplang_class_definition(self, nodes):
        return Tree(Token("RULE", "ssharplang_class_definition"), [node for node in nodes if node != None])

    def ssharplang_method_definition(self, nodes):
        if nodes[2].children[0].value == "__main__": 
            self.applied = True
            return None
        else: return Tree(Token("RULE", "ssharplang_method_definition"), nodes)


removeMainMethod = RemoveMainMethod()
def remove_mainmethod(parseTree):
    return removeMainMethod.reset().transform(parseTree)
