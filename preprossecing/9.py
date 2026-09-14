import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('titanic.csv')

dataset['Sex_Numeric'] = dataset['Sex'].map({'female': 0, 'male': 1})

dataset.plot(
    x='PassengerId',
    y='Sex_Numeric',
    kind='scatter',
    c='Sex_Numeric',
    colormap='Paired'
)

plt.show()