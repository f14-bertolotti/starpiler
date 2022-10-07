from abc import abstractmethod 

class Visitable:

    def visit(self, function, visited = set()):
        function(self)
        visited.add(self)
        for visitable in filter(lambda x: x not in visited, self.getVisitable()):
            visitable.visit(function, visited)


    @abstractmethod
    def getVisitable(self): pass

