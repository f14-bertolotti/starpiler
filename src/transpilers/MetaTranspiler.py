
from src.transpilers.ToString import toString

class MetaTranspiler:
    def __init__(self, deltas, exitCondition):
        self.exitCondition = exitCondition
        self.deltas        =        deltas

    def search(self, parseTree):
        parseTree.path = []
        queue   = [parseTree]
        visited = {parseTree}

        while queue:
            parseTree = queue.pop(0)
            if self.exitCondition(parseTree): 
                # print(toString(parseTree))
                return parseTree
            
            for delta in self.deltas:
                try:
                    newParseTree = delta(parseTree)
                except: 
                    continue 

                newParseTree.path = parseTree.path + [delta.__name__]

                if newParseTree not in visited:
                    visited.add(newParseTree)
                    queue.append(newParseTree)

        raise ValueError("could not transpile")
 
