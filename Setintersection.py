#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
#intersection-operation
#code
n=int(input())
english=set(map(int, input().split()))
b=int(input())
french=set(map(int, input().split()))
result=english.intersection(french)
print(len(result))