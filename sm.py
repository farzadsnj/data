import matplotlib.pyplot as plt
import numpy as np

# Define the types of vulnerabilities and corresponding data
vulnerabilities = ['SQL Injection', 'Cross-Site Scripting (XSS)', 'Cross-Site Request Forgery (CSRF)', 'Sensitive Data Exposure', 'Broken Authentication']
before_security_measures = [5, 7, 6, 8, 5]  # Number of vulnerabilities found before security measures
after_security_measures = [0, 1, 0, 1, 0]   # Number of vulnerabilities found after security measures

# Set the positions and width for the bars
x = np.arange(len(vulnerabilities))
width = 0.35

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the bars for before and after security measures
bars_before = ax.bar(x - width/2, before_security_measures, width, label='Before Security Measures', color='lightcoral')
bars_after = ax.bar(x + width/2, after_security_measures, width, label='After Security Measures', color='lightgreen')

# Add labels, title, and legend
ax.set_xlabel('Vulnerability Type', fontsize=12)
ax.set_ylabel('Number of Vulnerabilities', fontsize=12)
ax.set_title('Security Assessment Results: Before vs After Implementation of Security Measures', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(vulnerabilities, rotation=45, ha='right')
ax.legend()

# Adding value labels on top of each bar for better readability
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset the text slightly
                    textcoords="offset points",
                    ha='center', va='bottom')

add_value_labels(bars_before)
add_value_labels(bars_after)

# Display the plot
plt.tight_layout()
plt.show()
