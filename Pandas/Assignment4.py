
import pandas as pd
import numpy as np

f1 = open("/Users/kartikeysapkal/Documents/Python/CSV's/grainsales.csv","r")

data = pd.read_csv(f1)



df = pd.DataFrame(data)

maindata = df #im creating this variable to reset my dataframe

df['Sales'].describe()

df=df.groupby('Months').sum()

df=df.sort_values(by=['Sales'],ascending=False)

df.head(1)

print("Best Month for Sales: July")

print("Revenue Earned was: 16000000")

df = maindata

df = df.groupby("GrainName").sum()
df = df.sort_values(by=["Sales"],ascending = False)
df.head(1)

print("Most Sold Grain is: Wheat")
print("The Best Month for sales is July and this product has occured in July so this is most sold product with highest sales")

df = maindata
df= df.groupby("City").sum()
df = df.sort_values(by = ['Sales'],ascending= False)
df.head(1)

print("'Asansole' Has sold highest no. of products")
df = maindata 

df = df.groupby('State').sum()
df = df.sort_values(by = ['Sales'],ascending = False)
print("West Bengol has highest sales")
