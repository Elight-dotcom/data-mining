import pandas as pd

dataset = pd.read_csv('titanic.csv')

rows, cols = dataset.shape

print("Number of Rows: ", rows)
print("Number of Columns: ", cols)