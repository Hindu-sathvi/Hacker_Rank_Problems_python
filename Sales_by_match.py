#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    color_counts = {}
    for sock in ar:
        color_counts[sock] = color_counts.get(sock, 0) + 1
    pairs = 0
    for count in color_counts.values():
        pairs += count // 2

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
