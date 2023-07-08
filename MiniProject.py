import os
x= 'Hii'
while(True): 
    x= input("Enter What You want to speak : ")
    if(x=='q'): 
        command = f"say Ae Nikalh Lavdeh..!"
        os.system(command)
        break
    else: 
        command = f"say {x}"
        os.system(command)
