import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data for bar chart
platforms = ['Traditional Platform', 'Developed Platform']
average_matching_time = [3.5, 1.8]  # in hours per week
success_rate = [60, 88]  # in percentage

# Set the positions and width for the bars
x = np.arange(len(platforms))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the matching efficiency
bars1 = ax.bar(x - width/2, average_matching_time, width, label='Avg. Matching Time (hrs)', color='skyblue')

# Plotting the success rate percentage
bars2 = ax.bar(x + width/2, success_rate, width, label='Success Rate (%)', color='lightgreen')

# Adding titles and labels
ax.set_xlabel('Platform Type')
ax.set_ylabel('Metrics')
ax.set_title('Comparison of Matching Time and Success Rate Between Traditional and Developed Platforms')
ax.set_xticks(x)
ax.set_xticklabels(platforms)
ax.legend()

# Adding data labels to each bar
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

plt.tight_layout()
plt.savefig('comparison_matching_success.png')  # Saving the chart as an image file
plt.show()

# Data for usability metrics table
usability_data = {
    'Metric': ['System Usability Scale (SUS)', 'User Satisfaction Rating', 'Matching Accuracy'],
    'Average Score': [85, 4.6, 90],
    'Benchmark': [68, 'N/A', 70]
}

# Creating a pandas DataFrame
usability_df = pd.DataFrame(usability_data)

# Displaying the table in a formatted output
print("\nUser Satisfaction Metrics:\n")
print(usability_df.to_string(index=False))
