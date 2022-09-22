from src.syntax import Larkable
from src.syntax import Production

class Rule(Larkable):
    def __init__(self, *args, mod=""):
        self.rule = list(args)
        self.mod = mod

    def __hash__(self):
        return hash(self.rule)

    def __iter__(self):
        return iter(self.rule)

    def append(self, *args):
        self.rule = self.rule + list(args)
        return self

    def toLark(self):
        return "(" + " ".join([x.name if isinstance(x, Production) else x.toLark() for x in self]) + f"){self.mod}"

    def __str__(self):
        return f"rule{self.rule}"
