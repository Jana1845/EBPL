import pandas as pd

import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv("Diabetes.csv")

# Pie chart of 'Outcome'

outcome_counts = df['Outcome'].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(outcome_counts, labels=['Non-diabetic', 'Diabetic'], autopct='%1.1f%%', 

startangle=90)

plt.title('Outcome Distribution')

plt.show()

# Line plot of 'Glucose'

plt.figure(figsize=(10, 5))

plt.plot(df['Glucose'], color='red')

plt.title('Glucose Levels Over Index')

plt.xlabel('Index')

plt.ylabel('Glucose')

plt.show()
