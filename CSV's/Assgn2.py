import csv
from collections import Counter

f1 = open("CSV's/Sales.csv","r")

product_details = [ ]
supplier_details = { }
customer_details = [ ]
gender = { }

while(True):
    data = f1.readline() 
    if not data:
        break;
    #print(data)

    data = data.replace("\n","")
    # print(data)
    temp = data.split(",")
    # print(temp)

    product_details.append(temp[1])
    customer_details.append(temp[3])
    supplier_details.update({temp[1]:temp[2]})
    gender.update({temp[3]:temp[4]})

f1.close()

customer_details = tuple(customer_details)


frequency = { }
for item in product_details:
    if item in frequency: 
        frequency[item]+=1
    else: 
        frequency[item]=1

# print(frequency.items)
# print(list(frequency.items()))
# SortedFrequency = sorted(frequency.items(),key = lambda x:x[1],reverse=True)
# print(SortedFrequency)

supplierList = list(supplier_details.items())

print(supplierList)

suppliers = []
for i in range(len(supplierList)): 
    suppliers.append(supplierList[i][1])

print(suppliers)

supp = Counter(suppliers)
print(supp)