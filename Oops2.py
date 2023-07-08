class Employee: 
    def __init__(self,name,occupation,networth=100,age=35):
        print("Constructor Evoked")
        self.Name=name
        self.Occupation=occupation
        self.NetWorth = networth
        self.Age= age
       

    Name="Kartik"
    Occupation="Technical Lead"
    NetWorth=50000000
    Age=30
    
    def show(self): 
        print(f"Name: {self.Name}\nOccupation: {self.Occupation}\nNetWorth: {self.NetWorth}\nAge: {self.Age}")

emp1=Employee("Kartik", "Technical Lead")
emp1.show()
    