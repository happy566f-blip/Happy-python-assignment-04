(A) NumPy: Key Features
NumPy (Numerical Python) is a powerful Python library used mainly for scientific computing, data analysis, and numerical operations.
⭐ 1. Fast Performance
NumPy is much faster than Python lists because it is written in C.
Uses vectorized operations (performing operation on whole arrays at once).
⭐ 2. Multi-Dimensional Arrays
Provides the ndarray object for creating 1D, 2D, and multi-dimensional arrays.
Example:
Copy code
Python
import numpy as np
a = np.array([[1, 2], [3, 4]])
⭐ 3. Memory Efficient
Stores data in continuous memory, using less space than Python lists.
⭐ 4. Mathematical Functions
Has many built-in functions: sqrt, sum, mean, sin, log, etc.
Example:
Copy code
Python
np.mean([1, 2, 3, 4])
⭐ 5. Vectorization
Eliminates the need for loops.
Example:
Copy code



(B) import numpy as np

# Creating a 1D array
arr1 = np.array([10, 20, 30, 40])

# Creating a 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

# Displaying details of 1D array
print("1D Array:", arr1)
print("Shape of 1D Array:", arr1.shape)        # shape → (4,)
print("Dimensions of 1D Array:", arr1.ndim)   # ndim → 1 dimension
print("Data Type of 1D Array:", arr1.dtype)   # dtype → int32/int64

print("\n-------------------------------------\n")

# Displaying details of 2D array
print("2D Array:\n", arr2)
print("Shape of 2D Array:", arr2.shape)       # shape → (2, 3)
print("Dimensions of 2D Array:", arr2.ndim)   # ndim → 2 dimensions
print("Data Type of 2D Array:", arr2.dtype)   # dtype → int32/int64
✅ Explanation of Output
✔ 1D Array (arr1)
Data: [10, 20, 30, 40]
Shape → (4,)
Means it has 4 elements in one row.
Dimensions (ndim) → 1
It is a one-dimensional array.
Data Type → int32 or int64
Depends on system.
✔ 2D Array (arr2)
Data:


1 2 3
4 5 6
Shape → (2, 3)
Means 2 rows and 3 columns.
Dimensions (ndim) → 2
It is a two-dimensional array.
Data Type → int32 or int64
🟦 Short Notes (for assignment answer)
shape → tells how many rows and columns
ndim → tells number of dimensions (1D, 2D, 3D, etc.)
dtype → tells the type of data stored (int, float, etc.)

Python
a = np.array([1, 2, 3])
b = a * 2   # No loop required
