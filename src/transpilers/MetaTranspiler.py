
from src.utils import SPrettyPrinter
import heapq

from src.utils import NotAppliedException
from src.utils import nodeset
from src.utils import relative_set_difference_distance as rsdd

import copy
from collections import defaultdict

class MetaTranspiler:
    def __init__(self, deltas, metric):
        self.metric = metric
        self.deltas = deltas


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
            metric, _ , tree = heapq.heappop(queue)
            #print(i, metric, len(tree.path), tree.path)
            if metric == 0: 
                #print("="*10,"DONE","="*10)
                #print(SPrettyPrinter().transform(tree))
                return tree

            for delta in self.deltas:
                #print("\t",delta.__name__)
                try:
                    path = tree.path.copy()
                    newtree = delta(tree)
                    newtree.path = path + [delta.__name__]

                    if newtree not in visited:
                        i += 1
                        heapq.heappush(queue, tuple((self.metric(newtree), i, newtree)))
                        visited.add(newtree)

                except NotAppliedException: pass

        raise ValueError("Could not transpile")

 
    def search_Astar(self, tree, solutionset):

        openSet = []

        gScore = defaultdict(lambda : float("inf"))
        gScore[tree] = 0

        fScore = defaultdict(lambda : float("inf"))
        treeset = nodeset(tree)
        fScore[tree] = 0 if treeset.issubset(solutionset) else rsdd(solutionset, solutionset, treeset)

        iteration = 0
        tree.path = []
        heapq.heappush(openSet, (fScore[tree], iteration, tree, treeset))

        while openSet:

            print([x[0] for x in openSet])

            score, _, current, currentset = heapq.heappop(openSet)

            if nodeset(current).issubset(solutionset):
                return current
 
            print(score, iteration, current.path)

            for delta in reversed(self.deltas):
                try:
                    neighbor = delta(current)

                    neighborset = nodeset(neighbor)
                    neighbor.path = current.path + [delta.__name__]
                    tentative_gScore = gScore[current] + rsdd(solutionset, currentset, neighborset)

                    if tentative_gScore < gScore[neighbor]:

                        gScore[neighbor] = tentative_gScore
                        fScore[neighbor] = tentative_gScore + (0 if neighborset.issubset(solutionset) else rsdd(solutionset, solutionset, neighborset)) 

                        if neighbor not in openSet:
                            iteration += 1
                            heapq.heappush(openSet, (fScore[neighbor], -iteration, neighbor, neighborset))
    
                except NotAppliedException as e: continue


                
        raise ValueError("could not transpile")

