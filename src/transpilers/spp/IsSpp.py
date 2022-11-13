from lark.tree import Tree
from lark import Token

def isSpp(node):
    if isinstance(node, Tree) and node.data.startswith("spplang_") and all(map(isSpp, node.children)): return True
    elif isinstance(node, Token): return True
    else: return False


