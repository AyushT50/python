"""
Chapter 8: Functions and Recursions in Python
This chapter covers function definitions, types of functions, and recursion with practical examples.
Author: Ayush Tambe
Date: September 2024
"""

# Function Definition

def avg():
    """Calculates the average of three numbers."""
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    average = (a + b + c) / 3
    print(f"The average is: {average}")

# Function call (calling the avg function three times)
avg() 
avg() 
avg() 


# Quick Quiz: A simple function without arguments

def good():
    """Prints a simple greeting message."""
    print("Good Day!")

good()  # Function call


# Types of Functions:
# 1. Built-in functions: e.g., range(), print(), len().
# 2. User-defined functions: Functions that we define ourselves.


# Function with Arguments

def good(name, ending):
    """Prints a greeting message with a name and an ending phrase."""
    print(f"Good Day {name}{ending}")
    return "done"

# Calling the function with arguments
result = good("Ayush", ", thank you!")
print(result)  # Output: done


# Default Arguments in Functions

def good(name, ending=" Thank you!"):
    """Prints a greeting message with a name and a default ending phrase."""
    print(f"Good Day {name}{ending}")

# Calling the function with and without providing the second argument
good("Ayush")  # Uses the default argument for ending
good("Nilesh", ", have a great day!")  # Overrides the default argument

