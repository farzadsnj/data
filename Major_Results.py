import matplotlib.pyplot as plt
import pandas as pd

# Setting up the figure layout
plt.figure(figsize=(20, 15))

# 1. Platform Usage Metrics - Bar Chart
plt.subplot(2, 2, 1)
metrics = ['Matching Time (hrs)', 'Successful Matches (%)', 'Bounce Rate (%)']
traditional_values = [3.5, 60, 50]  # Traditional Platforms
developed_values = [1.8, 88, 12]  # Developed Platform

x = range(len(metrics))
plt.bar(x, traditional_values, width=0.4, label='Traditional Platforms', align='center')
plt.bar(x, developed_values, width=0.4, label='Developed Platform', align='edge')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.title('Platform Usage Metrics Comparison')
plt.xticks(x, metrics)
plt.legend()

# 2. User Satisfaction and Usability - Table
plt.subplot(2, 2, 2)
data = {
    "Metric": ["System Usability Scale", "User Satisfaction Rating", "Matching Accuracy"],
    "Average Score": [85, "4.6 / 5", "90%"],
    "Benchmark": [68, "N/A", "70%"]
}
df = pd.DataFrame(data)

# Removing axes and displaying the table
plt.axis('off')
plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
plt.title('User Satisfaction Metrics', pad=20)

# 3. Security Assessment Results - Bar Chart
plt.subplot(2, 2, 3)
security_metrics = ['Critical Vulnerabilities', 'Successful Breaches', 'User Trust (%)']
values = [0, 0, 95]  # Outcomes

plt.bar(security_metrics, values, color=['red', 'red', 'green'])
plt.ylabel('Results')
plt.title('Security Assessment Results')

# 4. Secondary Results - Pie Charts
plt.subplot(2, 2, 4)
# Data for Feature Adoption and Profile Completeness
labels_adoption = ['Used Messaging Feature', 'Did Not Use Messaging Feature']
sizes_adoption = [80, 20]

# Plotting feature adoption pie chart
plt.pie(sizes_adoption, labels=labels_adoption, autopct='%1.1f%%', startangle=140)
plt.title('Feature Adoption Rate')

plt.tight_layout()
plt.show()
