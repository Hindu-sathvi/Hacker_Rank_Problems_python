#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOU
n=int(input())
english=set(map(int, input().split()))
b=int(input())
french=set(map(int, input().split()))
result=english.symmetric_difference(french)
print(len(result))