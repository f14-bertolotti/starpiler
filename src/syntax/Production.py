from textwrap import wrap

class Production:
    
    def __init__(self, name, rules=[]):
        self.rules = rules
        self.name = name

    def __iter__(self):
        return iter(self.rules)

    def __hash__(self):
        return hash(tuple(hash(rule) for rule in self.rules))

    def setName(self, name):
        self.name = name
        return self

    def append(self, rule):
        self.rules = (*self.rules, rule)
        return self

    def toLark(self):
        right = "\n | ".join([rule.name if isinstance(rule,Production) else rule.toLark() for rule in self])
        return f"{self.name} : {right}"

    def __str__(self):
        return f"Production({self.name})"
