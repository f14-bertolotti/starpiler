import pickle, networkx, configator, seaborn
import matplotlib.pyplot as plt
from functools import reduce

configuration = configator.Configator()

with open(configuration.draw.input_path, 'rb') as file:
    graph, _, _, _ = pickle.load(file)

pos = networkx.nx_agraph.graphviz_layout(graph, prog=configuration.draw.layout, args="")

max_rsdd = reduce(lambda x,y: x if x.rsdd > y.rsdd else y, graph.nodes).rsdd

palette = [color + (1,) for color in seaborn.color_palette(configuration.draw.palette, max_rsdd+1)]


node_color = [palette[int(node.rsdd)] for node in graph.nodes]
edge_color = [palette[int(e1.rsdd)] if not d["data"]["visited"] else [0,0,0,0.05] for e0,e1,d in graph.edges.data()]

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
            transparent=True)


