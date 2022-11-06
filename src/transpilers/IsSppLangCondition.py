from lark.tree import Tree
from lark import Token

def isSppLang(node):
    if isinstance(node, Tree) and node.data.startswith("spplang_") and all(map(isSppLang, node.children)): return True
    elif isinstance(node, Token): return True
    else: return False


