import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Data for the radar chart
labels = ['Sample Size', 'Short Evaluation Period', 'Technical Constraints']
values = [3, 4, 2]  # Scale from 1 (least impact) to 5 (most impact)

# Number of variables
num_vars = len(labels)

# Create the angle values for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart requires the values to be repeated for a closed loop
values += values[:1]
angles += angles[:1]

# Plot radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='coral', alpha=0.4)
ax.plot(angles, values, color='red', linewidth=2)

# Set labels for each axis
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Set the title of the chart
plt.title('Limitations Impact Analysis', size=20, color='darkblue', y=1.1)

plt.show()
