from lark.visitors import Visitor

class NodeSetVisitor(Visitor):

    def __init__(self, *args, **kwargs):
        self.visited = set()
        super().__init__(*args, **kwargs)

    def reset(self):
        self.visited.clear()
        return self

    def __default__(self, tree):
        self.visited.add(tree.data.value)

    def visit(self, tree):
        super().visit(tree)
        return self.visited.copy()


visitor = NodeSetVisitor()
def nodeset(tree):
    return visitor.reset().visit(tree)

def lang2rules(lang):
    return {rule[0].value for rule in lang.grammar.rule_defs}
