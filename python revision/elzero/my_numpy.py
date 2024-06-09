"""
numpy allows you to make num array and it stands for numircal python
- homogeneous: must contain the same object type (numpy arrays)
- heterogeneous: can contain different type of objects (python lists)

- the np.array is much faster than the normal lists as showed below
- the np array is much smaller in size than the normal list
"""
import numpy as np
import time
# to know the size of data
import sys

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(type(my_list))
print(type(my_array))

a = np.array([1, 2, 3, 4, 5])# 1 dimentional array
b = np.array([[1,2], [3,4]])# 2 dimentional array
c = np.array(10)# 0 dimentional array

print(a)
print(b[-1,0]) # b[-1][0]
print(c)

print(a.ndim)# to know the number of dimentions in this arr

my_custom_dimentions = np.array([1,2], ndmin=4)# make it 4 dimetions by defualt


print('-'*40)

elements = 1500000

list1 = range(elements)
list2 = range(elements)

array1 = np.arange(elements)#like the range kda
array2 = np.arange(elements)#like the range kda

list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(list1, list2)]
print(f"list time: {time.time() - list_start}")

array_start = time.time()
array_result = array1 + array2
print(f"array time: {time.time() - array_start}")

print(sys.getsizeof(array1))


print('-'*40)

print(array1[:20])
print(b)

