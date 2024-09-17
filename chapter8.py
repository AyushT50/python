# Functions and Recursions

# Functuion defining :-

''''
def avg():  
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    c = int(input("Enter the number"))

    average = (a + b + c)/ 3
    print(average)

# function call or calling
avg() 
avg()
avg()

'''

# Quick Quiz
''''
def good():
    print("good day")

good()
'''

# Types of functions :- 1 . Built in functions .  eg., range(), print(),len().
#                       2 . User defined functions

# Function with arguments

''''
def good(name,ending):
    print("good day " + name + ending)
    return "done"

a = good("Ayush"," thank you")
print(a)
'''

# Default arguments
'''''
def good(name,ending=" Thank you"):
    print("Good Day " + name + ending)

good("Ayush")

'''







