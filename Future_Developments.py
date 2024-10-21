from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='Platform Future Development Process')

# Define nodes
dot.node('A', 'Start - Current Platform Features')
dot.node('B', 'Enhance Onboarding Process\n(Interactive Tutorials, Tooltips)')
dot.node('C', 'Incorporate Machine Learning\n(Predictive Matching)')
dot.node('D', 'Expand Collaboration Tools\n(Shared Workspaces, Task Management)')
dot.node('E', 'User Experience Feedback & Data Analysis')
dot.node('F', 'Continuous Improvement Loop')

# Define edges
dot.edge('A', 'B', label='Improving User Onboarding')
dot.edge('B', 'C', label='Better Personalized Matching')
dot.edge('C', 'D', label='Promote Teamwork')
dot.edge('D', 'E', label='Collect User Feedback')
dot.edge('E', 'F', label='Refine & Improve Platform', style='dashed')
dot.edge('F', 'B', label='Cycle of Continuous Improvement', style='dashed')

# Set graph attributes
dot.attr(label='Continuous Development Cycle for Platform Enhancement', fontsize='20')

# Render the process diagram
dot.render('platform_future_development', format='png', view=True)
