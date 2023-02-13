from lark import Tree, Token

from src.utils import AppliedTransformer

class FunctionCalls(AppliedTransformer):
    def reset(self):
        self.applied = False
        return self

    def ssharplang_function_call(self, nodes):
        self.applied = True
        return Tree(Token("RULE", "spplang_function_call"), nodes)

transformer= FunctionCalls()
def functionCalls(parseTree):
    return transformer.reset().transform(parseTree)
