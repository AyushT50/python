# Object Oriented Programming

''''
class Employee:
    name = "Ayush" # This is class attribute
    language = "python"
    salary = 9000000

a = Employee() # Here 'a' is object of Employee class and this is object call
print(a.name,a.language,a.salary)

a.l_name = "Tambe" # This is a object or instance attribute
print(a.name,a.l_name,a.language,a.salary)

# Here l_name is object or instance attribute and salary , language ,name are class attributes as they directly belong to the class
'''

''''
class Employee:
    language = "Python"
    salary = 9000000

harry = Employee()
harry.language = "Java" 
print(harry.language,harry.salary)
'''

# Self Parameter
'''
class Employee:
    language = "Python"
    salary = 9000000

    def getInfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning all of you")

harry = Employee() 
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)
'''

# Constructor
'''
class Employee:
    language = "Python"
    salary = 9000000

    def __init__(self, name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating a object ") # This is 'dunder' method which is automatically called 
        
    def getInfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning all of you")

harry = Employee("Ayush",14000000,"Java") 
print(harry.name,harry.language,harry.salary)
#harry.getInfo()
#harry.greet()
'''


# practice set 
# 1.
'''
class programmer:
    name = "ayush"
    salary = 9000000
    id = 121
    language = "Python"

    def __init__(self,name,salary,id,language):
        self.name = name
        self.salary = salary
        self.id = id
        self.language = language


a = programmer("ram",6000000,122,"Java")
print(a.name,a.salary,a.id,a.language)

b = programmer("sham",8000000,123,"Javascript")
print(b.name,b.salary,b.id,b.language)
'''

# 2. 
'''
class calculator:
    a = 5

    def cal(self):
        print(f"the square is:{self.a * self.a}")
        print(f"the square is:{self.a * self.a * self.a}")
       
b = calculator()
b.cal()
'''

#  3.       
'''
class calculator:
    a = 5

    def cal(self):
        print(f"the square is:{self.a * self.a}")
        print(f"the square is:{self.a * self.a * self.a}")

    @staticmethod
    def greet():
        print("hello")
       
b = calculator()
b.cal()
b.greet()
'''


