#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
i=1
G.add_node(i,pos=(i,i))
G.add_node(2,pos=(2,2))
G.add_node(3,pos=(4,1))
G.add_node(4, pos = (2, 0))
G.add_edge(1, 2, weight = 0.5)
G.add_edge(1, 4, weight = 0.8)
G.add_edge(2, 3, weight = 1.4)
G.add_edge(4, 3, weight = 2.1)
G.add_edge(1, 3)
G.add_edge(2, 4)

pos=nx.get_node_attributes(G,'pos')
labels = {1: 'A', 3:'B', 2: 'C', 4: 'D'}
nx.draw(G, pos)

nx.draw_networkx_labels(G,pos, labels)
labels = {(1, 2): "x/100", (1, 4): "3.1", (2, 3): "3.1", (4, 3):"y/100", (2, 4): "0", (1, 3):"5"}
print (labels)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("ncm_assgn5.png")
