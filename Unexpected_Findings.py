import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
categories = ['Competency Input Complexity', 'Navigation Issues', 'Lack of Guidance']
user_count = [50, 30, 20]

# Total affected users
total_users = 50
affected_percentages = [50, 30, 20]

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar chart
bars = ax.barh(categories, user_count, color=['#f4a261', '#2a9d8f', '#e76f51'], edgecolor='black')

# Add data labels to each bar
for bar, percent in zip(bars, affected_percentages):
    plt.text(bar.get_width() - 5, bar.get_y() + bar.get_height() / 2, f'{percent}%', ha='center', va='center', fontsize=12, color='black')

# Adding title and labels
ax.set_title('Difficulties Faced by Users During Profile Setup', fontsize=16)
ax.set_xlabel('Number of Users Reporting Issues', fontsize=14)
ax.set_ylabel('Category of Difficulty', fontsize=14)

# Display the chart
plt.tight_layout()
plt.savefig('user_profile_setup_difficulties.png', format='png', dpi=300)
plt.show()
