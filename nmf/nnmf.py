import numpy as np
from sklearn.decomposition import NMF
import networkx as nx
import matplotlib.pyplot as plt

# Generate a random social network graph
G = nx.erdos_renyi_graph(50, 0.2)

# Generate simulated diffusion data
# In this example, we simulate information diffusion with random values between 0 and 1.
diffusion_data = {node: np.random.rand() for node in G.nodes()}

# Create a matrix from the diffusion data
X = np.array(list(diffusion_data.values()))

# Perform NMF on the diffusion data
n_components = 2  # You can adjust this as needed
model = NMF(n_components=n_components, init='random', random_state=0)
W = model.fit_transform(X.reshape(1, -1))
H = model.components_

# Identify influential nodes
influential_nodes = np.argmax(W, axis=1)

# Visualize the network and influential nodes
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_nodes(G, pos, nodelist=influential_nodes, node_color='r')
plt.title('Social Network with Influential Nodes')
plt.show()

# Print influential nodes and their influence scores
print("Influential Nodes:")
for i, node in enumerate(influential_nodes):
    print(f"Node {node} - Influence Score: {W[0, i]}")
