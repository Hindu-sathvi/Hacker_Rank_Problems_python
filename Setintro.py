#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
#introduction-to-sets
#code
def average(array):
    # your code goes here
     # Convert the list to a set to get distinct heights
    distinct_heights = set(arr)
    # Calculate the average of the distinct heights
    avg = sum(distinct_heights) / len(distinct_heights)
    # Return the average rounded to 3 decimal places
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)