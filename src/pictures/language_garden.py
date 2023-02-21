import networkx, pickle, heapq

from src.syntax import ssharplang
from src.transpilers import ssharp2spp_transpile, ssharp2spp_deltas
from src.transpilers import spp2s_transpile, spp2s_deltas
from src.semantics.slang import run
from src.utils import NotAppliedException
from src.utils import merge_delta

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

queue = []
heapq.heappush(queue, (0,0,ssharp_tree))
visited = set()
iteration = 0

while queue:

    if iteration % 1000 == 0: dump(visited)

    l, i, current = heapq.heappop(queue)
    print(f"iteration: {iteration}, queue: {len(queue)}, visited:{len(visited)}, len:{l}")

    for delta in ssharp2spp_deltas + [merge_delta(spp2s_deltas)]:
        try: 
            neighbor = (l + 1, iteration, delta(current)) 
            if neighbor not in visited and neighbor[0] < 20:
                iteration += 1
                heapq.heappush(queue, neighbor)
                visited.add(neighbor[2])
        except NotAppliedException: pass


dump(visited)





