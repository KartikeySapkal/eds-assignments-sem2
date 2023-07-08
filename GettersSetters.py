class Myclass: 
    def __init__(self, value): 
        self.Value= value
    
    def show(self): 
        print(f"Value is: {self.Value}")
@property
def ten_value(self): 
    return 10*self.Value 

@ten_value.setter
def ten_value(self,newValue): 
   self.Value=newValue*100


obj=Myclass(10)
obj.ten_value= 67
print(obj.ten_value)
obj.show()