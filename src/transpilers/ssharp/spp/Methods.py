from lark import Tree, Token

from src.utils import AppliedTransformer
from src.transpilers.ssharp.spp.Utils import * 

class Methods(AppliedTransformer):
    
    debug = 0

    def reset(self):
        self.applied = False
        return self

    def ssharplang_start(self, nodes):
        if importgc not in nodes: nodes.insert(0, importgc)
        return Tree(Token("RULE","ssharplang_start"), nodes)

    def ssharplang_method_definition(self, nodes):

        if is_main_method(nodes):
            return Tree(Token("RULE", "ssharplang_method_definition"), nodes)

        self.applied = True

        plist = [x for c in zip(
            filter(lambda x:isinstance(x,Tree), nodes[1].children[0].children[1:]), 
            filter(lambda x:isinstance(x,Tree), nodes[3].children[1:-1])) for x in [Tree(Token("RULE", "spplang_parameter_definition"), list(c)), Token("COMMA",",")]]
        if len(plist) > 1: del plist[-1]

        for p in plist:
            if isinstance(p,Tree) and p.children[0].data == "ssharplang_tname":
                p.children[0] = Tree(Token("RULE", "spplang_pointer"), [p.children[0], Token("STAR","*")])

        rtype = Tree(Token("RULE", "spplang_pointer"), [nodes[1].children[1].children[1], Token("STAR","*")]) if nodes[1].children[1].children[1].data == "ssharplang_tname" else nodes[1].children[1].children[1]

        return \
            Tree(Token('RULE', 'spplang_method_definition'), [
            Token('DEF', 'def'), 
            rtype, 
            nodes[2] if nodes[2].children[0].value != "__init__" else Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "start")]), 
            Tree(Token('RULE', 'spplang_parameter_seq_def'), [
                Token('LPAR', '('), 
                *plist,
                Token('RPAR', ')')]), 
            Token('DOES', 'does'), 
            nodes[5],
            Token('SEMICOLON',';')
            ])

    
methodsTransformer = Methods()
def methods(parseTree)->Tree:
    return methodsTransformer.reset().transform(parseTree)
