
from src.utils import SPrettyPrinter
import heapq

from src.utils import NotAppliedException



class MetaTranspiler:
    def __init__(self, deltas, metric):
        self.metric = metric
        self.deltas = deltas

    def apply(self, tree, delta, queue, visited, i):
        
        try:
            path = tree.path.copy()
            newtree = delta(tree)
            newtree.path = path + [delta.__name__]

            if newtree not in visited:
                heapq.heappush(queue, tuple((self.metric(newtree), i, newtree)))
                visited.add(newtree)

        except NotAppliedException: pass


    def apply_list(self, tree, deltas, queue, visited, i):
        path = tree.path.copy()
        applied = False

        for delta in deltas:

            try:
                tree = delta(tree)
                path.append(delta.__name__)
                applied = True
            except NotAppliedException: pass

        if tree not in visited and applied:
            tree.path = path
            heapq.heappush(queue, tuple((self.metric(tree), i ,tree)))
            visited.add(tree)
            

    def search(self, tree):

        tree.path = []
        queue = list()
        i = 0
        heapq.heappush(queue, (self.metric(tree), i, tree))
        visited = {tree}
        #print()

        while queue:
            #if i > 1000: exit(0)
            #input()
            metric,_ , tree = heapq.heappop(queue)
            #print(metric, tree.path)
            if metric == 0: 
                #print("="*10,"DONE","="*10)
                #print(SPrettyPrinter().transform(tree))
                return tree

            for delta in self.deltas:
                
                if isinstance(delta, list):
                    #print("\t", ":".join([d.__name__ for d in delta]))
                    self.apply_list(tree, delta, queue, visited, i)
                    i += len(delta)

                else:

                    #print("\t",delta.__name__)
                    self.apply(tree, delta, queue, visited, i)
                    i += 1



        raise ValueError("Could not transpile")
