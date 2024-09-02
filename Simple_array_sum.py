#https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
#code:
#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'simpleArraySum' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.


def simpleArraySum(ar):
    # Write your code here
    total_sum = 0
    
    # Iterate through each element in the array
    for num in ar:
        # Add each element to the total sum
        total_sum += num
    
    # Return the final sum
    return total_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
