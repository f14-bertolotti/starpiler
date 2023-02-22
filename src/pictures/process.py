import pickle, networkx
import matplotlib.pyplot as plt
import matplotlib

with open('data/trees.pickle', 'rb') as file:
    graph, root = pickle.load(file)

pos = networkx.nx_agraph.graphviz_layout(graph, root=0, prog="dot", args="")
node_color = [node.value for node in graph.nodes]
edge_color = [edge[0].value for edge in graph.edges]

networkx.draw(graph, 
              pos, 
              #arrows=False, 
              node_color=node_color, 
              edge_color=edge_color, 
              cmap=matplotlib.colormaps["magma"], 
              edge_cmap=matplotlib.colormaps["magma"],
              node_size=5)
plt.show()
#plt.savefig("data/graph.pdf",dpi=600,format="pdf")


