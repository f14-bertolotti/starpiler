from textwrap import wrap
from src.syntax import Production

class Rule:
    def __init__(self, *args):
        self.rule = args

    def __hash__(self):
        return hash(self.rule)

    def __iter__(self):
        return iter(self.rule)

    def append(self, arg):
        self.rule = (*self.rule, arg)
        return self

    def toLark(self):
        return " ".join([x.name if isinstance(x, Production) else x for x in self])

    def __str__(self):
        return f"rule{self.rule}"
