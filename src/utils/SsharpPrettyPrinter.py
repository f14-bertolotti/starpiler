from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token
from src.utils import Node2String

class SsharpPrettyPrinter(Node2String):


    @v_args(tree=True)
    def ssharplang_class_definition(self, tree):
        tree.string = f"{tree.children[0]} {tree.children[1].string} {tree.children[2]} \n\t" + \
                 "\n\t".join(map(lambda n:n.string, tree.children[3:-1])) + \
                 tree.children[-1] + "\n"   
        return tree

    @v_args(tree=True)
    def ssharplang_block(self, tree):
        tree.string = "\t" + "\n\t".join(map(lambda n:n.string, tree.children))
        return tree

    @v_args(tree=True)
    def ssharplang_method_definition(self, tree):
        tree.string = f"{tree.children[0]} {tree.children[1].string} {tree.children[2].string} {tree.children[3].string} {tree.children[4]}\n\t\t" + \
            "\n\t\t".join(map(lambda n:n.string, tree.children[5].children)) + \
            f"\n\t{tree.children[6]}\n"
        return tree

    @v_args(tree=True)
    def ssharplang_start(self, tree):
        tree.string = "\n".join(child.string for child in tree.children)
        return tree
   
