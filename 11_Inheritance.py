# Inheritance Demonstration in Python

"""
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) where one class derives the properties and methods of another class.
"""

class Car:
    """A base class representing a car."""
    
    @staticmethod
    def start():
        """Starts the car."""
        print("Car started...")

    @staticmethod
    def stop():
        """Stops the car."""
        print("Car stopped...")


class ToyotaCar(Car):
    """A derived class representing a specific type of car, Toyota."""
    
    def __init__(self, name):
        self.name = name


# Example of Single Inheritance
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
car1.start()  # Output: Car started...

# Example of Multi-Level Inheritance
class Fortuner(ToyotaCar):
    """A specific model of Toyota."""
    
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

fortuner_instance = Fortuner("Fortuner", "2023")
fortuner_instance.start()  # Output: Car started...

# Example of Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c_instance = C()
print(c_instance.varA)  # Output: Welcome to class A
print(c_instance.varB)  # Output: Welcome to class B
print(c_instance.varC)  # Output: Welcome to class C

# Demonstrating the Super() Method
class Vehicle:
    """A base class representing a vehicle."""
    
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class ToyotaCar(Vehicle):
    """A derived class representing a Toyota vehicle."""
    
    def __init__(self, name):
        self.name = name
        super().__init__("Car")
        self.start()

# Example of Class Method
class Person:
    """A class representing a person."""
    
    name = "Ayush"

    @classmethod
    def change_name(cls, new_name):
        """Changes the name of the person."""
        cls.name = new_name

person_instance = Person()
person_instance.change_name("Rahul")
print(person_instance.name)  # Output: Rahul
print(Person.name)  # Output: Rahul

# Using Property Decorator
class Student:
    """A class representing a student with marks."""
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @property
    def percentage(self):
        """Calculates the percentage based on marks."""
        return str((self.m1 + self.m2 + self.m3) / 3) + "%"

student_instance = Student(98, 99, 100)
print(student_instance.percentage)  # Output: 99.0%
student_instance.m1 = 96
print(student_instance.percentage)  # Output: 97.66666666666667%
