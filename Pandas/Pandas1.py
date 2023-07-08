import numpy as np
import pandas as pd

dict1={
    "City":["Jalgaon","Pune","Aurangabad"],
    "Marks":[30,98,99],
    "Name":["Lokesh","Kartik","Nachiket"]
}

df=pd.DataFrame(dict1)

print(df)

df.to_csv("Data.csv")

df.to_csv("FalseIndexData.csv",index=False)

print("\n\n",df.head(1))
print("\n\n",df.tail(1))
print("\n\n",df.describe())