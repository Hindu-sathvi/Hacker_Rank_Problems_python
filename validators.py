#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
#string-validators
#code
if __name__ == '__main__':
    s = input().strip()
    # Check for alphanumeric characters
    print(any(char.isalnum() for char in s))
    # Check for alphabetical characters
    print(any(char.isalpha() for char in s))
    # Check for digits
    print(any(char.isdigit() for char in s))
    # Check for lowercase characters
    print(any(char.islower() for char in s))
    # Check for uppercase characters
    print(any(char.isupper() for char in s))
"""STRING VALIDATORS:Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
str.isalnum():This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
str.isalpha():This method checks if all the characters of a string are alphabetical (a-z and A-Z).
str.isdigit():This method checks if all the characters of a string are digits (0-9).
str.islower():This method checks if all the characters of a string are lowercase characters (a-z).
str.isupper():This method checks if all the characters of a string are uppercase characters (A-Z)."""
