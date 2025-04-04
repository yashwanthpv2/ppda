import numpy as np
matrix_a = np.random.randint(1, 11, size=(3, 3))
matrix_b = np.random.randint(1, 11, size=(3, 3))
subtraction_result = matrix_a - matrix_b
division_result = np.divide(matrix_a, matrix_b, where=matrix_b != 0)
print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nSubtraction result (A - B):")
print(subtraction_result)

print("\nElement-wise division result (A / B):")
print(division_result)
