"""
Chapter 5: Dictionaries and Sets in Python
This script covers the usage of dictionaries and sets, two essential data structures in Python, demonstrating their basic operations and methods.
Author: Ayush Tambe
Date: September 2024
"""

# Dictionaries in Python
marks = {
    "harry": 100,
    "ayush": 99,
    "Ram": 98
}

print(marks, type(marks))  # Output: Dictionary with marks and its type

# Accessing dictionary values
# Uncomment the lines below to see how values can be accessed by keys.
'''
print(marks["ayush"])  # Output: 99
print(marks["harry"])  # Output: 100
print(marks["Ram"])    # Output: 98
'''

# Dictionary Methods
print(marks.items())  # Output: Dictionary items as key-value pairs
print(marks.keys())   # Output: Dictionary keys
print(marks.values()) # Output: Dictionary values

# Updating dictionary values
marks.update({"harry": 99})  # Updates 'harry' to 99
print(marks)  # Output: Updated dictionary

# Using get() method to access values
print(marks.get("ayush"))   # Output: 99 (returns the value if key exists)
print(marks.get("ayush1"))  # Output: None (returns None if key doesn't exist)

# Working with Sets
# Empty dictionary and empty set
D = {}  # This is an empty dictionary
e = set()  # This is an empty set
print(type(e))  # Output: <class 'set'>

# Basic set operations
s = {1, 2, 3}  # Set with integers
s1 = {33, 44, 55, 2, 3}

s.add(4)  # Adds 4 to the set
print(s)  # Output: {1, 2, 3, 4}

s.remove(2)  # Removes 2 from the set
print(s)  # Output: {1, 3, 4}

# Intersection of two sets
print(s.intersection(s1))  # Output: {3}

# Practice Set

# 1. Dictionary lookup practice
'''
words = {
    "hath": "hand",
    "per": "leg",
    "manus": "human"
}

word = input("Enter the word you want the meaning of: ")
print(words[word])
'''

# 2. Input numbers into a set (demonstrating uniqueness of set elements)
'''
s = set()
n1 = input("Enter the number 1: ")
s.add(int(n1))
n1 = input("Enter the number 2: ")
s.add(int(n1))
n1 = input("Enter the number 3: ")
s.add(int(n1))
n1 = input("Enter the number 4: ")
s.add(int(n1))
n1 = input("Enter the number 5: ")
s.add(int(n1))
n1 = input("Enter the number 6: ")
s.add(int(n1))

print(s)  # Output: Unique set of entered numbers
'''

# 3. Adding a string and integer to a set
s = set()
s.add("18")
s.add(18)
print(s)  # Output: {'18', 18}

# 4. Creating a dictionary with user input
'''
m = {}
v = input("Enter your name: ")
n = input("Enter favorite language: ")
m.update({v: n})

v = input("Enter another name: ")
n = input("Enter favorite language: ")
m.update({v: n})

print(m)  # Output: Dictionary with names and their favorite languages
'''

# 5. Error in set with mutable elements (Lists are not allowed in sets)
# Uncomment to see the error
'''
s2 = {8, 7, 12, "harry", [1, 2]}  # Lists are mutable, so this will raise an error
print(s2)
'''
