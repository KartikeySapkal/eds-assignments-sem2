import pandas as pd
import numpy as np

df= pd.read_csv("CSV's/PandasDataset.csv")

print(df.head(5))
print(df.tail(5))
print(df.info())
print(df.describe())


