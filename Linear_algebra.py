#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
#linear-algebra
#code:
import numpy as np
n = int(input())
matrix = np.array([list(map(float, input().split())) for _ in range(n)])
determinant = np.linalg.det(matrix)
print(round(determinant, 2))
"""The numpy.linalg.det function in Python is used to compute the determinant of a square matrix. 
The determinant is a scalar value that can be computed from the elements of a square matrix.
It has many important properties in linear algebra, including determining whether a matrix is invertible.

"""
