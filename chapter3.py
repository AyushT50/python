# strings

name = "ayush"
nameshort = name[0:3] # '0' means starting index and '3' means ending index 
# ^^^ start from index 0 all thr way till 3(excluding 3)

print(nameshort)# this will be print 'ayu'because i givned thh ending index is 3


# Negative Slicing
# in negative slicing index start from ending with -1
# e.g harry = ( y = -1), (r = -2) ,(r = -3) etc
print(name[-4:-1])#same as
print(name[1:4])

print(name[:4])# same as print(name[0:4])
print(name[0:4])
print(name[1:])# same as print(name[1:5])
print(name[1:5])


# STRINGS Function
# endswith,startswith,capitalize,upper,lower,count,replace
print(len(name))
print(name.endswith("ush"))# if name is end with yus the print yes
print(name.endswith("ayu"))

print(name.startswith("ayu"))# if name is start with ayu the print yes
print(name.startswith("ush"))

# Replace string
replacestring = name.replace("ayush","tambe")
print(replacestring)

#Escape sequence characters = \n, \t , ;\ , \ , \'ayush\' ,  etc...
print("name is ayush nilesh tambe\nsal is 20 core  ")


# practice set
# 1

a = input("enetr your name: ")
print("good afternoon  ",a)
print(f"good afternoon {a} ")# if you give the 'f' string

# 2

letter='''Dear <name>,
you are selected!
<Date>'''
print(letter.replace("<name>","ayush").replace("<Date>","01-01-2025"))
print(f"Dear {a}\nyou are selected!\n 01-01-2025")

# 3

name= "ayush  tambe"
print(name.find("  "))

# 4

print(name.replace("  "," "))

# 5
letter = "Dear harry,\nthis python course is nice.\n Thanks"
print(letter)










