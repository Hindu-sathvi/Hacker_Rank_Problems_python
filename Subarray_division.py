#https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
#code:
import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    # Loop through the chocolate bar and check each segment
    for i in range(len(s) - m + 1):
        # If the sum of the current segment equals d, increment the count
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Number of squares in the chocolate bar

    s = list(map(int, input().rstrip().split()))  # Numbers on the chocolate squares

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])  # Ron's birth day (sum of the segment)
    m = int(first_multiple_input[1])  # Ron's birth month (length of the segment)

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
