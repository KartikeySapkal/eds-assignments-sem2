# program for converting given salary into dollers

def SnoopDog(salary): 
    dollers  = salary/81.80
    return dollers

salary = int(input("Enter Your Salary: "))
print(SnoopDog(salary))