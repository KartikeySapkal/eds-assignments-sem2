import numpy as np

a = np.array([[1,2,3],[5,6,7],[8,9,0]])
print(a,end="\n\n")
b = np.array([[8,9,0],[5,6,7],[1,2,3]])
print(b,end="\n\n")
# print(a%b)
# print(a*b)
print(np.hstack((a,b)),end="\n\n")
print(np.vstack((a,b)),end="\n\n")

print(a+b,end="\n\n")

print(a-b,end="\n\n")

d=np.arange(0,100,10)
print(d)
# [ 0 10 20 30 40 50 60 70 80 90]

# d = np.reshape(2,5)
print(d.reshape(5,2))
# [[ 0 10]
#  [20 30]
#  [40 50]
#  [60 70]
#  [80 90]]

e = np.linspace(10,100,10).reshape(2,5)
print(e)
# [[ 10.  20.  30.  40.  50.]
#  [ 60.  70.  80.  90. 100.]]

ide = np.identity(5)
print(ide)

print(np.eye(6))

d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)
e = np.random.random((2, 2))
print ("\nA random array:\n", e)


