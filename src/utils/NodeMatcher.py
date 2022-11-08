from lark.visitors import Visitor
class NodeMatcher(Visitor):

    def __init__(self, condition, *args, **kwargs):
        self.condition = condition
        self.matches   = list()
        super().__init__(*args, **kwargs)

    def visit(self, *args, **kwargs):
        super().visit(*args, **kwargs)
        return self.matches

    def __default__(self, tree):
        if self.condition(tree): self.matches.append(tree)
        super().__default__(tree)


