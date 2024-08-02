#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
#capitalize
#code
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
        # Split the string into words to handle alphanumeric constraints
    words = s.split(' ')
    # Capitalize each word properly
    capitalized_words = [word.capitalize() if word.isalpha() else word for word in words]
    # Join the capitalized words back into a single string
    capitalized_name = ' '.join(capitalized_words)
    return capitalized_name


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

