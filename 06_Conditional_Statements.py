"""
Chapter 6: Conditional Statements in Python
This script covers various types of conditional statements (if-elif-else) used for decision-making in Python, demonstrating ladder structures and multiple if statements.
Author: Ayush Tambe
Date: September 2024
"""

# If-Elif-Else Ladder

'''
a = int(input("Enter your age: "))
if a >= 18:
    print("You can vote")
elif 5 <= a < 0:
    print("You are a child or have entered a negative age")
else:
    print("You cannot vote")
'''

# Multiple If Statements

'''
a = int(input("Enter your age: "))

# If Statement No 1
if a % 2 == 0:
    print("The number is even")

# If Statement No 2
if a >= 18:
    print("You can vote")
elif 5 <= a < 0:
    print("You are a child or have entered a negative age")
else:
    print("You cannot vote")
'''

# Practice Set

# 1. Find the largest of four numbers

'''
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if a > b and a > c and a > d:
    print("a is the greatest")
elif b > a and b > c and b > d:
    print("b is the greatest")
elif c > a and c > b and c > d:
    print("c is the greatest")
else:
    print("d is the greatest")
'''

# 2. Check if a student passes based on marks and percentage

'''
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

total_percentage = (100 * (m1 + m2 + m3)) / 300

if total_percentage >= 40 and m1 > 33 and m2 > 33 and m3 > 33:
    print("You're pass")
else:
    print("You're fail")
'''

# 3. Detect spam based on keywords in a message

'''
spam_keywords = ["make a lot of money", "click this", "subscribe this", "buy now"]
message = input("Enter your message: ")

if any(keyword in message for keyword in spam_keywords):
    print("This is a scam")
else:
    print("This may not be a scam")
'''

# 4. Check if a username has at least 10 characters

'''
username = input("Enter your username: ")
if len(username) >= 10:
    print("This username is valid")
else:
    print("Username should be 10 characters or more")
'''

# 5. Check if a number is present in a list

'''
numbers = [3, 4, 6, 7, 8, 1]
num = int(input("Enter a number: "))

if num in numbers:
    print("Entered number is present in the list")
else:
    print("The number is not present in the list")
'''

# 6. Assign grades based on marks

'''
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Your grade is: A")
elif marks >= 70:
    print("Your grade is: B")
elif marks >= 60:
    print("Your grade is: C")
elif marks >= 50:
    print("Your grade is: D")
else:
    print("Your grade is: F")
'''

# 7. Detect if a post mentions 'Harry'

post = input("Enter your post: ")
if "Harry" in post or "harry" in post:
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")
