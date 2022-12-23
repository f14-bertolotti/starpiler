from lark.visitors import Transformer, v_args
from src.syntax.spplang import methodDefinition as mdlang
from src.syntax.spplang import functionDeclaration as fclang
from src.syntax.spplang import variableDefinition as galang
from src.syntax import Language
from lark import Lark, Token
from lark.tree import Tree
import copy

endMethod = Lark(Language(mdlang).toLark(), keep_all_tokens=True).parse(f"def void end(_* this) does return;;")

class AddEndMethods(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("could not find any spplang_class")
        return res

    @v_args(meta=True)
    def spplang_class(self, meta, nodes):
        self.applied = True
        className  = nodes[1].children[0].value
        endNames = sum([isinstance(node, Tree) and node.children[2].children[0].value == "end" for node in nodes[3:-1]])
        if endNames == 0:
            end = copy.deepcopy(endMethod)
            end.children[3].children[1].children[0].children[0].children[0].children[0] = Token("__ANON__", className)
            return Tree(Token("RULE", "spplang_class"), nodes[:-1] + [end,nodes[-1]], meta)
        elif endNames == 1:
            return Tree(Token("RULE", "spplang_class"), nodes, meta)
        else:
            raise ValueError("multiple \"end\" names defined")


def addEndMethods(parseTree):
    return AddEndMethods().transform(parseTree)
