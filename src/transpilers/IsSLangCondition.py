from lark.tree import Tree
from lark import Token

def isSLang(node):
    if isinstance(node, Tree) and node.data.startswith("slang_") and all(map(isSLang, node.children)): return True
    elif isinstance(node, Token): return True
    else: return False


