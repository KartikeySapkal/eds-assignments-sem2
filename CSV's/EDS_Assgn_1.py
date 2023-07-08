import csv
from statistics import mean
import numpy as np

file=open("CSV's/stud_info.csv",'r')
info_dataset=[]
while True:
    data=file.readline()
    if data:
        info_dataset.append(data.replace("\n", "").split(','))        
    else:
        break


RollNo=[]
Name=[]
Gender=[]
DOB=[]

for row in info_dataset[1:]:
    RollNo.append(row[0])
    Name.append(row[1])
    Gender.append(row[2])
    DOB.append(row[3])



file=open("CSV's/student_marks.csv",'r')
marks_dataset=[]
while True:
    data=file.readline()
    if data:
        marks_dataset.append(data.replace("\n", "").split(','))        
    else:
        break


Maths=[]
Physics=[]
Chemistry=[]
Total=[]
Percentage=[]

for row in marks_dataset[1:]:
    Maths.append(row[1])
    Physics.append(row[2])
    Chemistry.append(row[3])
    Total.append(row[4])
    Percentage.append(row[5])


file=open("CSV's/stud_placement.csv",'r')
placement_dataset=[]
while True:
    data=file.readline()
    if data:
        placement_dataset.append(data.replace("\n", "").split(','))        
    else:
        break


Company=[]
JobRole=[]
Package=[]

for row in placement_dataset[1:]:
    Company.append(row[1])
    JobRole.append(row[2])
    Package.append(row[3])


studentdata=[]
studentdata.append(RollNo)
studentdata.append(Name)
studentdata.append(Gender)
studentdata.append(DOB)
studentdata.append(Maths)
studentdata.append(Physics)
studentdata.append(Chemistry)
studentdata.append(Total)
studentdata.append(Percentage)
studentdata.append(Company)
studentdata.append(JobRole)
studentdata.append(Package)
print("\n\nStudentdata\n\n")
print(studentdata)

fw=open("CSV's/StudentDetails.csv","w")

data_to_write=[]
for i in range(len(studentdata[0])):# 10 rows
    row=list()
    for j in range(len(studentdata)):#12 col
        data=studentdata[j][i]
        row.append(data)
    row.append('\n')
    data_to_write.append(",".join(row))
print("\n\n\n\nPrinting Data to write")
print(data_to_write,end= "\n\n\n")

fw.writelines(data_to_write)

print("\n\n\n")
print(fw)
fw.close()

f1 = open("CSV's/StudentDetails.csv","r")

print("\n\n\n\nkkkkkkkkkkkk")
print()
d8 = list(csv.reader(f1))
print(d8)

for i in range(len(d8)): 
    del d8[i][12]


#peforming statistical operations on list

# printing average of the all the packages
pkg=[]
sum = 0
for i in range(len(d8)): 
    sum  = sum + float(d8[i][11])
    pkg.append(float(d8[i][11]))


avg = sum/len(d8)

print("\n")
print("Sum of packages: ",sum)
print("Average packages of students: ",avg) 
print("Minimum Package Offered: ",min(pkg))
print("Maximum Package Offered: ",max(pkg))

# performing statistical analysis on marks

print("\n\nMaximum percentage gained by students: ",max(Percentage))
print("Minimum percentage gained by students: ",min(Percentage))

per = []
for i in range(len(d8)): 
    per.append(float(Percentage[i]))

print("Average percentage of students: ",mean(per))    

print("\n")

print("Total No. of Companies visited: ",len(Company))


pakage = [ ]

for i in range(len(d8)): 
    pakage.append(float(d8[i][11]))


print(pakage)
a= np.array(pakage)
print(a)

print(np.average(a))



