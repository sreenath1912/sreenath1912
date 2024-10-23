import numpy as np
from numpy.lib.format import dtype_to_descr
from numpy.ma.core import arange

# methods of arrays
## arange
print(np.arange(5, 10))  #np
print(np.arange(10))  #np

print(list(range(10)))  # core python

print(np.arange(5.5, 10.5))

## Zero, zero_like
print("printing xxxxx")
x = np.zeros((3, 2))
print(x)

print("yyyyyy")

y = np.zeros_like((4, 2), float)
print(y)

#random
a = np.random.rand(1, 10)
print(a)
a = np.random.randn(1, 10)
print(a)
a = np.random.randint(1, 10, size=(4, 2))
print(a)

#identity matrix
print(np.identity(4, dtype=int))

print(np.identity(4, dtype=float))

#transpose
a = np.random.randint(1, 10, size=(4, 2))
b = a.transpose()
print(b)
print('ssssssss')
#reshape
a = np.random.randint(1, 10, size=(4, 3))
print(a)

print("fffffff")
z = a.reshape(6, 2)
print(z)

n = np.arange(36).reshape((6, 2, 3))
print(n)

# indexing ane sliciing in arrays :
## 1d
arr = arange(12) ** 2
print(arr)
print(arr[3])

## 2d
a = np.arange(36).reshape((6, 6)) ** 2
print(a)
b = a[1][2]
print(b)
print(a[1, 4])
print(a[1:4, 1])  # 49,169,361
print(a[1, 2:5])  # 64,81,100
print("next ")
print(a[1:4, 1:3])
print("next ")
print(a[1::2, 2:5])
print("next ")
print(a[[1, 2, 4, 5], 1:4])
print("next ")
print(a[1:5, [1, 2, 3, 4]])
print("next ")
### split if array :
a = np.arange(36).reshape((6, 6)) ** 2
b = np.split(a, 6)
print(b)
print("split array in to 2 ")
a = np.arange(10)
b= np.split(a, 2)
print(b)
print("split array in to 3 ")
b= np.split(a, [2,5,7])
print(b)

## 2d,  split , axis
print("88888888888888888888888888888888888888888888888888888888888 ")
a = np.arange(16).reshape((4,4))
c= np.split(a, 2, axis=1)
print(c)

