
from src.utils import SPrettyPrinter
import heapq

from src.utils import NotAppliedException

class MetaTranspiler:
    def __init__(self, deltas, metric):
        self.metric = metric
        self.deltas = deltas

    def search(self, parseTree):

        parseTree.path = []
        queue = list()
        i = 0
        heapq.heappush(queue, (self.metric(parseTree), i, parseTree))
        visited = {parseTree}
        #print()

        while queue:
            #if i > 1000: exit(0)
            #input()
            metric,_ , parseTree = heapq.heappop(queue)
            print(metric, parseTree.path)
            if metric == 0: 
                #print("="*10,"DONE","="*10)
                #print(SPrettyPrinter().transform(parseTree))
                return parseTree

            for delta in self.deltas:
                try:
                    i += 1
            
                    newParseTree = None
                    if isinstance(delta, list):
                        path = parseTree.path
                        for subdelta in delta:
                            parseTree = subdelta(parseTree)
                        newParseTree = parseTree
                        newParseTree.path = path + [subdelta.__name__ for subdelta in delta]

                    else:
                        newParseTree = delta(parseTree) 
                        newParseTree.path = parseTree.path + [delta.__name__]

                    if newParseTree not in visited:
                        heapq.heappush(queue, tuple((self.metric(newParseTree), i, newParseTree)))
                        visited.add(newParseTree)
                except NotAppliedException: 
                    #import traceback
                    #print(">>> ", traceback.print_exc())
                    #print(">>> ", parseTree.path)

                    continue

        raise ValueError("Could not transpile")
