from datetime import date

today = date.today()


def calage(bdate): 
    age  = today.year - bdate.year - ((today.month,today.day)<(bdate.month,bdate.day))
    return age

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth Month: "))
day = int(input("Enter your birth day: "))

print("Your Age is : ",calage(date(year,month,day)))
