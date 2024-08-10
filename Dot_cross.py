#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
#dot-and-cross
#code:
import numpy as np
n = int(input())
A = np.array([list(map(int, input().split())) for _ in range(n)])
B = np.array([list(map(int, input().split())) for _ in range(n)])
result = np.dot(A, B)
print(result)
