#1.LCM of given numbers:
#using lcm function
import math
# Input for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = math.lcm(a, b)
print(f"LCM of {a} and {b} is {result}")
# Input for multiple numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = math.lcm(*numbers)
print(f"LCM of {numbers} is {result}")

#using numpy
import numpy as np
from functools import reduce
# For two numbers
a = 12
b = 18
result = np.lcm(a, b)
print(f"LCM of {a} and {b} is {result}")
# For multiple numbers
numbers = np.array([12, 18, 24])
result = reduce(np.lcm, numbers)
print(f"LCM of {numbers} is {result}")


#2.HCF of a number
import math
from functools import reduce
# Function to calculate the GCD of multiple numbers
def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)
# Input for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = math.gcd(a, b)
print(f"HCF of {a} and {b} is {result}")
# Input for multiple numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = gcd_multiple(numbers)
print(f"HCF of {numbers} is {result}")

#3.Reverse of a string
#usig slicing operation
# Taking input from the user
s = input("Enter a string: ")
reverse = s[::-1]
print(f"Reversed string: {reverse}")

#without slicing operation
s= input("Enter a string: ")
reverse = ''
for char in s:
    reverse = char + reverse
print(f"Reversed string: {reverse}")


#4.Prime number 
n=int(input("Enter number"))
count=0
if n<=1:
  count=1
for _ in range(2,n):
    if n%2==0:
        count=1        
if count==0:
    print("prime")
else:
    print("not prime")

#5.sum of a given number
n=int(input("enter number"))
x=str(n)
sum=0
for i in x:
    c=int(i)
    sum=sum+c
print(sum)

#6.palindrome:
n=int(input("enter the number:"))
rev=int(str(n)[::-1])
if n==rev:
    print("palindrome")
else:
  print("not a palindrome")

#7.Amstrong number
def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    sum = sum(int(digit) ** num_digits for digit in digits)
    return sum == n
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")



#8.Factorial of a given number
import math
number = int(input("Enter a number: "))
factorial = math.factorial(number)
print(f"Factorial of {number} is {factorial}")

#using loops
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}")

#using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
number = int(input("Enter a number: "))
factorial = factorial_recursive(number)
print(f"Factorial of {number} is {factorial}")



#9.Strong number
import math
def is_strong_number(n):
    digits = str(n)
    sum = sum(math.factorial(int(digit)) for digit in digits)
    return sum == n
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong number.")
else:
    print(f"{number} is not a Strong number.")




