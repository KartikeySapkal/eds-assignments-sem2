import csv

f1 = open("CSV's/stud_info.csv","r")
f2 = open("CSV's/stud_placement.csv","r")
f3 = open("CSV's/student_marks.csv","r")

rollno = [ ]
name = [ ]
gender = [ ]
dob = [ ]
company = [ ]
Jobrole = [ ]
package = [ ]

while True: 
    data = f1.readline()
    if not data: 
        break;
    # print(data)
    data = data.replace("\n","")
    # print(data)
    temp = data.split(",")
    print(temp)
    rollno.append(temp[0])
    name.append(temp[1])
    gender.append(temp[2])
    dob.append(temp[3])
f1.close()


print(rollno)
print(name)
print(gender)
print(dob)

while True: 
    data = f2.readline()
    if not data: 
        break;
    data = data.replace("\n","")
    temp1 = data.split(",")
    print(temp1)
    company.append(temp1[1])
    Jobrole.append(temp1[2])
    package.append(temp1[3])

f2.close()

print(company)
print(Jobrole)
print(package)

maths = [ ]
physics = [ ]
chemistry = [ ]
total =  [ ]
percentage = [ ]



while(True): 
    data  = f3.readline()
    if not data: 
        break;
    data  = data.replace("\n","")
    temp2 = data.split(",")
    print(temp2)
    maths.append(temp2[1])
    physics.append(temp2[2])
    chemistry.append(temp2[3])
    total.append(temp2[4])
    percentage.append(temp2[5])

f3.close()

print(maths)
print(physics)
print(chemistry)
print(total)
print(percentage)

studentdata=[]
studentdata.append(rollno)
studentdata.append(name)
studentdata.append(gender)
studentdata.append(dob)
studentdata.append(maths)
studentdata.append(physics)
studentdata.append(chemistry)
studentdata.append(total)
studentdata.append(percentage)
studentdata.append(company)
studentdata.append(Jobrole)
studentdata.append(package)


print(studentdata)

fw= open("CSV's/studentdata.csv","w")

data_to_write = [ ]

for i in range(len(studentdata[0])): 
    row = list()
    for j in range(studentdata):  # type: ignore
        data = studentdata[j][i]
        row.append(data)
    row.append("\n")
    data_to_write.append(",".join(row))
print(data_to_write) 

fw.writelines(data_to_write)

fw.close()

