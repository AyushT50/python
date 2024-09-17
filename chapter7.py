# Loops

# While Loops
''''
i=1

while(i<=6):
    print("ayush")
    i +=1

l = [1,"harry",False,True,"rohan","shubham"]

i = 0
while(i<len(l)):
    print(l[i])
    i +=1


# For Loops

# for i in range(0,44,4):
#     print(i)

for i in l:
    print(i)

# For loops with else

l1 = [1,2,6]
for i in l1:
    print(i)

else:
    print("done") # this is printed when the loop exhausts!


# For loop using break

for i in range(100):
    if (i ==34):
        break # exit thr loop right now
    print(i)

for i in range(100):
    if (i == 34):
        continue # Skip this iteration\
    print(i)


# For loop using pass


for i in range(100):
    pass # skip this loop

i=0
while(i<45):
    print(i)
    i +=1


'''''

# practice set

# 1
'''''
n = int(input("enetr the number :"))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")
   '''

# 2 
'''''
l = ["harry","soham","sachin","rahul"]

for i in l:
    if (i.startswith("s")):
        print(f"hello {i}")
        '''
# 3
'''''
n = int(input("enetr the number :"))

i=1
while(i<=10):
    print(f"{n} X {i} = {n * i}")
    i +=1
    '''
# 4
'''''
n = int(input("enetr the number :"))

for i in range(2,n):
    if(n%i) == 0:
        print("number is not prime ")
        break
else:
    print("number is prime")
    '''

# 5
'''''
n = int(input("enetr the number :"))

i = 1
sum = 0
while(i<n):
    sum +=i
    i += 1
print(sum)
'''

# 7

n =  3 # Size of the square

for i in range(1, n+2):
        print('*')
