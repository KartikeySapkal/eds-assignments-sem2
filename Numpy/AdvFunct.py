def adduni(*args): 
    sum = 0
    for i in range(len(args)): 
        sum+=args[i]
    return sum


def f(**args): 
    for x in args: 
        print(args,args[x])


print(adduni(5,4,3,2,1))
f(a=3,b=5,c="aaa",d=3.8)
