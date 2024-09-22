"""
Chapter 8.1: Recursion in Python
This script demonstrates recursion with a factorial example and various other functions.
Author: Ayush Tambe
Date: September 2024
"""

# Factorial using Recursion
'''
Factorial(0) = 1
Factorial(1) = 1
Factorial(2) = 1 X 2 
Factorial(3) = 1 X 2 X 3
Factorial(4) = 1 X 2 X 3 X 4
Factorial(5) = 1 X 2 X 3 X 4 X 5

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    """Calculates the factorial of a given number n using recursion."""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")


# Practice Set

# 1. Find the greatest of three numbers
def greatest(a, b, c):
    """Finds the greatest of three numbers."""
    if a > b and a > c:
        return "a is greater"
    elif b > a and b > c:
        return "b is greater"
    else:
        return "c is greater"

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
print(greatest(a, b, c))


# 2. Celsius to Fahrenheit converter
def cel_to_fah(c):
    """Converts Celsius to Fahrenheit."""
    return c * (9 / 5) + 32

c = int(input("Enter the temperature in Celsius to convert to Fahrenheit: "))
print(f"The temperature in Fahrenheit is: {cel_to_fah(c)}")


# 3. Print with specific formatting
print("a")
print("b")
print("c", end=" ")
print("d", end=" ")


# 4. Sum of the first n natural numbers using recursion
def sum_of_n(n):
    """Calculates the sum of the first n natural numbers using recursion."""
    if n == 1:
        return 1
    return n + sum_of_n(n - 1)

n = int(input("Enter a number: "))
print(f"Sum of the first {n} natural numbers is: {sum_of_n(n)}")


# 5. Print a pattern using recursion
def pattern(n):
    """Prints a reverse triangle pattern of stars using recursion."""
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

pattern(3)


# 6. Inches to centimeters converter
def inch_to_cm(a):
    """Converts inches to centimeters."""
    return a * 2.54

print(f"6 inches is equal to {inch_to_cm(6)} cm")
