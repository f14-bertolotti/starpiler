from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token
from src.utils import Node2String

class SPrettyPrinter(Node2String):

    @v_args(tree=True)
    def slang_struct(self, tree):
        tree.string = f"{tree.children[0]} {tree.children[1].string} {tree.children[2]} \n\t" + \
                 "\n\t".join(map(lambda n:n.string, tree.children[3:-1])) + \
                 tree.children[-1] + "\n"   
        return tree

    @v_args(tree=True)
    def slang_block(self, tree):
        tree.string = "\t" + "\n\t".join(map(lambda n:n.string, tree.children))
        return tree

    @v_args(tree=True)
    def slang_function_definition(self, tree):
        tree.string = f"{tree.children[0]} {tree.children[1].string} {tree.children[2].string} {tree.children[3].string} {tree.children[4]}\n{tree.children[5].string}{tree.children[6]}\n"
        return tree

    @v_args(tree=True)
    def slang_function_declaration(self, tree):
        tree = super().__default__(tree.data, tree.children, tree.meta)
        tree.string += "\n"
        return tree

    @v_args(tree=True)
    def slang_start(self, tree):
        tree.string = "\n".join(child.string for child in tree.children)
        return tree
   

