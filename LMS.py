class Bank:
    def Verification(self): 
        print("Create Password: ")
        PassWord= (input("Enter PassWord: "))
        print("Verify Password: ")
        PassWord2= (input("Enter Again: "))



print("Welcome to Bank Management system\n")
print("Press 1 to Create Acc")
print("Press 2 to Login")
print("Press 3 to Check Balance")
print("Press 4 to Deposite Money")
print("Press 5 to Withdraw Money")

m=int(input("\nEnter Your Choice: "))
emp1=Verification()

if m==1: 
    print("Enter Your Name: ",end=" ")
    name=input()
    print("ENter Mob no: ",end=" ")
    mobNo= int(input())
    Verification()

    if(PassWord==PassWord2): 
        print("Account Successfully Created")
    else: 
        print("Something Went Wrong!!")    
