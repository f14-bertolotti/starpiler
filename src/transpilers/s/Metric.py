from lark.tree import Tree
from lark import Token

def metric(node):
    if isinstance(node, Tree) and not node.data.startswith("slang_"):
        return sum(map(metric, node.children)) + 1
    elif isinstance(node, Tree): 
        return sum(map(metric, node.children)) + 0 
    else:
        return 0
    

def metric01(node):
    if isinstance(node, Tree) and not node.data.startswith("slang_"):
        return min(sum(map(metric, node.children)) + 1, 1)
    elif isinstance(node, Tree): 
        return min(sum(map(metric, node.children)) + 0, 1)
    else:
        return 0
 
