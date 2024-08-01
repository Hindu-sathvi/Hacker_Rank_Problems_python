import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    capitalized_name = s.title()
    return capitalized_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
  """File functions:File functions in Python are used to interact with files—whether you're reading from or writing to them. 
  File Handling Modes:

'r' - Read (default mode)
'w' - Write (creates a new file or truncates an existing file)
'a' - Append (writes data to the end of the file)
'b' - Binary mode (e.g., 'rb' or 'wb')
'x' - Exclusive creation (raises an error if the file already exists."""
  
