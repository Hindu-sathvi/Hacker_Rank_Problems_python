#https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    last_seen = {}
    min_distance = float('inf')
    for i, value in enumerate(a):
        if value in last_seen:
            distance = i - last_seen[value]
            min_distance = min(min_distance, distance)
        last_seen[value] = i
    return min_distance if min_distance != float('inf') else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
