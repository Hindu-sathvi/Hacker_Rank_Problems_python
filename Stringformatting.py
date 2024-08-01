#https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
#string-formatting
#code
def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    
    # Iterate through each number from 1 to 'number'
    for i in range(1, number + 1):
        # Print each value with appropriate formatting
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")
  

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

""" width = len(bin(number)) - 2:width is used to just have the right spaceing among the numbers printed.AS binary numbers ocupy more spaces than octal or hexadecimal numbers.
rjust:The rjust method in Python is used to right-justify a string in a field of a specified width. 
It pads the string with spaces (or a specified fill character) on the left to ensure that the string reaches the desired width.
If the string is already at least as wide as the specified width, it will be returned unchanged."""
