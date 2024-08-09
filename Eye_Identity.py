#https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
#eye-and-identity
#code:
import numpy as np
np.set_printoptions(legacy='1.13')  # Ensure alignment with expected output formatting
N, M = map(int, input().split())
result = np.eye(N, M)
print(result)
