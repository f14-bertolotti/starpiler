from lark.tree import Tree

def metric01(node):
    if isinstance(node, Tree) and not node.data.startswith("ssharplang_"):
        return min(sum(map(metric01, node.children)) + 1, 1)
    elif isinstance(node, Tree): 
        return min(sum(map(metric01, node.children)) + 0, 1)
    else:
        return 0
 
