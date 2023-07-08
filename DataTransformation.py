from datetime import date

today = date.today()
print(today)



def CalAge(bdate): 
        age  = today.year - bdate.year - ((today.month,today.day)<(bdate.month,bdate.day))
        return age

year = int(input("Enter Your Birth Year: "))
month= int(input("Enter Your Birth Month: "))
day = int(input("Enter Your Birth Day: "))


print("Your Age is: ",CalAge(date(year,month,day)))









