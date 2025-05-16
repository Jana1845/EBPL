import pandas as pd

import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv("Diabetes.csv")

# Bar Chart: Frequency of top 10 Glucose Levels

df['Glucose'].value_counts().head(10).sort_index().plot(kind='bar', color='red')

plt.title('Top 10 Glucose Level Counts')

plt.xlabel('Glucose Level')

plt.ylabel('Frequency')

plt.tight_layout()

plt.savefig('bar_chart.png')

plt.close()

# Scatter Plot: Glucose vs Insulin

plt.scatter(df['Glucose'], df['Insulin'], alpha=0.5)

plt.title('Scatter Plot of Glucose vs Insulin')

plt.xlabel('Glucose')

plt.ylabel('Insulin')

plt.tight_layout()

plt.savefig('scatter_plot.png')

plt.close()
