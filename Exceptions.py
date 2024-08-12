#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
#exceptions
#code
t = int(input())
for _ in range(t):
    a, b = input().split()
    
    try:
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

"""Exceptions in Python are errors detected during execution that disrupt the normal flow of a program.
When an error occurs, Python generates an exception, which can be handled to prevent the program from crashing.
1.ZeroDivisionError:
Raised when an attempt is made to divide by zero.
2.ValueError:
Raised when a built-in operation or function receives an argument of the right type but with an inappropriate value.
Handling Exceptions:
You can handle exceptions using try and except blocks"""