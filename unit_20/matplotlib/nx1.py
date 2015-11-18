import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from(range(1,8))
G.add_weighted_edges_from([(1,7,15),(1,3,6),(1,5,7),
                           (1,6,6),(1,2,4),(2,4,10),
                           (3,5,10),(3,7,5),(3,6,5),
                           (4,7,3),(4,5,15),(5,6,5)])

pos = nx.spring_layout(G) # positions for all nodes

# nodes and node labels
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

# edges
edges = [(u,v) for (u,v,d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, edgelist=edges, font_size=16)

# edge labels
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

plt.show() # matplotlib.pyplot.show()