import pandas as pd

df = pd.read_csv("../datasets/ml-100k/u.data")

df[1:3]

print(df.head())