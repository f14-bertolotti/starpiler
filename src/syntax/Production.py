from src.syntax import Larkable

class Production(Larkable):
    
    def __init__(self, name, rules=[], mod=""):
        self.rules = rules
        self.name = name
        self.mod = mod

    def __iter__(self):
        return iter(self.rules)

    def __hash__(self):
        return hash(tuple(hash(rule) for rule in self.rules))

    def setName(self, name):
        self.name = name
        return self

    def append(self, *args):
        self.rules = self.rules + list(args)
        return self

    def toLark(self):
        right = "\n | ".join([rule.name if isinstance(rule,Production) else rule.toLark() for rule in self])
        return f"{self.mod}{self.name} : {right}"

    def __str__(self):
        return f"Production({self.name})"
