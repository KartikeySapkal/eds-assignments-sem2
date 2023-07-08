import pandas as pd
import numpy as np

print("\nCreating DataFrame using pandas")
dataset= { 
    "Name": ["Kartikey","Vivek","Nachiket"],
    "Marks": [99,98,98],
    "City": ["Jalgaon","Pune","Jalgaon"]
}

df=pd.DataFrame(dataset)
print(df)
print(df.describe())
print(df.head(1))

# creating series data structure using pandas and numpy
print("\n\n\n")
print("Creating series using pandas and numpy.!!!")
a= np.array([1,2,3,4])
b= pd.Series(a,index=np.arange(4))

print(b)