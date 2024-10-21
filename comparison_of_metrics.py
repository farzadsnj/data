import matplotlib.pyplot as plt
import numpy as np

# Data for comparison
metrics = ['Matching Efficiency (hrs)', 'Success Rate (%)', 'Security (Vulnerabilities)']
traditional_platform = [3.5, 60, 5]  # Values: Avg matching time, Success rate, Security vulnerabilities
developed_platform = [1.8, 88, 0]     # Values: Avg matching time, Success rate, Security vulnerabilities

# X-axis setup
x = np.arange(len(metrics))
width = 0.35  # Width of bars

# Plotting the side-by-side bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, traditional_platform, width, label='Traditional Platform', color='skyblue')
bars2 = ax.bar(x + width/2, developed_platform, width, label='Developed Platform', color='orange')

# Adding labels, title, and legend
ax.set_xlabel('Metrics')
ax.set_ylabel('Values')
ax.set_title('Comparison of Key Metrics: Developed Platform vs. Traditional Platform')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Adding value labels to bars for better readability
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset above the bar
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

# Displaying the plot
plt.tight_layout()
plt.savefig('comparison_of_metrics.png', format='png', dpi=300)
plt.show()
