import tqdm, numpy, pickle, networkx, matplotlib

from src.utils import relative_set_difference_distance
from src.utils import lang2rules
from src.utils import nodeset

from src.syntax import slang

with open('data/trees.pickle', 'rb') as file:
    visited = pickle.load(file)

solutionset = lang2rules(slang)

id2tree = {i:tree for i,tree in enumerate(visited)}


dst_matrix = numpy.zeros((len(visited), len(visited)))

for i in tqdm.tqdm(range(len(visited))):
    for j in range(len(visited)):
        dst_matrix[i,j] = relative_set_difference_distance(solutionset, nodeset(id2tree[i]), nodeset(id2tree[j]))

dt = [('len', float)]
dst_matrix = dst_matrix.view(dt)
G = networkx.from_numpy_array(dst_matrix)

G = networkx.drawing.nx_agraph.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="red", style="setlinewidth(0.1)")

G.draw('data/out.png', format='png', prog='neato')

print(dst_matrix)

