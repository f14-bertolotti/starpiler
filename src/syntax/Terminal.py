from src.syntax import Larkable
from src.syntax import Visitable
 

class Terminal(Larkable, Visitable):

    def __init__(self, value, regex=False, mod=""):
        Larkable .__init__(self)
        Visitable.__init__(self)

        self.value = value
        self.regex = regex
        self.mod = mod

    def __iter__(self):
        return iter([self.value])

    def toLark(self):
        return f"/{self.value}/" if self.regex else f"\"{self.value}\"{self.mod}"

    def getVisitable(self): return []
