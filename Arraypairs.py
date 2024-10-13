#https://www.hackerrank.com/challenges/array-pairs/problem?isFullScreen=true
#code
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    
    
    count = {}
    total_pairs = 0
    
   
    for num in arr:
        if num in count:
   
            total_pairs += count[num]
           
            count[num] += 1
        else:
            count[num] = 1
            
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
