import networkx, pickle, heapq

from src.syntax import slang, spplang, ssharplang
from src.transpilers import ssharp2spp_transpile, ssharp2spp_deltas
from src.transpilers import spp2s_transpile, spp2s_deltas
from src.semantics.slang import run
from src.utils import NotAppliedException
from src.utils import merge_delta

from src.utils import relative_set_difference_distance as rsdd
from src.utils import lang2rules
from src.utils import nodeset


def dump(obj):
    with open('data/trees.pickle', 'wb') as file:
        pickle.dump(obj, file)




ssharp_program = """
class Point {
    var double x;
    var double y;
    
    fun (Point,double,double->Point) __init__(this, x, y) {
        this.x = x;
        this.y = y;
        return this;
    }

    fun (Point,Point->Point) add(this, other) {
        this.x = this.x + other.x;
        this.y = this.y + other.y;
        return this;
    }

}

"""

class Node:
    def __init__(self, tree, rsdd, issol=False, isroot=False, genfrom=None):
        self.tree, self.rsdd = tree, rsdd
        self.issol, self.isroot = issol, isroot
        self.genfrom = genfrom

    def __hash__(self):
        return hash(self.tree)

    def __eq__(self, other):
        return self.tree == other.tree

    def __neq__(self, other):
        return self.tree != other.tree


solutionset = lang2rules(slang)

root = Node(t:=ssharplang.parse(ssharp_program), 
            rsdd(solutionset, solutionset, s:=nodeset(t)), 
            issol=s.issubset(solutionset), 
            isroot=True,
            genfrom=None)

graph     = networkx.DiGraph()
queue     = []
iteration = 0
visited   = {root.tree}
graph.add_node(root)
heapq.heappush(queue, (0,root))

while queue:

    _, current = heapq.heappop(queue)

    print(f"iteration: {iteration}, queue: {len(queue)}, visited:{len(visited)}")

    for delta in ssharp2spp_deltas + [merge_delta(spp2s_deltas)]:
        try: 

            neighbor = Node(t:=delta(current.tree),
                        rsdd(solutionset, solutionset, s:=nodeset(t)),
                        issol=s.issubset(solutionset),
                        isroot=False,
                        genfrom=delta.__name__)
            
            if current == neighbor: pass
            elif neighbor.tree not in visited:
                visited.add(neighbor.tree)
                iteration += 1
                heapq.heappush(queue, (iteration, neighbor))
                graph.add_node(neighbor)
                graph.add_edge(current, neighbor)
            else:
                pass #graph.add_edge(current, neighbor)

        except NotAppliedException: pass

dump((graph,root))


