from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.utils import AppliedTransformer
from src.utils import NotAppliedException

from src.semantics.types import Object, Pointer
from src.transpilers.ssharp.spp.ClassAccesses import classAccesses

class Assignements(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_assignement(self, meta, nodes):
        self.applied=True

        if nodes[0].data == "ssharplang_identifier":
            
            nodes[0] = Tree(Token('RULE', 'spplang_reference'), [
                Token('AMPERSAND', '&'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[0].children[0].value)])], meta)

        elif nodes[0].data == "ssharplang_class_access":

            nodes[0] = Tree(Token('RULE', 'spplang_struct_ref_access'), [
                nodes[0].children[0], 
                Token('__ANON__', '&.'), 
                nodes[0].children[2]], meta)

        return Tree(Token("RULE", "spplang_assignement"), nodes, meta)
#
    @v_args(meta=True)
    def ssharplang_declaration_assignment(self, meta, nodes):
        self.applied=True
        nodes[0] = Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_tname'), [nodes[0].children[0]]), Token('STAR', '*')])
        return Tree(Token("RULE", "spplang_declaration_assignment"), nodes, meta)


    @v_args(meta=True)
    def ssharplang_auto_assignment(self, meta, nodes):
        self.applied=True
        return Tree(Token("RULE", "spplang_auto_assignment"), nodes, meta)



def assignements(parseTree) -> Tree:
    try: parseTree = Assignements().transform(parseTree)
    except NotAppliedException: pass
    try: parseTree = classAccesses(parseTree)
    except NotAppliedException: pass
    return parseTree
