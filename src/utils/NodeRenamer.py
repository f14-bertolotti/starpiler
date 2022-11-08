from lark.visitors import Visitor
class NodeRenamer(Visitor):

    def __init__(self, renamer, *args, **kwargs):
        self.renamer = renamer
        super().__init__(*args, **kwargs)

    def visit(self, *args, **kwargs):
        super().visit(*args, **kwargs)

    def __default__(self, tree):
        tree.data = self.renamer(tree.data)
        super().__default__(tree)


