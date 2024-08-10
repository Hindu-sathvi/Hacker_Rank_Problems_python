#https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
#inner-and-outer
#code:
import numpy as np
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
inner_product = np.inner(A, B)
print(inner_product)
outer_product = np.outer(A, B)
print(outer_product)
