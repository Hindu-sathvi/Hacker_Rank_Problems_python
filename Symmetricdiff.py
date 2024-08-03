#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference(a, b):
    sym_diff = a.symmetric_difference(b)
    return sorted(sym_diff)

if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    
    result = symmetric_difference(a, b)
    for num in result:
        print(num)
