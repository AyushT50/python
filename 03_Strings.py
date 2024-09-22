"""
Chapter 3: Strings in Python
This script demonstrates basic string operations, slicing, and string functions.
Author: Ayush Tambe
Date: September 2024
"""

# Example of string slicing
name = "ayush"
nameshort = name[:3]  # Slice string from index 0 to 2 (excluding 3)
print(nameshort)  # Output: 'ayu'

# Negative Slicing
# Demonstrates how slicing from the end works
print(name[-4:-1])  # Output: 'yus'
print(name[1:4])    # Output: 'yus'

# Demonstrating string functions
print(len(name))  # Length of the string
print(name.endswith("ush"))  # True if name ends with 'ush'
print(name.startswith("ayu"))  # True if name starts with 'ayu'

# Replacing strings
new_name = name.replace("ayush", "tambe")
print(new_name)  # Output: 'tambe'

# Escape sequence characters
print("Name is Ayush Nilesh Tambe\nSalary: 20 crore")

# Practice problems
# Problem 1: Take user input and display a greeting
a = input("Enter your name: ")
print(f"Good afternoon, {a}")

# Problem 2: Use a template letter
letter = '''Dear <name>,
You are selected!
<Date>'''
letter = letter.replace("<name>", "Ayush").replace("<Date>", "01-01-2025")
print(letter)

# Problem 3: Find double spaces in a string
name_with_spaces = "ayush  tambe"
print(name_with_spaces.find("  "))

# Problem 4: Replace double spaces with single spaces
print(name_with_spaces.replace("  ", " "))

# Problem 5: Format a letter using escape sequences
formatted_letter = "Dear Harry,\nThis Python course is great.\nThanks"
print(formatted_letter)
