#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
#python-tuples
#code
n = int(input())
t = tuple(map(int, input().split()))
result = hash(t)
print(result)
"""Check the version of the python before printing the result.
The difference in hash values could be due to the version of Python you are using. 
Python's hash() function may produce different values on different runs or different versions of Python.
The hash values across different runs and environments."""