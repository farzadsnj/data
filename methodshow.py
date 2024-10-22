import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes with more detailed methodology aspects
nodes = {
    "Research Methodology": {
        "Design Science Approach": ["Iterative Development"],
        "Tech Stack": ["MERN Stack", "React.js", "Node.js", "MongoDB", "Express.js"],
        "Matching Algorithms": ["Gale-Shapley", "Competency-Based Matching"]
    }
}

# Add nodes to the graph
for main_node, branches in nodes.items():
    G.add_node(main_node)
    for sub_node, details in branches.items():
        G.add_node(sub_node)
        G.add_edge(main_node, sub_node)
        for detail in details:
            G.add_node(detail)
            G.add_edge(sub_node, detail)

# Set the layout for the nodes
pos = nx.spring_layout(G, seed=20)

# Draw the graph with methodology details
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=False)
plt.title("Research Methodology Hierarchical Layout", size=10)
plt.show()
