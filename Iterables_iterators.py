#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
#iterables-and-iterators
#code:
from itertools import combinations
n = int(input())
elements = input().split()
k = int(input())
total= list(combinations(range(n), k))
favorable = sum(1 for combo in total if any(elements[i] == 'a' for i in combo))
probability = favorable / len(total)
print(f"{probability:.4f}")
