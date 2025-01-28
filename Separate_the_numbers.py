#https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true
#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    # Try all possible starting numbers
    for length in range(1, len(s)//2 + 1):
        first_num = int(s[:length])  
        temp = str(first_num) 
        next_num = first_num 

        while len(temp) < len(s):
            next_num += 1
            temp += str(next_num)

        if temp == s:
            print(f"YES {first_num}")
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
