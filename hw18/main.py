import numpy as np


arr = np.arange(10)

print("Original array:")
print(arr)


new_arr = arr.copy()
new_arr[new_arr % 2 == 1] = -1

print("\nArray after replacing odd numbers:")
print(new_arr)


arr_2d = arr.reshape(2, 5)

print("\n2D array:")
print(arr_2d)


even_sum = np.sum(arr[arr % 2 == 0])

print("\nSum of even numbers:")
print(even_sum)