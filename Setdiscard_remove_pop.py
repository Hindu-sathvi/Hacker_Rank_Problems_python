#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
#set-discard-remove-pop
#code
n = int(input())
s = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    command = input().split()
    operation = command[0]
    
    if operation == "pop":
        s.pop()
    elif operation == "remove":
        value = int(command[1])
        s.remove(value)
    elif operation == "discard":
        value = int(command[1])
        s.discard(value)

# Print the sum of the remaining elements in the set
print(sum(s))
#.pop():This operation removes and return an arbitrary element from the set.If there are no elements to remove, it raises a KeyError.
#.discard(x):This operation also removes element  from the set.If element  does not exist, it does not raise a KeyError.
#The .discard(x) operation returns None.
#.remove(x):This operation removes element  from the set.If element  does not exist, it raises a KeyError.The .remove(x) operation returns None.