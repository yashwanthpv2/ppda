import numpy as np
array = np.random.randint(1, 21, (3, 3))
print("Original array:")
print(array)
mean_value = np.mean(array)
print(f"Mean of the array: {mean_value}")
array[array < 10] = 0
print("Modified array:")
print(array)
