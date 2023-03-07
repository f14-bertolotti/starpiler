import configator, pathlib, networkx, random, pickle, heapq
from src.syntax          import slang, spplang, ssharplang
from src.transpilers     import s2spp_deltas, spp2s_deltas, ssharp2spp_deltas
from src.utils           import NotAppliedException
from src.utils           import relative_set_difference_distance as rsdd
from src.utils           import lang2rules
from src.utils           import nodeset
from src.transpilers     import MetaTranspiler
from src.transpilers.s   import metric01 as s_metric
from src.transpilers.spp import metric01 as spp_metric
from src.garden.Utils    import dump, Node


configuration = configator.Configator()

random.seed(configuration.garden.seed)

metric = {"spplang":spp_metric,"slang":s_metric}[configuration.garden.solutionset]
ssharp_program = pathlib.Path(configuration.garden.input_path).read_text()
solutionset = lang2rules(locals()[configuration.garden.solutionset])
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

deltas = random.sample(ssharp2spp_deltas, int(len(ssharp2spp_deltas) * configuration.garden.ssharp2spp)) + \
         random.sample(spp2s_deltas     , int(len(spp2s_deltas)      * configuration.garden.spp2s)) + \
         random.sample(s2spp_deltas     , int(len(s2spp_deltas)      * configuration.garden.s2spp))
random.shuffle(deltas)

print(len(deltas))

while queue:

    if iteration > configuration.garden.max_iterations: break 
    _, current = heapq.heappop(queue)

    print(f"\riteration: {iteration}, queue: {len(queue)}, visited:{len(visited)} ...",end="")

    for delta in deltas:
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
                graph.add_edge(current, neighbor, data={"visited":False})
            else:
                graph.add_edge(current, neighbor, data={"visited":True})


        except NotAppliedException: pass
        
print("DONE")

print("A* search ...", end="", flush=True)
sol,Astar_visited = MetaTranspiler(ssharp2spp_deltas + spp2s_deltas, None, return_visited=True).search_Astar(root.tree, solutionset)
Astar_visited.add(sol)
print("DONE")

print("bfs search ...", end="", flush=True)
sol,bfs_visited = MetaTranspiler(ssharp2spp_deltas + spp2s_deltas, metric, return_visited=True).search(root.tree)
bfs_visited.add(sol)
print("DONE")

dump((graph,root,bfs_visited,Astar_visited), configuration.garden.output_path)


