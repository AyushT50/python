# File I/O 
''''
types of files
1. text files : .txt, .docx,.log
2 . binary files : .mp4, .mov, .png,etc.
'''

# syntax: f = open("file_name","mode")  #by default mode is 'read' and also in text mode
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

f = open("sample.txt", "w") # this will create new file with given name without doing aything

f.write("i am the white hat hacker") 
f.write("\nfrom india") 
f.close() # if data is open then anyone can access the data so close the data 
