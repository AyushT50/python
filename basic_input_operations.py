# Basic Input and Arithmetic Operations in Python

# Taking two integer inputs and printing them
a = int(input("Enter the value 1: "))  
b = int(input("Enter the value 2: "))  
print("The number 1 is:", a)  
print("The number 2 is:", b)  

# Performing and printing the sum of a and b
print("The sum is:", a + b)  

# Taking a string input and displaying its type
a = input("Enter a value: ")  
print("The entered value is:", a)  
print("The type of the value is:", type(a))  

# Comparison of two integers
a = int(input("Enter the value of a: "))  
b = int(input("Enter the value of b: "))  
c = a > b  
print("Is a greater than b? ", c)  

# Performing arithmetic operations
a = 4  
b = 2  

# Printing the average and square of numbers
print("The average is:", (a + b) / 2)  
print("The square of a is:", (a * a))  

# Using bitwise XOR incorrectly to find square (should be corrected)
# Note: ^ is the bitwise XOR operator, not the exponentiation
print("The square of a using XOR (incorrect):", (a ^ a))  # Incorrect in Python

# Correct way to square b
print("The square of b is:", (b * b))  
