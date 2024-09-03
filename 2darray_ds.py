#https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = -float('inf')

    # Loop through the 2D array and calculate the hourglass sums
    for i in range(4):  # 4 because the hourglass spans 3 rows
        for j in range(4):  # 4 because the hourglass spans 3 columns
            # Calculate the sum of the current hourglass
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_sum = top + middle + bottom
            
            # Update max_sum if the current hourglass_sum is greater
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()