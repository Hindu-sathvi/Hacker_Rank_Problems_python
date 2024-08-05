#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT'
from itertools import permutations
input_data = input().split()
S = input_data[0]
k = int(input_data[1])
perms = permutations(S, k)
for perm in sorted(perms):
    print(''.join(perm))
