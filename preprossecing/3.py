import pandas as pd

dataset = pd.read_csv('titanic.csv')

data = pd.DataFrame(dataset, columns=['Name', 'Sex', 'Age', 'Pclass', 'Fare'])

print(data)