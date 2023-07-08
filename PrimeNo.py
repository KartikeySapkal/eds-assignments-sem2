a=int(input("Enter No: "))
for i in range(2,5):
    n=a%i
    if(n==0):
        flag= False
    else: 
        flag=True

if flag==True: 
    print("Prime..!")
else: 
    print("No is not Prime")            