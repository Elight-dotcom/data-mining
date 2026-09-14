import pandas as pd

dataset = pd.read_csv('titanic.csv')
class_counts = dataset['Pclass'].value_counts()

print(class_counts)