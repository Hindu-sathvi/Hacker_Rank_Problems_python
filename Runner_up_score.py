#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
#find-second-maximum-number-in-a-list 
#finding runner_up score
#code
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))  
    unique_scores.sort(reverse=True)
    print(unique_scores[1])
"""first we take the input for an array and remove the duplicated values and sort them in an order.as we want runner_up score we get it from the position 1 of sorted array"""
