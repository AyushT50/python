# Recursion
'''
Factorial(0) = 1
Factorial(1) = 1
Factorial(2) = 1 X 2 
Factorial(3) = 1 X 2 X 3
Factorial(4) = 1 X 2 X 3 X 4
Factorial(5) = 1 X 2 X 3 X 4 X 5

factorial(n) = n X n-1 X .... 3 X 2 X 1 

factorial(n) = n * factorial(n-1)
'''

''''
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter the number :"))
print(f"the factorial of {n} is :",factorial(n))
'''


# Practice set

# 1
''''
def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>a and b>c):
        print("b is greater")
    else:
        print("c is greater")

a = int(input("enter the values of a :"))
b = int(input("enter the values of b :"))
c = int(input("enter the values of c :"))

print(greatest(a,b,c))

'''

# 2
''''
def celtofah(c,f):
    return f
c = int(input("enter the tempreture in celcius to convert into fahrenheit :"))
f = c * (9/5) + 32
print(celtofah(c,f))

'''

# 3
''''
print("a")
print("b")
print("c", end=" ")
print("d", end=" ")
 '''

# 4

'''
def sum(n):
    if (n==1):
        return 1
    
    return sum(n-1) + n

n = int(input("enter the number : "))
print(sum(n))
'''

# 5
''''
def pattern(n):
    if (n==0):
        print("nothing")
        return
    print("*" * n)
    pattern(n-1)

pattern(3)
'''

# 6

def inch_to_cm(a):
    return a * 2.54

print(inch_to_cm(6))









    

