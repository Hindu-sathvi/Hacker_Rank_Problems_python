#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
#itertools-combinations
#code
from itertools import combinations
def print_combinations(s, k):
    s = ''.join(sorted(s))
    for i in range(1, k + 1):
        for combo in combinations(s, i):
            print(''.join(combo))
input_str = input().strip()
s, k = input_str.split()
k = int(k)
print_combinations(s, k)
