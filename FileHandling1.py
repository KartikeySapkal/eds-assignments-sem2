import csv
def top5Emp(d3): 
    d3.sort(key = lambda x: int(x[4]),reverse  = True)
    print("Sorted Data: ",d3)
    for i in range(len(d3)):
        print(f"Top {i+1} Employee is: {d3[i][1]}")

    cw = csv.writer(f3)
    cw.writerows(d3)



f1 = open("emp.csv","r")
f2 = open("sal.csv","r")
f3 = open("emp-sal","w")
# here reader method is used to access the data from this csv file
# reader method can be access using csv.reader method

d1 = list(csv.reader(f1,delimiter=",")) 
d2 = list(csv.reader(f2,delimiter=","))
x = (len(d1)) #5
y = (len(d2)) #5
d3 =[ ]
for i in range(x): 
    d3.append(d1[i] + d2[i])

top5Emp(d3)    






f1.close()
f2.close()
f3.close()
