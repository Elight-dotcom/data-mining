import pandas as pd

dataset = pd.read_csv('titanic.csv')
class_counts = dataset['Sex'].value_counts()

print(class_counts)