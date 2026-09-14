import pandas as pd

dataset = pd.read_csv('titanic.csv')

dataset['Relatives'] = dataset['SibSp'] + dataset['Parch']

data = pd.DataFrame(dataset, columns=['SibSp', 'Parch', 'Relatives'])

print(data)