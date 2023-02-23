import pickle, networkx
import matplotlib.pyplot as plt
import matplotlib


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

with open('data/trees.pickle', 'rb') as file:
    graph, root = pickle.load(file)


pos = networkx.nx_agraph.graphviz_layout(graph, prog="twopi", args="")

for node in filter(lambda x:x.issol, graph.nodes):
    path = networkx.shortest_path(graph, root, node)
    for n in path: n.issol = True



node_color = ["red" if node.isroot or node.issol else "black" for node in graph.nodes]
edge_color = ["red" if (edge[0].issol or edge[0].isroot) and edge[1].issol else "black" for edge in graph.edges]

networkx.draw(graph, 
              pos, 
              arrows=False, 
              node_color=node_color, 
              edge_color=edge_color, 
              width=1,
              linewidths=1,
              node_size=3)
plt.show()
#plt.savefig("data/graph.pdf",dpi=600,format="pdf")


