import matplotlib.pyplot as plt

# Data for secondary results
labels = ['Utilized Messaging Feature', 'Did Not Utilize Messaging Feature']
feature_adoption = [80, 20]  # Percentage of participants who used the messaging feature vs. those who did not

# Create a pie chart for feature adoption
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(feature_adoption, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'], wedgeprops={'edgecolor': 'black'})

# Add title
ax.set_title('Feature Adoption: Messaging Feature Utilization')

# Display the plot
plt.tight_layout()
plt.show()

# Data for profile completeness
labels = ['More Likely to Receive Offers', 'Less Likely to Receive Offers']
profile_completeness = [25, 75]  # Percentage likelihood of receiving project offers with complete profiles vs. incomplete profiles

# Create a pie chart for profile completeness
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(profile_completeness, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#2196F3', '#FF5722'], wedgeprops={'edgecolor': 'black'})

# Add title
ax.set_title('Impact of Profile Completeness on Receiving Project Offers')

# Display the plot
plt.tight_layout()
plt.show()
