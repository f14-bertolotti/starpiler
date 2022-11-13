from lark.tree import Tree
from lark import Token

def isS(node):
    if isinstance(node, Tree) and node.data.startswith("slang_") and all(map(isS, node.children)): return True
    elif isinstance(node, Token): return True
    else: return False


