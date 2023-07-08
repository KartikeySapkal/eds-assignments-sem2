# Numpy is a librabry in python. Which is ude to perform mathematical tasks
# its faster than lists and has less time complexity than loops
# it stores integers in less amount of memory with contiguos blocks
# it help to perform matrix operations and also useful for other mathematical tasks
# numpy also integrates with other libraries like pandas, matplotlib etc
# its a useful tool for machine learning


# now lets start

import numpy as np

a = np.array([1,2,3],dtype = "int16")
print(a) #[1 2 3]

b = np.array([[1,2,3],[4,5,6]], dtype = 'int32')
print(b) #[[1 2 3]
        #  [4 5 6]]

print(a.ndim) # 1
print(b.ndim) # 2

print(a.shape) #(3,)
print(b.shape) #(2, 3)

print(a.dtype) #int16
print(b.dtype) #int32

# default dtype is int64 with itemsize 8 bytes

print(a.itemsize) #2 bytes cz dtype is int16 as it has 16 bits i.e. 2 bytes
print(b.itemsize) #4 reason dtype is int32

print(a.nbytes) #6 #total memory bytes allocated for variable
print(b.nbytes) #24 #total memory bytes allocated for variable






