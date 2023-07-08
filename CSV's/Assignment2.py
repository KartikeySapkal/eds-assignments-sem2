import csv

f1 = open("CSV's/Sales.csv","r")

product_details = [ ]
supplier_details = { }
customer_details = [ ]
gender = { }

while(True): 
    data = f1.readline()
    if not data: 
        break;
    print(data)

    data = data.replace("\n","") 
    print(data)
    temp = data.split(",")  
    #print(temp) 

    product_details.append(temp[1])
    customer_details.append(temp[3])
    supplier_details.update({temp[0]:temp[2]})
    gender.update({temp[3]:temp[4]})
f1.close()

customer_details = tuple(customer_details)


print(product_details)
print(customer_details)
print(supplier_details)
print(gender)    


frequency  = { }
for item in product_details: 
    if item in frequency: 
        frequency[item] += 1
    else: 
        frequency[item]= 1

print("\n\n\n")        
print(frequency) 

marklist = sorted(frequency.items(),key = lambda x:x[1],reverse = True)
marklist = dict(marklist)
print(marklist)

frequency1  = { }
for item in supplier_details: 
    if item in frequency1: 
        frequency1[item] += 1
    else: 
        frequency1[item]= 1
print("\n\n")
print(frequency1)
    

