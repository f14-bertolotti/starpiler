import pickle, networkx, configator
import matplotlib.pyplot as plt

configuration = configator.Configator()

v = configuration.draw.rgba_visited
u = configuration.draw.rgba_unvisited 
s = configuration.draw.rgba_special

with open(configuration.draw.input_path, 'rb') as file:
    graph, root, _, _ = pickle.load(file)

pos = networkx.nx_agraph.graphviz_layout(graph, prog=configuration.draw.layout, args="")

for node in filter(lambda x:x.issol, graph.nodes):
    path = networkx.shortest_path(graph, root, node)
    for n in path: n.issol = True


node_color = [[s.r,s.g,s.b,s.a] if node.isroot or node.issol else [u.r,u.g,u.b,u.a] for node in graph.nodes]
edge_color = [[s.r,s.g,s.b,s.a] if (e0.issol or e0.isroot) and e1.issol else ([u.r,u.g,u.b,u.a] if not d["data"]["visited"] else [v.r,v.g,v.b,v.a]) for e0,e1,d in graph.edges.data()]

networkx.draw(graph, 
              pos, 
              arrows=False, 
              node_color=node_color, 
              edge_color=edge_color, 
              width=configuration.draw.width,
              linewidths=configuration.draw.linewidths,
              node_size=configuration.draw.node_size)

if configuration.draw.show: plt.show()

plt.savefig(configuration.draw.output_path,
            dpi=configuration.draw.dpi,
            format=configuration.draw.format,
            transparent=True, 
            bbox_inches='tight')


