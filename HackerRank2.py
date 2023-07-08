




a = str(input())
num = [ ]

for i in range(len(a)): 
    try: 
        num.append(int(a[i]))
    except: 
        None    

if sum(num)>10: 
    print(15) 
elif sum(num)>4: 
    print(10) 
else: 
    print(5)              