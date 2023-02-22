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

solutionset = lang2rules(spplang)

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

ssharp_tree = ssharplang.parse(ssharp_program)
ssharp_tree.value = rsdd(solutionset, solutionset, nodeset(ssharp_tree))

graph = networkx.DiGraph()
graph.add_node(ssharp_tree)
queue = []
heapq.heappush(queue, (0,0,ssharp_tree))
iteration = 0
visited = {ssharp_tree}

while queue:

    l, i, current = heapq.heappop(queue)

    if nodeset(current).issubset(solutionset): break

    print(f"iteration: {iteration}, queue: {len(queue)}, visited:{len(graph)}, len:{l}")

    for delta in ssharp2spp_deltas:
        try: 
            neighbor = (l + 1, iteration, delta(current)) 
            neighbor[2].value = rsdd(solutionset, solutionset, nodeset(neighbor[2]))
            if neighbor[2] not in visited:
                visited.add(neighbor)
                iteration += 1
                heapq.heappush(queue, neighbor)
                graph.add_node(neighbor[2]) 
                graph.add_edge(current, neighbor[2], weight=rsdd(solutionset, nodeset(current), nodeset(neighbor[2])))
        except NotAppliedException: pass


dump((graph,ssharp_tree))





