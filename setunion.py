#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
#set-union
# Enter your code here. Read input from STDIN. Print output to STDOUT                         
n=int(input())
english = set(map(int, input().split())) 
b=int(input())
french = set(map(int, input().split())) 
result=english.union(french)
print(len(result))