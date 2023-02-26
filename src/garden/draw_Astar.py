import pickle, networkx, configator
import matplotlib.pyplot as plt

configuration = configator.Configator()
v = configuration.draw.rgba_visited
u = configuration.draw.rgba_unvisited
s = configuration.draw.rgba_special

with open(configuration.draw.input_path, 'rb') as file:
    graph, _, _, visited = pickle.load(file)


pos = networkx.nx_agraph.graphviz_layout(graph, prog=configuration.draw.layout)

node_color = [[s.r,s.g,s.b,s.a] if node.isroot or (node.tree in visited) else [u.r,u.g,u.b,u.a] for node in graph.nodes]
edge_color = [[s.r,s.g,s.b,s.a] if ((e0.issol or e0.isroot) and e1.issol) or (e0.tree in visited and e1.tree in visited and d["data"]["visited"]==False) else ([u.r,u.g,u.b,u.a] if not d["data"]["visited"] else [v.r,v.g,v.b,v.a]) for e0,e1,d in graph.edges.data()]

networkx.draw(graph, 
              pos, 
              arrows=False, 
              node_color=node_color, 
              edge_color=edge_color, 
              width=configuration.draw.width,
              linewidths=configuration.draw.linewidths,
              node_size=configuration.draw.node_size)

if configuration.draw.show: plt.show()
plt.savefig(configuration.draw.output_path,dpi=configuration.draw.dpi,format=configuration.draw.format)


