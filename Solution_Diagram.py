import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
g = nx.DiGraph()

# Define nodes for literature gaps and solutions
literature_gaps = [
    "Inadequate Matching Algorithms",
    "Insufficient Security Measures",
    "Poor User-Centric Design"
]

solutions = [
    "Advanced Matching Algorithms (Gale-Shapley & Competency-Based)",
    "Robust Security Protocols (SSL/TLS, JWT, OWASP Standards)",
    "User-Centered Design Approach (Feedback Integration)"
]

# Add nodes to the graph
for gap in literature_gaps:
    g.add_node(gap, color='red', style='filled', fillcolor='lightcoral')

for solution in solutions:
    g.add_node(solution, color='green', style='filled', fillcolor='lightgreen')

# Add edges from gaps to corresponding solutions
g.add_edge("Inadequate Matching Algorithms", "Advanced Matching Algorithms (Gale-Shapley & Competency-Based)")
g.add_edge("Insufficient Security Measures", "Robust Security Protocols (SSL/TLS, JWT, OWASP Standards)")
g.add_edge("Poor User-Centric Design", "User-Centered Design Approach (Feedback Integration)")

# Create a layout for the nodes
pos = nx.spring_layout(g, seed=42)

# Draw the nodes
node_colors = [g.nodes[node].get('fillcolor', 'white') for node in g.nodes]
nx.draw_networkx_nodes(g, pos, node_color=node_colors, node_size=3000, edgecolors='black')

# Draw the edges
nx.draw_networkx_edges(g, pos, arrowstyle='-|>', arrowsize=20, edge_color='black', connectionstyle='arc3,rad=0.1')

# Draw the labels
nx.draw_networkx_labels(g, pos, font_size=10, font_weight='bold', verticalalignment='center', horizontalalignment='center')

# Display the plot
plt.title("Literature Gaps and Solutions")
plt.axis('off')
plt.show()
