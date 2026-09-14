import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('titanic.csv')

cleaned_dataset = dataset.dropna(subset=['Age'])

dataset.plot(x='PassengerId', y='Age', kind='scatter', c='Age', colormap='Paired')

plt.show()