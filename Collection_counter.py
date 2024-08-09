#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
#collections-counter
#code:
from collections import Counter
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())
inventory = Counter(shoe_sizes)
total_earnings = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:  
        total_earnings += price
        inventory[size] -= 1  
print(total_earnings)
