l=[]
i=0;sum=0
for i in range(5): 
    print("Enter Marks of subject : ",i+1)
    a=int(input())
    l.append(a)

for i in range(len(l)): 
    sum=sum+l[i]

print("Sum of Marks: ",sum)  
avgMarks = sum/len(l)

print("Avg Marks: ",avgMarks)