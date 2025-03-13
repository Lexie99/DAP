import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv('data.csv', parse_dates=['date_time'])

# data summary
print(df.head())
print(df.describe())

# Q1: EDA
# 1. performance distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['performance'], kde=True, bins=30)
plt.title('performance distribution')
plt.subplot(1, 2, 2)
sns.boxplot(x=df['performance'])
plt.title('performance boxplot')
plt.tight_layout()
plt.show()

# 2. age and performance
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='performance', data=df, alpha=0.6)
plt.title('age vs. performance')
plt.xlabel('age')
plt.ylabel('performance')
plt.tight_layout()
plt.show()

# 3. gnder difference（assume 1=Female, 0=Male）
gender_group = df.groupby('gender').agg(
    avg_performance=('performance', 'mean'),
    feedback_rate=('feedback', 'mean'),
    avg_trip=('trip_number', 'mean')
).reset_index()
gender_group['gender'] = gender_group['gender'].map({0: 'Male', 1: 'Female'})

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.barplot(x='gender', y='avg_performance', data=gender_group)
plt.title('gender and average performance')
plt.subplot(1, 3, 2)
sns.barplot(x='gender', y='feedback_rate', data=gender_group)
plt.title('gender and feedback rate')
plt.subplot(1, 3, 3)
sns.barplot(x='gender', y='avg_trip', data=gender_group)
plt.title('gnder and average trip number')
plt.tight_layout()
plt.show()

# 4. performance by state
state_performance = df.groupby('state')['performance'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=state_performance.values, y=state_performance.index, palette='viridis')
plt.title('average perfomance by state')
plt.xlabel('performance')
plt.ylabel('state')
plt.tight_layout()
plt.show()

# Q2: sub sample analysis（use median as indicator variable）
median_perf = df['performance'].median()
df['performance_group'] = df['performance'].apply(lambda x: 'High' if x >= median_perf else 'Low')

# performance group comparison
group_comparison = df.groupby('performance_group').agg(
    avg_trip=('trip_number', 'mean'),
    feedback_rate=('feedback', 'mean'),
    avg_age=('age', 'mean'),
    avg_income=('income', 'mean')
).reset_index()

print("\nPerformance group comparison:")
print(group_comparison)

# visualization
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.barplot(x='performance_group', y='avg_trip', data=group_comparison)
plt.title('average trip number')
plt.subplot(2, 2, 2)
sns.barplot(x='performance_group', y='feedback_rate', data=group_comparison)
plt.title('feedback rate')
plt.subplot(2, 2, 3)
sns.barplot(x='performance_group', y='avg_age', data=group_comparison)
plt.title('average age')
plt.subplot(2, 2, 4)
sns.barplot(x='performance_group', y='avg_income', data=group_comparison)
plt.title('average income')
plt.tight_layout()
plt.show()