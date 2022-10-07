from src.syntax import Larkable
from src.syntax import Visitable

from src.syntax import Production

class Language(Larkable, Visitable):

    def __init__(self, production):
        Larkable .__init__(self)
        Visitable.__init__(self)

        self.production = production.setName("start")

    def bfs(self,node):
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
        visited = self.bfs(self.production)
        return "\n\n".join([elem.toLark() for elem in visited if isinstance(elem, Production)] + 
                           ["%ignore /[ \\t\\n\\f\\r]+/"] + 
                           ["%ignore /#[^\\n]*/"])

    def getVisitable(self):
        return [self.production]

    
