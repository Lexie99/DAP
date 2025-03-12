import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv')
# print(df.head())

# # Summary statistics
# print(df.describe())

# # Missing values
# print("\nMissing values:")
# print(df.isnull().sum())

# # Data distribution - histograms
# plt.figure(figsize=(10, 8))
# sns.histplot(df['performance'], kde=True)
# plt.title('Distribution of Performance')
# plt.xlabel('Performance')
# plt.ylabel('Frequency')
# plt.show()

# plt.figure(figsize=(10, 8))
# sns.histplot(df['age'], kde=True)
# plt.title('Distribution of Age')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# # Categorical variables - count plots
# plt.figure(figsize=(8, 6))
# sns.countplot(x='feedback', data=df)
# plt.title('Feedback Counts')
# plt.xlabel('Feedback')
# plt.ylabel('Count')
# plt.show()

# plt.figure(figsize=(8, 6))
# sns.countplot(x='gender', data=df)
# plt.title('Gender Distribution')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()

# plt.figure(figsize=(8, 6))
# sns.countplot(x='state', data=df)
# plt.title('State Distribution')
# plt.xlabel('State')
# plt.ylabel('Count')
# plt.show()

# # Correlation matrix
# plt.figure(figsize=(10, 8))
# sns.heatmap(df[['performance', 'trip_number', 'age', 'income']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Matrix')
# plt.show()


# Performance by gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='performance', data=df)
plt.title('Performance Ratings by Gender')
plt.xlabel('Gender')
plt.ylabel('Performance Rating')
plt.show()

# Trip frequency by state
plt.figure(figsize=(12, 8))
sns.barplot(x='state', y='trip_number', data=df)
plt.title('Average Trip Frequencies by State')
plt.xlabel('State')
plt.ylabel('Average Trip Number')
plt.xticks(rotation=45)
plt.show()

# Income vs. performance
plt.figure(figsize=(10, 8))
sns.scatterplot(x='income', y='performance', data=df)
plt.title('Income vs. Performance')
plt.xlabel('Income')
plt.ylabel('Performance Rating')
plt.show()




# Filter data for a specific age group (e.g., drivers aged 30-40)
age_group = df[(df['age'] >= 30) & (df['age'] <= 40)]
# Scatter plot for income vs. performance for the age group
plt.figure(figsize=(10, 8))
sns.scatterplot(x='income', y='performance', data=age_group)
plt.title('Income vs. Performance for Drivers Aged 30-40')
plt.xlabel('Income')
plt.ylabel('Performance Rating')
plt.show()

# Filter data for a specific gender (e.g. 1)
gender_group = df[df['gender'] == 1]
# Scatter plot for income vs. performance for the gender group
plt.figure(figsize=(10, 8))
sns.scatterplot(x='income', y='performance', data=gender_group)
plt.title('Income vs. Performance for Male Drivers')
plt.xlabel('Income')
plt.ylabel('Performance Rating')
plt.show()


# Scatter plot with color coded by gender
plt.figure(figsize=(10, 8))
sns.scatterplot(x='income', y='performance', hue='gender', data=df, palette='Set1')
plt.title('Income vs. Performance (Color Coded by Gender)')
plt.xlabel('Income')
plt.ylabel('Performance Rating')
plt.legend(title='Gender')
plt.show()


# Scatter plot with color coded by state
plt.figure(figsize=(12, 8))
sns.scatterplot(x='income', y='performance', hue='state', data=df, palette='viridis', legend='full')
plt.title('Income vs. Performance (Color Coded by State)')
plt.xlabel('Income')
plt.ylabel('Performance Rating')
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
