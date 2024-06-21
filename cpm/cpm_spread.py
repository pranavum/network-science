import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import k_clique_communities

# Create a network
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (6, 7)])

# Function to visualize the network
def plot_network(G, pos, title):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=12)
    plt.title(title)
    plt.show()

# Plot the initial network
pos = nx.spring_layout(G)
plot_network(G, pos, "Initial Network")

# Step 1: Clique Identification
k = 3  # Set the clique size
cliques = list(k_clique_communities(G, k))

# Step 2: Visualize Cliques
for i, clique in enumerate(cliques):
    subgraph = G.subgraph(clique)
    plot_network(subgraph, pos, f"Clique {i + 1}")

# Step 3: Influence Propagation
# In this simplified example, influence will spread from nodes 1 and 3 to their neighbors.
influence_spreaders = {1, 3}
infected_nodes = set(influence_spreaders)

# Simulate influence propagation (a basic example)
while True:
    newly_infected = set()
    for node in infected_nodes:
        neighbors = set(G.neighbors(node))
        newly_infected.update(neighbors - infected_nodes)
    if not newly_infected:
        break
    infected_nodes.update(newly_infected)

print("Influence Propagation Results:")
print("Influential Nodes:", influence_spreaders)
print("Infected Nodes:", infected_nodes)

# Step 4: Information Cascade
# In this simple example, information spreads from clique 1 to clique 2.
cascade = set()
for clique in cliques:
    if 1 in clique:
        cascade.update(clique)

print("Information Cascade Results:")
print("Cascade Nodes:", cascade)

# Step 5: Clique Interaction
# Check for overlapping nodes between cliques
clique_overlap = [set(clique) for clique in cliques]
clique_interactions = []

for i in range(len(cliques)):
    for j in range(i + 1, len(cliques)):
        overlap = clique_overlap[i].intersection(clique_overlap[j])
        if overlap:
            clique_interactions.append((i, j, overlap))

print("Clique Interaction Results:")
print("Overlapping Cliques:", clique_interactions)
