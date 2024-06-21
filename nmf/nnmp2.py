import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF

# Create a synthetic social network graph
G = nx.karate_club_graph()

# Extract the adjacency matrix
adjacency_matrix = nx.to_numpy_array(G)

# Apply NMF to identify community structures
n_components = 3  # Number of components (communities) to extractx``
model = NMF(n_components=n_components, init='random', random_state=0)
W = model.fit_transform(adjacency_matrix)
H = model.components_

def maxIndex(array):
    max = 0
    for i in range(len(array)):
        if array[i] > array[max]:
            max = i
    return max

colors = dict(enumerate(["yellow","red","green"]))

# Visualize the network with community colors
community_colors = [colors[maxIndex(W[i])] for i in range(len(W))]
print(W)

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=300, node_color=community_colors, cmap=plt.get_cmap('viridis'), font_size=12)
plt.title("Social Network with Community Structure (NMF)")
plt.show()
