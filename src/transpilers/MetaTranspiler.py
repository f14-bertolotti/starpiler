
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
                return parseTree
            
            for delta in self.deltas:

                newParseTree = delta(parseTree)
                newParseTree.path = parseTree.path + [delta.__name__]

                if newParseTree not in visited:
                    visited.add(newParseTree)
                    queue.append(newParseTree)

