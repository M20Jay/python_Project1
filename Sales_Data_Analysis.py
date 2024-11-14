print("\nimporting libraries:")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("\nLoading Data and Filtering")
data = pd.read_csv('/Users/martinjames/Documents/Self-Research/Academic work 2024/Python Analysis/Data/Superstore_dataset.csv')
print(data.head(5))

print('\n listing columns')
print(data.columns.tolist())

print("\nselecting relevant columns for analysis:")
df = data[['Sales','Profit','Quantity','Discount']]
print(df)

# Checking data info (dataypes, non-null count)
print('\nDataset Info:')
print(df.info())

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe())

# Time series plots for trends
plt.figure(figsize=(15,10))
for i, column in enumerate (df.columns,1):
    plt.subplot(2,2,i)
    plt.plot(df[column])
    plt.title(f"{column} Trend Over Time")
    plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

#Missing Values Identification
print("\nMissing Values Count:")
print(df.isnull().sum())

#Visualizing Missing Values
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(),yticklabels=False,cmap="viridis")
plt.title('Missing Values Heatmap')
plt.show()

# Missing Values Treatment
df_cleaned = df.copy()

# Method 1: Mean imputation
df_cleaned=df_cleaned.fillna(df_cleaned.mean())

#Method 2: Forward Fill Option
# df_cleaned=df_cleaned.fillna(method='ffill')

print("\nVerifiy mising values after cleaning")
print(df_cleaned.isnull().sum())

# Moving Average Analysis
window_size = 7
plt.figure(figsize=(15,10))
for i, column in enumerate(df_cleaned.columns, 1):
    plt.subplot(2,2,i)
    plt.plot(df_cleaned[column], label ='Original', alpha =0.5)
    plt.plot(df_cleaned[column].rolling(window=window_size).mean(), label ='Moving Average', color ='red')
    plt.title(f"{column} with {window_size}-day Moving Average")
    plt.legend()
plt.tight_layout()
plt.show()

# Outlier Analysis
#creating histograms for outliers detection

plt.figure(figsize=(15,10))
for i, column in enumerate(df_cleaned.columns, 1):
    plt.subplot(2,2,i)
    sns.histplot(df_cleaned[column],kde=True)
    plt.title(f"Distribution of {column}")
plt.tight_layout()
plt.show()

# Calculating Outliers using IQR Method
for column in df_cleaned.columns:
    Q1 = df_cleaned[column].quantile(0.25)
    Q3=df_cleaned[column].quantile(0.75)
    IQR=Q3-Q1
    Outliers = df_cleaned[(df_cleaned[column]<(Q1-1.5*IQR))|(df_cleaned[column]>(Q3+1.5*IQR))]
    print(f"\nOutliers in {column}:{len(Outliers)}")