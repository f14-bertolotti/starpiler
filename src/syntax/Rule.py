from src.syntax import Larkable
from src.syntax import Visitable
from src.syntax import Production

class Rule(Larkable, Visitable):
    def __init__(self, *args, mod=""):
        Larkable .__init__(self)
        Visitable.__init__(self)

        self.rule = list(args)
        self.mod = mod

    def __iter__(self):
        return iter(self.rule)

    def __getitem__(self, index):
        return self.rule[index]

    def __setitem__(self, index, value):
        self.rule[index] = value

    def append(self, value):
        self.rule.append(value)

    def insert(self, i, value):
        self.rule.insert(i, value)

    def toLark(self):
        return "(" + " ".join([x.name if isinstance(x, Production) else x.toLark() for x in self]) + f"){self.mod}"

    def getVisitable(self):
        return self.rule
        
