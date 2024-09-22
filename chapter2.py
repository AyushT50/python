# variables_and_datatypes.py

# Variables and Data Types Section
a = 5.3
b = 8.3
name = "Ayush"
sal = 45000
nothing = None

# Display the results of different operations
print("Sum of a and b (int):", int(a + b))
print("Name:", name)
print("Salary:", sal)
print("Nothing:", nothing)

# Arithmetic Operators Section
# Demonstrating basic arithmetic operations and shorthand operators
c = a + b
d = 1
d += 3  # Increment the value of 'd' by 3
print("New value of d:", d)

# Comparison Operators Section
# Demonstrating comparison between values
d = 5 <= 5
print("Is 5 less than or equal to 5?:", d)

# Logical Operators Section
# Demonstrating logical operations
print("Logical NOT of True:", not(True))
print("Logical NOT of False:", not(False))

# Type Operators Section
# Demonstrating type conversion and type-checking
a = "5"
b = float(a)  # Converting string 'a' to float
t = type(a)
print("Converted 'a' to float:", b)
print("Type of 'a':", t)

# Extra Learning Section
# Demonstrating additional functionality like printing with specific end values
print(8)
print(13, end=" ")
print(21)
