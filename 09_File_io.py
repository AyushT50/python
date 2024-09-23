# File I/O 
"""
Chapter 5: File I/O  in Python
This script covers the usage of File I/O 
Author: Ayush Tambe
Date: September 2024
"""

"""
File I/O Operations in Python

This script demonstrates various file input/output operations,
including reading and writing text files, as well as handling
files using the context manager.
"""
'''

types of files
1. text files : .txt, .docx,.log
2 . binary files : .mp4, .mov, .png,etc.
'''

# syntax: f = open("file_name","mode")  #by default mode is 'read' and also in text mode
'''
Modes in File I/O
"r": Read - Default mode. Opens the file for reading.
"w": Write - Opens the file for writing (will overwrite existing content).
Writing to a file is straightforward. If the file exists, Python will overwrite it. If not, it will create a new file.
"a": Append - Opens the file for appending (adds content to the end).
"x": Create - Creates the file but raises an error if it already exists.
'''
''''
f = open("demo.txt","r")
f = open("demo.txt","w") # this overwrite the data when mode is 'w'
f = open("demo.txt","a") # 'a' mode add the more data in the file 
'''
''''
data = f.read() # for reading a data of file
print(data)
print(type(data))
'''

''''
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
'''

'''
# Reading line by line:
file = open("demo.txt", "r")
for line in file:
    print(line, end="")  # Each line includes a newline character, so 'end=""' prevents double spacing
print(file.read(10))  # Reads the first 10 characters of the file
file.close()
'''

'''
f = open("sample.txt", "w") # this will create new file with given name without doing aything

f.write("i am the white hat hacker") 
f.write("\nfrom india") 
f.close() # if data is open then anyone can access the data so close the data 
'''

# Using with Statement:

# The with statement automatically closes the file for you, which is the preferred method for file handling.
'''
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after this block
'''

# practical example:

with open("log.txt","w") as file:
    file.write("log entry 1:successful login.\n")
    file.write("log entry 2:attempted access to restricted file.\n")

with open("log.txt","r") as file:
    for line in file:
        print(line.strip()) # The strip() method in Python is used to remove any leading (spaces at the beginning) and trailing (spaces at the end) whitespace characters from a string.
