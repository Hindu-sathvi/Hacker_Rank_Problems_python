#https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
#polynomials
#code:
import numpy as np
coefficients = list(map(float, input().split()))
x = float(input())
result = np.polyval(coefficients, x)
print(result)
"""The numpy.polyval function is used to evaluate a polynomial at a given point or at multiple points.
This function takes two primary arguments:
The coefficients of the polynomial, which are provided as a sequence (list, tuple, or NumPy array).
The value(s) at which to evaluate the polynomial, which can be a single number or a sequence of numbers."""
