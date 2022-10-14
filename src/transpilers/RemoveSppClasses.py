
from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token
from colorama import Fore, Back, Style
import rich

class Field:
    def __init__(self, type, name): 
        self.type, self.name = type, name
        self.name.children[0] = f"this.{self.name.children[0].value}"
        self.type = Tree(Token("RULE", "spplang_pointer"), [type, Token("STAR", "*")])
    def __str__ (self): return f"Field({self.type.data},{self.name.children[0]})"
    def getTree (self): return Tree(Token("RULE", "spplang_field_declaration"), [Token("DEF", "def"), self.type, self.name, Token("SEMICOLON", ";")])
class Method:
    def __init__(self, clsname, fields, rtype, name, params, body): 
        self.clsname, self.rtype, self.name, self.params, self.body = clsname, rtype, name, params, body
        self.params.children = [self.params.children[0]] + [Tree(Token("RULE","spplang_parameter_definition"), [field.type, field.name]) for field in fields] + self.params.children[1:]
        self.name.children[0] = f"{self.clsname}.{self.name.children[0]}"
    def __str__ (self): return f"Method({self.rtype.data},{self.name.children[0]},...,...)"
    def getTree(self): return Tree(Token("RULE", "spplang_function_definition"), [Token("DEF", "def"), self.rtype, self.name, self.params, Token("DOES","does"), self.body, Token("SEMICOLON", ";")]) 
class Class:
    def __init__(self, name, fields, methods): self.name, self.fields, self.methods = name, fields, methods
    def __str__ (self): 
        fieldsstr = ",".join(map(str, self.fields))
        methodsstr = ",".join(map(str, self.methods))
        return f"Class({self.name},{fieldsstr},{methodsstr})"

class RemoveSppClasses(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name2class = dict()

    def __default__(self, *args, **kwargs):
        print(f"{Fore.GREEN} {args[0]} {Style.RESET_ALL}")
        return super().__default__(*args, **kwargs)

    def spplang_start(self, nodes):
        res = Tree(Token("RULE","spplang_start"), [method.getTree() for node in nodes if isinstance(node,Class) for method in node.methods])
        return res

    def spplang_new(self, nodes):
        clsname = nodes[1].children[0]
        return Tree(Token("RULE","spplang_new"),nodes) 


    def spplang_class(self, nodes):

        clsname = nodes[1].children[0]
        fields  = [Field(node.children[1], node.children[2]) for node in nodes[3:-1] if node.data == "spplang_field_declaration"]
        methods = [Method(clsname, fields, node.children[1], node.children[2], node.children[3], node.children[5]) for node in nodes[3:-1] if node.data == "spplang_function_definition"]
        self.name2class[clsname] = Class(clsname, fields, methods)
    
        return self.name2class[clsname]





if __name__ == "__main__":
    from src.syntax.
    from src.syntax.spplang import lang
    res = RemoveSppClasses().transform(lang.parse("""
    class X with
        def int64 x;
        def int64 y;
        def int8* s;
        def int64 increment(int64 x) does
            return x + 1;
        ;
        def void start(int64 x, int64 y , int8* z) does
            this.x = x; this.y = y; this.z = z;
        ;
    ;


    def int64 start() does
        X x = new X();
        return 0;
    ;
    """))

    #rich.print(res)
