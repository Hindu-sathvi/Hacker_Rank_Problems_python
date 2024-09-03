#https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        # Print the spaces followed by the hash symbols
        print(' ' * (n - i) + '#' * i)



if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
