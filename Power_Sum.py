#https://www.hackerrank.com/challenges/the-power-sum/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N,num=1):
    # Write your code here
    #num=1
    power = num ** N
    if power == X:
        return 1
    elif power > X:
        return 0
    else:
        return powerSum(X - power, N, num + 1) + powerSum(X, N, num + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
