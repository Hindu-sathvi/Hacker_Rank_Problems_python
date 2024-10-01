#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    
    # Initialize counters for positive, negative, and zero numbers
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    # Iterate through the array and count positives, negatives, and zeros
    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    # Calculate the ratios
    pos_ratio = pos_count / n
    neg_ratio = neg_count / n
    zero_ratio = zero_count / n
    
    # Print the ratios, each with 6 decimal places
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
