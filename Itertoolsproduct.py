#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
product = product(A, B)
print(' '.join(map(str,product)))