from lark.visitors import Transformer
from lark.tree import Tree
from lark import Lark

class SmallMeta:
    def __init__(self, start_line=None, end_line=None, start_column=None, end_column=None, type=None): 
        self.start_line   = start_line
        self.end_line     = end_line
        self.start_column = start_column
        self.end_column   = end_column
        self.type         = type
    def __str__(self):
        return f"({self.start_line},{self.start_column}-{self.end_line},{self.end_column}-{self.type})"
    def clone(self):
        return SmallMeta(start_line=self.start_line, end_line=self.end_line, start_column=self.start_column, end_column=self.end_column, type=self.end_type)

class ReplaceMeta(Transformer):
    def __default__(self, data, children, meta):
        return Tree(data, children, SmallMeta(start_line=meta.line, end_line=meta.end_line, start_column=meta.column, end_column=meta.end_column, type=None))

class SMLark(Lark):
    def parse(self, *args, **kwargs):
        return ReplaceMeta().transform(super().parse(*args, **kwargs))
