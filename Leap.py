#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
#writing function for leap year
#code
def is_leap(year):
    # Initialize leap to False
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is also divisible by 100
        if year % 100 == 0:
            # Check if the year is also divisible by 400
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap


year = int(input())
print(is_leap(year))