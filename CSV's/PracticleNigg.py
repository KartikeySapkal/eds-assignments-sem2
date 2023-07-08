import csv
from collections import Counter

f1 = open("CSV's/company.csv","r")

Desig = [ ]
salaryrs = [ ]

while(True):
    data = f1.readline()
    if not data: 
        break;
    data = data.replace("\n","")
    temp = data.split(",")
    # print(temp)
    Desig.append(temp[3])
    salaryrs.append(temp[4])
    

del salaryrs[0]

Salarylist = [ ]
for i in range(len(salaryrs)): 
    Salarylist.append(int(salaryrs[i]))
JObSal = { }


for i in range(len(salaryrs)): 
    JObSal.update({Desig[i]:Salarylist[i]})

print(JObSal) 

JobList = sorted(JObSal.items(),key = lambda x : x[1],reverse =True)

print(JobList)

print(f"\n\nHighest Paying Job {JobList[0][0]} their salary is: {JobList[0][1]}")



