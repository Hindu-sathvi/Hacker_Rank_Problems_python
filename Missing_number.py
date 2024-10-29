#https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    count_arr={}
    count_brr={}
    for i in arr:
        if i in count_arr:
            count_arr[i]+=1
        else:
            count_arr[i]=1
    
    for j in brr:
        if j in count_brr:
            count_brr[j]+=1
        else:
            count_brr[j]=1
    missing=[]
    for num in count_brr:
        if count_brr[num] != count_arr.get(num, 0):
            missing.append(num)
    return sorted(missing)
   
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
