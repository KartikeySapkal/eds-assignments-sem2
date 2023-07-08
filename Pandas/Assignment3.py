import numpy as np
import pandas as pd

all_data = pd.read_csv("/Users/kartikeysapkal/Documents/Python/CSV's/PandasDataset.csv")
# print(all_data)
# print(all_data.shape)
# print(all_data.columns)
nan_df  = all_data[all_data.isna().any(axis=1)]
# print(nan_df)
# print(nan_df.shape)
all_data = all_data.dropna(how='all')
# print(all_data)
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
# print(all_data)
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('Int32')
print(all_data)

# all_data['Month2'] = pd.to_datetime(all_data['Order Date']).dt.month
# print(all_data)


def get_city(address): 
    return address.split(",")[1].strip(" ")

def get_state(address): 
    return address.split(",")[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)}({get_state(x)})")

print(all_data)

all_data["Sales"] = all_data['Quantity Ordered'].astype('int') * all_data['Price Each'].astype('float')

print(all_data.groupby(['Month']).sum())