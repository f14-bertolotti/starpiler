
from src.utils import SPrettyPrinter
import heapq

from src.utils import NotAppliedException
from src.utils import nodeset
from src.utils import relative_set_difference_distance as rsdd

import copy
from collections import defaultdict

class MetaTranspiler:
    def __init__(self, deltas, metric, return_visited=False):
        self.metric = metric
        self.deltas = deltas
        self.return_visited = return_visited


    def search(self, tree):

        tree.path = []
        queue = list()
        i = 0
        heapq.heappush(queue, (self.metric(tree), i, tree))
        visited = {tree}

        while queue:

            metric, _ , tree = heapq.heappop(queue)

            if metric == 0: 
                if self.return_visited: return tree, visited
                else: return tree

            for delta in self.deltas:
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

            _, _, current, currentset = heapq.heappop(openSet)

            if nodeset(current).issubset(solutionset): 
                if self.return_visited: return current, set(fScore.keys())
                else: return current



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

