from src.syntax import Production
from src.syntax import Larkable

class Language(Larkable):

    def __init__(self, production):
        self.production = production.setName("start")

    def visit(self,node):
        visited = [node]
        queue = [node]
        
        while queue:
            elem = queue.pop(0)
            for child in elem:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)
        return visited

    def toLark(self):
        visited = self.visit(self.production)
        return "\n\n".join([elem.toLark() for elem in visited if isinstance(elem, Production)] + ["%ignore /[ \\t\\n\\f\\r]+/"])

    
