import numpy as np
# Operations on Numpy

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)    #[[ 1  2  3  4  5  6  7]
#             # [ 8  9 10 11 12 13 14]]

# print(a[1,5]) # 13
print(a[0,: ]) #[1 2 3 4 5 6 7]
print(a[:, 2]) #[ 3 10]
print(a[0, 1:-1:2]) #[2 4 6]

a[1,5] = 20

print(a) # [[ 1  2  3  4  5  6  7]
          # [ 8  9 10 11 12 20 14]]