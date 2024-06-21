import networkx as nx
import matplotlib.pyplot as plt
import community  # Louvain method for modularity maximization

# Create a social network graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (6, 7)])

# Visualize the initial network
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=12)
plt.title("Initial Network")
plt.show()

# Step 1: Perform Modularity Maximization (Community Detection)
partition = community.best_partition(G)

# Visualize the communities
plt.figure(figsize=(8, 6))
values = [partition.get(node) for node in G.nodes()]
nx.draw(G, pos, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, node_size=300, font_size=12)
plt.title("Community Detection (Modularity Maximization)")
plt.show()

# Step 2: Information Cascade
# Simulate an information cascade from a seed node within a community (e.g., community 0).
seed_node = 1
infected_nodes = {seed_node}

def simulate_cascade(G, infected_nodes):
    while True:
        newly_infected = set()
        for node in infected_nodes:
            neighbors = set(G.neighbors(node))
            newly_infected.update(neighbors - infected_nodes)
        if not newly_infected:
            break
        infected_nodes.update(newly_infected)

simulate_cascade(G, infected_nodes)

# Step 3: Influence Propagation Analysis
# Measure the size of the information cascade and other propagation metrics.
cascade_size = len(infected_nodes)
print(f"Information Cascade Size: {cascade_size}")

# Step 4: Visualization of Results
# Visualize the cascade within the network.

# For illustrative purposes, you can label nodes in the cascade.
labels = {node: 'Cascade' if node in infected_nodes else f"Community {community_id}" for node, community_id in partition.items()}
nx.set_node_attributes(G, labels, 'info_status')

plt.figure(figsize=(8, 6))
node_colors = ['lightblue' if node in infected_nodes else 'lightgray' for node in G.nodes()]
nx.draw(G, pos, node_color=node_colors, node_size=300, font_size=12, labels=nx.get_node_attributes(G, 'info_status'))
plt.title("Information Cascade and Community-Labeled Network")
plt.show()
