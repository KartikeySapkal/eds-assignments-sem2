import datetime

print(datetime.datetime.now())
i=3
j=5
k=7
if i<j: 
    if j<k: 
        i=j
    else: 
        j=k 
else:
    if k>j: 
        i=k
    else: 
        j=k

print(i,j,k)


