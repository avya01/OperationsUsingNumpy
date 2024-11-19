import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original array: ", array)
array[array%2 != 0] = -1
print("All odd numbers replaced with -1: ", array)