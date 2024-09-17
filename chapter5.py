# DICTIONARY AND SETS

marks = {

    "harry":100,
    "ayush":99,
    "Ram":98
}
print(marks,type(marks))
'''''
print(marks["ayush"])
print(marks["harry"])
print(marks["Ram"])
'''
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":99})
print(marks)
print(marks.get("ayush"))
print(marks.get("ayush1"))


# Sets

D ={}#this is empty dictionary
e = set() # and this is empty set
print(type(e))

s={1,2,3} #this is set
s1={33,44,55,2,3}
print(s.add(4),s)
print(s.remove(2),s)
# print(s.pop(),s)
print(s.intersection(s1))


# Practice set

# 1
'''''
words ={
    "hath":"hand",
    "per":"leg",
    "manus":"human"

}

word = input("enetr the word you want to meaning of :")

print(words[word])

'''

# 2
'''''
s = set()

n1 = input("enter the number 1:")
s.add(int(n1))
n1 = input("enter the number 1:")
s.add(int(n1))
n1 = input("enter the number 1:")
s.add(int(n1))
n1 = input("enter the number 1:")
s.add(int(n1))
n1 = input("enter the number 1:")
s.add(int(n1))
n1 = input("enter the number 1:")
s.add(int(n1))

print(s)

'''''
# 3

s=set()
s.add("18")
s.add(18)
print(s)

# 4
'''''
m = {}

v = input("enter your name :")
n = input("enter fav language :")
m.update({v: n})
v = input("enter your name :")
n = input("enter fav language :")
m.update({v: n})
v = input("enter your name :")
n = input("enter fav language :")
m.update({v: n})
v = input("enter your name :")
n = input("enter fav language :")
m.update({v: n})
print(m)
'''

# 5

s2= {8,7,12,"harry",[1,2]}
# print(s2.repalce([1,2],[3,4]))






