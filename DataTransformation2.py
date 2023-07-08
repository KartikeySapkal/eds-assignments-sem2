from datetime import date
from datetime import datetime
import csv

def CalAge(bdate): 
        today = date.today()
        age  = today.year - bdate.year - ((today.month,today.day)<(bdate.month,bdate.day))
        return age


f1 = open("sal.csv","r")

emp = list(csv.reader(f1))
bdate  = [ ]
age = [ ]
dollars = [ ]

for i in range (len(emp)):
        print(emp[i][5])
        bdate.append(datetime.strptime(emp[i][5],'%m/%d/%Y').date()) 
        

for i in range(len(emp)): 
        age.append(CalAge(bdate[i]))
        dollars.append(float(emp[i][4])/81.80)

print(dollars)
print("Age:",age)

f1.close()