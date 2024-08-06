#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
input_string, k = input().split()
k = int(k)
string = ''.join(sorted(input_string))
combinations = combinations_with_replacement(string, k)
for combo in combinations:
    print(''.join(combo))