#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period=s[-2:]
    hours=int(s[:2])
    min_sec=s[2:-2]
    if period=='AM':
        if hours==12:
            hours=0
    else:
        if hours<12:
            hours+=12
    return f"{hours:02d}{min_sec}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
