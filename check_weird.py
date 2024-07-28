#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
#if-else
#code
def check_weird(n):
    if( n % 2 != 0):
        print("Weird")
    elif ((n % 2 == 0) and (2 <= n <= 5)):
        print("Not Weird")
    elif ((n % 2 == 0) and (6 <= n <= 20)):
        print("Weird")
    elif ((n % 2 == 0 )and (n > 20)):
        print("Not Weird")

# Sample Input
n = int(input().strip())
check_weird(n)
