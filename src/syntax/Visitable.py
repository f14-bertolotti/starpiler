from abc import abstractmethod 

class Visitable:

    def visit(self, visitor):
        function, visited = visitor
        visited.add(self)
        for unvisited in filter(lambda v: v not in visited, self.getVisitable()):
            unvisited.visit(visitor)
        return function(self)

    @abstractmethod
    def getVisitable(self): pass

