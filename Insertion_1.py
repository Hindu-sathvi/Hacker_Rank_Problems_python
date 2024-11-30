#https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    index = n - 1
    while index > 0 and arr[index - 1] > val:
        arr[index] = arr[index - 1]
        print(*arr)  
        index -= 1
 
    arr[index] = val
    print(*arr) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
