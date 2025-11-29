# NUMPY ARRAY OPERATION
import numpy as np

a = np.array([1, 2, 3])
print(a + 2)

# LIST COMPREHENSION OPERATION
lst = [1, 2, 3]
new = [x + 2 for x in lst]
print(new)


# Python program using numpy

# Creating a one-dimensional array
arr1 = np.array([10, 20, 30, 40])
print("One-dimensional Array:")
print(arr1)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Data Type:", arr1.dtype)

print()

# Creating a two-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Two-dimensional Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)


---

✅ Expected Output

[3 4 5]
[3, 4, 5]

One-dimensional Array:
[10 20 30 40]
Shape: (4,)
Dimensions: 1
Data Type: int64

Two-dimensional Array:
[[1 2 3]
 [4 5 6]]
Shape: (2, 3)
Dimensions: 2
Data Type: int64