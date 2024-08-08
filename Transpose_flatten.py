import numpy as np
n, m = map(int, input().split())
matrix = np.array([input().split() for _ in range(n)], int)
transpose_matrix = np.transpose(matrix)
flattened_matrix = matrix.flatten()
print(transpose_matrix)
print(flattened_matrix)
