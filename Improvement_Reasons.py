import matplotlib.pyplot as plt

# Data for the pie chart
factors = ['Matching Algorithm', 'User-Centered Design', 'Security Features', 'Other Factors']
contributions = [40, 30, 20, 10]
colors = ['gold', 'skyblue', 'lightgreen', 'lightcoral']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(contributions, labels=factors, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

# Adding title
ax.set_title('Contribution Factors to Improved User Efficiency and Satisfaction', fontsize=16)

# Displaying the chart
plt.tight_layout()
plt.savefig('contribution_factors_pie_chart.png', format='png', dpi=300)
plt.show()
