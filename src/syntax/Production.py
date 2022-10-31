from src.syntax import Larkable
from src.syntax import Visitable

class Production(Larkable, Visitable):
    
    def __init__(self, name, rules=[], mod="", priority=0):
        Larkable .__init__(self)
        Visitable.__init__(self)

        self.priority = priority
        self.rules = rules
        self.name = name
        self.mod = mod

    def __iter__(self):
        return iter(self.rules)

    def __getitem__(self, index):
        return self.rules[index]

    def __setitem__(self, index, value):
        self.rules[index] = value

    def setName(self, name):
        self.name = name
        return self

    def setPriority(self, priority):
        self.priority = priority
        return self

    def append(self, *args):
        self.rules = self.rules + list(args)
        return self

    def insert(self, i, value):
        self.rules.insert(i, value)

    def toLark(self):
        right = "\n | ".join([rule.name if isinstance(rule,Production) else rule.toLark() for rule in self])
        return f"{self.mod}{self.name}.{self.priority} : {right}"
    
    def getVisitable(self): 
        return self.rules
