# Prepare/Take datasets for any real-life application. For Ex. Sales of the company. Read the data from Sales.csv/.xls/.txt. Store Product details in the List data structure. Store Supplier Details in Dictionary Data Structure. Store Customer Details in Tuple Data Structure. Now perform the following operations:

#  Find the most popular product for sale.
#  Find the best supplier for sales.
#  Find the customer who buys most of the products.
#  Find the number of customers who are ‘Female’



import csv
from collections import Counter
f1 = open("CSV's/Sales.csv","r")

product_detials = [ ]
supplier_details = { }
customer_details = [ ]
supplist= [ ]
customer = [ ]
gender = [ ]

while(True): 
    data= f1.readline()
    if not data: 
        break;
    print(data)
    data = data.replace("\n","")
    # print(data)
    temp = data.split(",")
    # print(temp)
    product_detials.append(temp[1])
    customer_details.append(temp[3])
    supplier_details.update({temp[2]:temp[1]})
    supplist.append(temp[2])
    customer.append(temp[3])
    gender.append(temp[4])

f1.close() 

customer_details= tuple(customer_details)

# print(supplier_details)
# print(supplist)

Supp_dict =(Counter(supplist))
# print(Supp_dict)

supplist1 = sorted(Supp_dict.items(),key=lambda x : x[1], reverse = True)
supplist1 = list(supplist1)

print(supplist1[0][0])

product_detials_count = Counter(product_detials)

# print(product_detials_count)

prodlist = sorted(product_detials_count.items(),key = lambda x:x[1],reverse=True)

# print(prodlist)

print(prodlist[0][0])

customer_dict = Counter(customer)

# print(customer_dict)

customerlist = sorted(customer_dict.items(),key = lambda x: x[1],reverse=True)
# print(customerlist)
print(customerlist[0][0])


genderdict = Counter(gender)
# print(genderdict)

counter_list = sorted(genderdict.items(),key = lambda x: x[1],reverse = True)
print("No of females: ",counter_list[1][1])
