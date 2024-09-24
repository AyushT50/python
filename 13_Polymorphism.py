# polymorphism.py

"""
Polymorphism Demonstration in Python

This script showcases polymorphism through the use of operator overloading.
"""

class Complex:
    """A class to represent complex numbers."""
    
    def __init__(self, real: float, img: float):
        self.real = real
        self.img = img
    
    def show_num(self) -> None:
        """Display the complex number in the form a + bi."""
        print(f"{self.real} + {self.img}i")
    
    def __add__(self, other: 'Complex') -> 'Complex':
        """Overload the + operator to add two complex numbers."""
        return Complex(self.real + other.real, self.img + other.img)


# Example usage
num1 = Complex(1, 3)
num1.show_num()

num2 = Complex(4, 6)
num2.show_num()

num3 = num1 + num2  # Using overloaded + operator
num3.show_num()


# practice_set.py

"""
Practice Set for Python Classes and Inheritance

This script contains various exercises demonstrating class implementation.
"""

class Circle:
    """A class to represent a circle."""
    
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return 3.14 * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the circle."""
        return 2 * 3.14 * self.radius


# Example usage
c1 = Circle(15)
print(f"The area of the circle is: {c1.area()}")
print(f"The perimeter of the circle is: {c1.perimeter()}")


class Employee:
    """A class to represent an employee."""
    
    def __init__(self, role: str, department: str, salary: float):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self) -> None:
        """Display the employee's details."""
        print(f"Employee Info: Role={self.role}, Department={self.department}, Salary={self.salary}")


class Engineer(Employee):
    """A class to represent an engineer, inheriting from Employee."""
    
    def __init__(self, name: str, age: int):
        super().__init__("Engineer", "IT", 80000)  # Fixed salary for engineers
        self.name = name
        self.age = age


# Example usage
engineer = Engineer("Ayush Tambe", 19)
engineer.show_details()


class Order:
    """A class to represent an order."""
    
    def __init__(self, item: str, price: float):
        self.item = item
        self.price = price

    def __gt__(self, other: 'Order') -> bool:
        """Overload the > operator to compare order prices."""
        return self.price > other.price


# Example usage
order1 = Order("Laptop", 100000)
order2 = Order("Book", 500)
print(order1 > order2)  # Prints True or False based on price comparison
