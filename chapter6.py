# Conditional statements

# if elif else ladder

'''''
a = int(input("enter your age :"))
if (a>=18):
    print("you can vote")

elif(a<=5 and a<0):
    print("you are child or you are entering negative age")


else:
    print("you cannot vote")
    '''

# multiple if statements
# a = int(input("enter your age :"))

# if statment no 1

''''
if(a%2 == 0):
    print("the a is even")
'''
# if statement no 2

'''''
if (a>=18):
    print("you can vote")

elif(a<=5 and a<0):
    print("you are child or you are entering negative age")


else:
    print("you cannot vote")

'''
# prcatice set

# 01
'''''
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))
d = int(input("enter the value of d:"))

if(a>b and a>c and a>d):
    print("a is greater")
elif(b>a and b>c and b>d):
    print("b is greater")

elif(c>a and c>b and c>d):
    print("c is greater")
else:
    print("d is greater")

    '''

# 2
''''
m1 = int(input("enter the marks1 :"))
m2 = int(input("enter the marks2 :"))
m3 = int(input("enter the marks3 :"))

total_per =(100* (m1+m2+m3))/300

if(total_per>=40 and m1>33 and m2>33 and m3>33):
    print("you're pass")
else:
    print("you're fail")
    '''

# 3
''''
a = "make a lot of money"
b = "click this"
c = "subcribe this"
d = "buy now"

message = input("enter the your message :")

if((a in message) or (b in message) or (c in message) or (d in message)):
    print("this is scam")
else:
    print("this is maybe not scam")
    '''
# 4
''''
a = input("enter the username :")
if (len(a)>=10):
    print("this user name is ok")
else:
    print("user name length should be 10 or more than 10")
'''

# 5
''''
list = [3,4,6,7,8,1]

num = int(input(" enter the number"))
if (num in list):
    print("entered number is present in list")
else:
    print("the number is not presennt in list")
'''
# 6
'''''
a = int(input("enter your marks :"))

if (a>=80):
    print("your grade is : A")
elif(a>=70):
    print("your grade is : B")
elif(a>=60):
    print("your grade is : C")
elif(a>=50):
    print("your grade is : D")
else:
    print("your grade is : F")
    '''
# 6
post = input("Enter your post")
if ("Harry" and "harry" in post):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")