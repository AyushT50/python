"""
Chapter 4: Lists and Tuples in Python
This script demonstrates basic operations on lists and tuples, including list methods and tuple immutability.
Author: Ayush Tambe
Date: September 2024
"""

# Working with Lists
lists = ["Ayush", "Tambe", 5, 5.48, False, "apple"]
print(lists[5])  # Output: 'apple'

# Modifying list elements (lists are mutable)
lists[0] = "Nilesh"
print(lists[0])  # Output: 'Nilesh'
print(lists[1:5])  # Slicing the list from index 1 to 4 (excluding 5)

# List Methods
# Lists are mutable, meaning their contents can be changed.
print(lists.append("Ayush"))  # Appends "Ayush" to the end of the list
print(lists)  # Output: Modified list

# Working with another list
l1 = [1, 5, 3, 8, 9, 10]
l1.insert(3, 3000)  # Inserts 3000 at index 3
print(l1)  # Output: [1, 5, 3, 3000, 8, 9, 10]

# Removing elements
print(l1.pop(3))  # Removes the element at index 3
print(l1.remove(1))  # Removes the element with value 1
print(l1)  # Output: Modified list after pop and remove

# Working with Tuples
# Tuples are immutable, meaning they cannot be changed once created.
a = (1,)
print(type(a))  # Output: <class 'tuple'> (single element tuple)

b = (1, 24, 34, 56, "Ayush")
print(b)  # Output: Tuple elements

# Practice Set
# 1. Taking input for a list of fruits
'''
a = []
f1 = input("Enter fruit 1: ")
a.append(f1)
f2 = input("Enter fruit 2: ")
a.append(f2)
f3 = input("Enter fruit 3: ")
a.append(f3)
f4 = input("Enter fruit 4: ")
a.append(f4)
f5 = input("Enter fruit 5: ")
a.append(f5)
f6 = input("Enter fruit 6: ")
a.append(f6)
f7 = input("Enter fruit 7: ")
a.append(f7)
print(a)
'''

# 2. Taking input for a list of marks and sorting it
'''
a = []
m1 = input("Enter marks 1: ")
a.append(m1)
m2 = input("Enter marks 2: ")
a.append(m2)
m3 = input("Enter marks 3: ")
a.append(m3)
m4 = input("Enter marks 4: ")
a.append(m4)
m5 = input("Enter marks 5: ")
a.append(m5)
m6 = input("Enter marks 6: ")
a.append(m6)

a.sort()
print(a)  # Sorted list of marks
'''

# 3. Demonstrating immutability of tuples
'''
b = (34, "Ayush")
b[1] = "Tambe"  # This will raise an error because tuples are immutable
print(b)
'''

# 4. Summing a list of numbers
l = [3, 4, 6, 1, 8, 5]
print(sum(l))  # Output: Sum of the list elements

# 5. Counting the occurrence of 0 in a tuple
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))  # Output: 3 (counts how many times 0 appears)
