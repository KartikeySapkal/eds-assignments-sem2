import numpy as np

a = np.loadtxt("Numpy/testmarks1.csv", delimiter=",", dtype=float, skiprows=1)
print("a=\n",a)
b = np.loadtxt("Numpy/testmarks2.csv", delimiter=",", dtype=float, skiprows=1)
print("b=\n",b)

# matrix operations

print("Transpose of Matrix a is: \n", a.T)
print("\nTranspose of Matrix b is: \n", b.T)
print("a*b is: \n",a*b)
print("\nTrace of a:\n", a.trace())
print("\nTrace of b:\n", b.trace())
print("\nFlatten a: ", a.flatten())
print("\nFlatten b: ", b.flatten())

# Horizontal stacking
print("Horizontal Stacking")
print(np.hstack((a, b)), end="\n\n")

# Vertical stacking
print("Vertical Stacking")
print(np.vstack((a, b)), end="\n\n")

# Custom sequence generation
print("Generating Custom Sequences:\n")
print(np.arange(0, 10))
print(np.arange(0, 105, 5))

# Arithmetic and Mathematical Operations

print("Adding a and b:\n", np.add(a, b))
print("Subtracting a and b:\n", np.subtract(a, b))
print("Multiplying a nd b :\n", np.multiply(a, b))
print("Dividing a nd b :\n", np.divide(a, b))
print("Mod of a and b:\n", np.mod(a, b))
print("Remainder of a and b:\n", np.remainder(a, b))

# Statistical Operations

print("Mean of a: ", np.mean(a))
print("Mean of b: ", np.mean(b))

print("Variance of a: ", np.var(a))
print("Variance of b: ", np.var(b))

print("Standard Deviation of a: ", np.std(a))
print("Standard Deviation of b: ", np.std(b))

print("Sum of all elements in a: ", np.sum(a))
print("Sum of all elements in b: ", np.sum(b))


# stacking and sorting

print("Broadcasting:\n", a+5)

print("Data Stacking:\n", np.stack((a, b), axis=2))

print("Sorting a: \n", np.sort(a))
print("Sorting b: \n", np.sort(b))

print("Counting elements in a: ", np.count_nonzero(a))
print("Counting elements in b: ", np.count_nonzero(b))

print("Counting using elements less than 50 in a: ", np.count_nonzero(a > 4))
print("Counting using elements less than 10 in b: ", np.count_nonzero(b > 50))


# view and copy
print("\n\nView Method\n")

v = a.view()

v[:] = 0

print("a=\n", a)
print("v=\n", v)

print("Array created using view method is just shallow copy of original array\nSO changes made is original array reflects in view copy or vice versa")

print("\n\ncopy method: \n")

c = b.copy()

c[:] = 0

print("b=\n", b)
print("c=\n", c)

print("Both b and c has showed different o/p cz they are different arrays!")

#Bitwise operations

a=15
b=20

print("Binary of a: ",bin(a))
print("Binary of b:",bin(b))

print("Bitwise a and b: ",np.bitwise_and(a,b))
print("Bitwise a or b: ",np.bitwise_or(a,b))
print("Bitwise a xor b: ",np.bitwise_xor(a,b))
