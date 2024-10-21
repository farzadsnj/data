import matplotlib.pyplot as plt
import numpy as np

# Data for user satisfaction metrics
metrics = ['System Usability Scale (SUS)', 'User Satisfaction Rating', 'Matching Accuracy']
average_scores = [85, 4.6, 90]  # Average scores for each metric
benchmarks = [68, 3.5, 70]  # Benchmarks for each metric (assuming 3.5 as a neutral benchmark for satisfaction rating)

# Define the x-axis positions for the bars
x = np.arange(len(metrics))
width = 0.35  # Width of the bars

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, average_scores, width, label='Average Score', color='#4CAF50')
bars2 = ax.bar(x + width/2, benchmarks, width, label='Benchmark', color='#FFC107')

# Add labels, title, and legend
ax.set_xlabel('Metrics')
ax.set_ylabel('Scores')
ax.set_title('User Satisfaction Metrics vs. Benchmarks')
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=15, ha='right')
ax.legend()

# Adding text annotations to show values on top of the bars
for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=10)

# Display the plot
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
