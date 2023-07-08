# def factorial(n):
# 	if n == 0 or n == 1 : #Base condition which doesn’t call the function any further
# 		return n
# 	else:
# 		return n*factorial(n-1)

# a= int(input("Enter No: "))
# print(factorial(a))


# fibonacci series

# 0,1,1,2,3,5,8,13,21....

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(0,n,1):
#         if i==0:
#             print(a)
#         elif i==1:
#             print(b)
#         else:
#             NextNo=a+b
#             print(NextNo)
#             a=b
#             b=NextNo

# n= int(input("Enter Limit For Fibonacci: "))
# fibonacci(n)

# Armstrong number: a number which is equal to sum of cube of its digits
# ex: 371  as 3**3 = 27 and 7**3 = 343 and 1**3  = 1
# so 27+343+1 =

# def armstrong(a):
#     digit=0
#     sum=0
#     num=a
#     while(a>0):
#         digit = a%10
#         sum = sum+ digit**3
#         a=a//10
#     if(sum==num):
#         print("Armstrong")
#     else:
#         print("Not an Armstrong")


# ch = int(input("Enter Number: "))
# armstrong(ch)


# note:
# 10/3 = 3.33 float
# but 10//3 = 3 int


