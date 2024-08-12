#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
n = int(input())
A = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    operation, k = input().split()
    k = int(k)
    other_set = set(map(int, input().split()))
    
    if operation == 'intersection_update':
        A.intersection_update(other_set)
    elif operation == 'update':
        A.update(other_set)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif operation == 'difference_update':
        A.difference_update(other_set)
print(sum(A))
"""Set mutations in Python refer to operations that modify the contents of a set. 
These mutations are applied directly to the set and affect its elements based on the operation performed.
1>.update() or |=:
Adds elements from an iterable (e.g., another set, list) to the set.
Syntax: set.update(iterable) or set |= iterable
2>.intersection_update() or &=:
Keeps only elements found in both the set and the iterable.
Syntax: set.intersection_update(iterable) or set &= iterable
3>.difference_update() or -=:
Removes elements found in the iterable from the set.
Syntax: set.difference_update(iterable) or set -= iterable
4>.symmetric_difference_update() or ^=:
Updates the set to keep only elements that are in either set, but not in both.
Syntax: set.symmetric_difference_update(iterable) or set ^= iterable"""