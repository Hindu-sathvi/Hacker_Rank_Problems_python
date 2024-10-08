#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first= 0
    second = 0
    
    n = len(arr)
    
    for i in range(n):
        first += arr[i][i]
        second += arr[i][n - i - 1]
    
    return abs(first - second)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
