import pandas as pd

data = pd.read_csv("googleplaystore.csv")

print(data.head())
print(data.columns)
print(data.info())
print(data.describe())