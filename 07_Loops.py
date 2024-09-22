"""
Chapter 7: Loops in Python
This script covers while loops, for loops, and associated features like break, continue, and pass statements in Python.
Author: Ayush Tambe
Date: September 2024
"""

# While Loops
'''
i = 1
while i <= 6:
    print("Ayush")
    i += 1

# Looping through a list using a while loop
l = [1, "Harry", False, True, "Rohan", "Shubham"]
i = 0
while i < len(l):
    print(l[i])
    i += 1
'''

# For Loops
'''
# Looping through a list using a for loop
for i in l:
    print(i)

# For loop with range and step
for i in range(0, 44, 4):
    print(i)
'''

# For Loops with Else
'''
l1 = [1, 2, 6]
for i in l1:
    print(i)
else:
    print("Loop is done")  # Executed when the loop naturally exhausts
'''

# Break Statement in For Loops
'''
# Exit the loop when i equals 34
for i in range(100):
    if i == 34:
        break  # Break the loop
    print(i)
'''

# Continue Statement in For Loops
'''
# Skip the iteration when i equals 34
for i in range(100):
    if i == 34:
        continue  # Skip the current iteration
    print(i)
'''

# Pass Statement in For Loops
'''
# Using pass to skip the loop body
for i in range(100):
    pass  # Does nothing, a placeholder for future code

# Using while loop to print numbers
i = 0
while i < 45:
    print(i)
    i += 1
'''

# Practice Set

# 1. Print multiplication table of a given number
'''
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")
'''

# 2. Greet names starting with 's' from a list
'''
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")
'''

# 3. Multiplication table using a while loop
'''
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1
'''

# 4. Check if a number is prime
'''
n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
'''

# 5. Calculate the sum of the first n natural numbers
'''
n = int(input("Enter a number: "))
i = 1
sum = 0
while i < n:
    sum += i
    i += 1
print(f"Sum of first {n} numbers is: {sum}")
'''

# 7. Print a square pattern of size n using *
n = 3  # Size of the square
for i in range(1, n+2):
    print('*')
