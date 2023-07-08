import csv
def top_5_emp(d3):
    d3.sort(key = lambda x: int(x[4]),reverse=True)
    print("Sorted Data:",d3)
    
    print("\n\nTop1 Employee",d3[0][1])
    print("Top2 Employee",d3[1][1])
    print("Top1 Employee",d3[2][1])
    print("Top2 Employee",d3[3][1])
    print("Top2 Employee",d3[4][1])
    
f1 = open("emp.csv","r")
f2 = open("sal.csv","r")
f3 = open("emp_sal.csv","w")

d1=list(csv.reader(f1,delimiter=','))
d2=list(csv.reader(f2,delimiter=','))

print("\n\nFile1 Contents:",d1)
print("\n\nFile2 Contents:",d2)
d3 = []
for i in range(len(d1)):
    d3.append(d1[i] + d2[i])

print(d3)
cw = csv.writer(f3) 
cw.writerows(d3)

top_5_emp(d3)


f1.close()
f2.close()
f3.close()






