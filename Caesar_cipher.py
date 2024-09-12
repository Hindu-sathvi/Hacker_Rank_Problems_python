#https://hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true
#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    encrypt = []
    k = k % 26 
    for char in s:
        if char.islower():
            # Shift lowercase characters
            current_position = ord(char) - ord('a')
            shifted_position = (current_position + k) % 26
            shifted_char = chr(shifted_position + ord('a'))
            encrypt.append(shifted_char)
            
        elif char.isupper():
            # Shift uppercase characters
            current_position = ord(char) - ord('A')
            shifted_position = (current_position + k) % 26
            shifted_char = chr(shifted_position + ord('A'))
            encrypt.append(shifted_char)
            
        else:
            # Non-alphabetic characters remain the same
            encrypt.append(char)
    
    return ''.join(encrypt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
