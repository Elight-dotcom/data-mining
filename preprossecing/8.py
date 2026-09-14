import pandas as pd

dataset = pd.read_csv('titanic.csv')

survival_counts = pd.crosstab(index=dataset['Pclass'], columns=dataset['Survived'])

survival_counts.columns = ['Tidak Selamat (0)', 'Selamat (1)']

print(survival_counts)