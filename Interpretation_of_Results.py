from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='Matching Algorithm Implementation Flowchart')

# Define nodes
dot.node('A', 'Start Matching Process')
dot.node('B', 'Researcher Preferences')
dot.node('C', 'Project Requirements')
dot.node('D', 'Gale-Shapley Algorithm')
dot.node('E', 'Competency-Based Matching')
dot.node('F', 'Successful Match')

# Define edges
dot.edge('A', 'B', label='Collect Researcher Data')
dot.edge('A', 'C', label='Collect Project Data')
dot.edge('B', 'D', label='Preference Weighting')
dot.edge('C', 'D', label='Project Requirements Analysis')
dot.edge('D', 'E', label='Apply Gale-Shapley Algorithm')
dot.edge('E', 'F', label='Match Evaluation')
dot.edge('F', 'A', label='Iterate if No Match', constraint='false')

# Render the flowchart
dot.render('matching_algorithm_flowchart', format='png', view=True)
