#https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
#code:
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)
    min_value = min(arr)
    max_value = max(arr)
    min_sum = total_sum - max_value
    max_sum = total_sum - min_value
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
