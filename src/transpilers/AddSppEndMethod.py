from lark.visitors import Transformer, v_args
from src.syntax.spplang import methodDefinition as mdlang
from src.syntax.spplang import functionDeclaration as fclang
from src.syntax import Language
from lark import Lark, Token
from lark.tree import Tree

class AddSppEndMethod(Transformer):
    @v_args(meta=True)
    def spplang_start(self, meta, nodes):
        freeNames = sum([(isinstance(node,Tree) and node.data == "spplang_class"                and node.children[1].children[0].value == "free") or \
                         (isinstance(node,Tree) and node.data == "spplang_import"               and node.children[3].children[0].value == "free") or \
                         (isinstance(node,Tree) and node.data == "spplang_function_definition"  and node.children[2].children[0].value == "free") or \
                         (isinstance(node,Tree) and node.data == "spplang_function_declaration" and node.children[2].children[0].value == "free") for node in nodes])
        if freeNames == 0:
            freeDeclaration = Lark(Language(fclang).toLark(), keep_all_tokens=True).parse("def void free(int8*);")
            return Tree(Token("RULE", "spplang_start"), [freeDeclaration] + nodes, meta)
        elif freeNames == 1:
            return Tree(Token("RULE", "spplang_start"), nodes, meta)
        else:
            raise ValueError("multiple \"end\" methods defined")
    
    @v_args(meta=True)
    def spplang_class(self, meta, nodes):
        className  = nodes[1].children[0].value
        endNames = sum([isinstance(node, Tree) and node.children[2].children[0].value == "end" for node in nodes[3:-1]])
        if endNames == 0:
            endMethod = Lark(Language(mdlang).toLark(), keep_all_tokens=True).parse(f"""
                        def void end({className}* this) does 
                            &free(this);
                            return;
                        ;
                        """)
            return Tree(Token("RULE", "spplang_class"), nodes[:-1] + [endMethod,nodes[-1]], meta)
        elif endNames == 1:
            return Tree(Token("RULE", "spplang_class"), nodes, meta)
        else:
            raise ValueError("multiple \"end\" names defined")


def addSppEndMethod(parseTree):
    return AddSppEndMethod().transform(parseTree)
