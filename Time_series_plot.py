import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
df = pd.DataFrame({
    'Sales': np.random.normal(1000, 100, len(dates)),
    'Profit': np.random.normal(200, 30, len(dates)),
    'Quantity': np.random.normal(50, 10, len(dates)),
    'Discount': np.random.normal(0.1, 0.02, len(dates))
})

print(df)

# Create more detailed time series plots
plt.figure(figsize=(15, 10))

for i, column in enumerate(df.columns, 1):
    # Create subplot
    plt.subplot(2, 2, i)

    # Plot with improved styling
    plt.plot(df.index, df[column],
             label=column,
             color='blue',
             linewidth=2,
             alpha=0.7)

    # Add mean line
    plt.axhline(y=df[column].mean(),
                color='red',
                linestyle='--',
                label='Mean')

    # Enhance the subplot
    plt.title(f'{column} Trend Over Time', fontsize=12, pad=20)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel(column, fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Rotate x-axis labels
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Print basic statistics for each column
for column in df.columns:
    print(f"\n{column} Statistics:")
    print(f"Mean: {df[column].mean():.2f}")
    print(f"Std Dev: {df[column].std():.2f}")
    print(f"Trend: {df[column].iloc[-1] - df[column].iloc[0]:.2f}")