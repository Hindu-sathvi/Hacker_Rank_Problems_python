#https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true
#code:
#Panagrams:A pangram is a string that contains every letter of the alphabet.
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    input= set(s)
    if alphabet_set.issubset(input):
        return "pangram"
    else:
        return "not pangram"
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
