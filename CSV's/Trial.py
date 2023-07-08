import csv

f1 = open("CSV's/stud_info.csv","r")
f2 = open("CSV's/stud_placement.csv","r")
f3 = open("CSV's/student_marks.csv","r")

d1 = list(csv.reader(f1))
d2 = list(csv.reader(f2))
d3 = list(csv.reader(f3))
print("Printing D1")
print(d1)

DOB = [ ]
name = [ ]

for i in range(len(d1)): 
    DOB.append(d1[i][3])
    name.append(d1[i][1])


 
studentdata = [ ]

studentdata.append(DOB)
studentdata.append(name)
print("\n\n\n")
print(studentdata)
    
