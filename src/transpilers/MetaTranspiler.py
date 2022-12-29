
from src.utils import SPrettyPrinter
import heapq

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
            #print(metric, parseTree.path)
            if metric == 0: 
                #print("="*10,"DONE","="*10)
                #print(SPrettyPrinter().transform(parseTree))
                return parseTree

            for delta in self.deltas:
                try:
                    i += 1
                    new = delta(parseTree)
                    #print("\t", self.metric(new), delta.__name__)
                    new.path = parseTree.path + [delta.__name__]
                    if new not in visited:
                        heapq.heappush(queue, tuple((self.metric(new), i, new)))
                        visited.add(new)
                except: 
                    #import traceback
                    #print(">>> ", traceback.print_exc())
                    #print(">>> ", parseTree.path)
                    #print(">>> ", delta.__name__)

                    continue

        raise ValueError("Could not transpile")
