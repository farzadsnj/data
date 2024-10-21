import matplotlib.pyplot as plt

# Data for comparison of average matching time
platforms = ['Traditional Platforms', 'Developed Platform']
average_matching_time = [3.5, 1.8]  # in hours

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(platforms, average_matching_time, color=['#ff9999','#66b3ff'])
plt.xlabel('Platform Type')
plt.ylabel('Average Matching Time (hours)')
plt.title('Figure 1: Comparison of Average Matching Time Between Traditional Platforms and Developed Platform')

# Adding text annotations to show values
for index, value in enumerate(average_matching_time):
    plt.text(index, value + 0.05, f'{value} hrs', ha='center', fontsize=12)

# Display the plot
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
