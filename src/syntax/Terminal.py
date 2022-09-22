from src.syntax import Larkable

class Terminal(Larkable):

    def __init__(self, value, regex=False, mod=""):
        self.value = value
        self.regex = regex
        self.mod = mod

    def __iter__(self):
        return iter([self.value])

    def toLark(self):
        return f"/{self.value}/" if self.regex else f"\"{self.value}\"{self.mod}"

    def __str__(self):
        return f"Terminal(\"{self.value}\", mod=\"{self.mod}\")"
