#https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice_score = 0
    bob_score = 0
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    return [alice_score, bob_score]
a = [5, 6, 7]
b = [3, 6, 10]
print(compareTriplets(a, b))
a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a, b)) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()