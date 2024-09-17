# List and Tuples
lists =["Ayush", "Tambe", 5, 5.48, False , "apple"]
print(lists[5])
lists[0] = "Nilesh" 
print(lists[0])
print(lists[1:5])

# Lists Methods
# if you run any methods in lists that can be change but in string that doesn't change
# string is imutable and list is mutable
print(lists.append("ayush"))#this can add ayush in the end of the list
print(lists)

l1 = [1,5,3,8,9,10]
#l1.sort()
# l1.reverse()
l1.insert(3,3000) #insert 3000 at 3rd index of the list 
print(l1)
print(l1.pop(3))
print(l1.remove(1))
print(l1)


# Tupples
# also tupple can't be changed

a = (1,)
print(type(a))

b = (1,24,34,56,"ayush")
print(b)

# Practice set
# 1
'''a = []
f1=input("enetr the fruit 1")
a.append(f1)
f2=input("enetr the fruit 2")
a.append(f2)
f3=input("enetr the fruit 3")
a.append(f3)
f4=input("enetr the fruit 4")
a.append(f4)
f5=input("enetr the fruit 5")
a.append(f5)
f6=input("enetr the fruit 6")
a.append(f6)
f7=input("enetr the fruit 7")
a.append(f7)'''
# 2

'''''
a =[]
m1 = input("enetr theh marks1")
a.append(m1)
m2 = input("enetr theh marks1")
a.append(m2)
m3 = input("enetr theh marks1")
a.append(m3)
m4 = input("enetr theh marks1")
a.append(m4)
m5 = input("enetr theh marks1")
a.append(m5)
m6 = input("enetr theh marks1")
a.append(m6)

print(a.sort())'''

# 3
'''''
b = (34,"ayush")
b[1]= "tambe"
print(b)
'''

# 4
l = [3,4,6,1,8,5]
print(sum(l))


# 5

a = (7,0,8,0,0,9)

print(a.count(0))

