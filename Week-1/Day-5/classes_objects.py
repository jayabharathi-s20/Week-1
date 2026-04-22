#OOP--Python is an object-oriented language, allowing you to structure your code using classes

#A class defines what an object should look like, and an object is created based on that class.

#Classes-A Class is like an object constructor, or a "blueprint" for creating objects.

class SampleClass:#class creation
    x=5

#Creating multiple objects
obj1=SampleClass()
print(obj1.x)
obj2=SampleClass()
print(obj2.x)

#del obj1
print(obj1.x)

#Python __init__() Method--__init__ is a constructor method that runs automatically when you create an object.Its main role is to initialize (assign) values to the object’s properties (attributes).
#Example-01

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def profile(self):
        print(f"{self.name}-{self.price}")
        

item1= Item("Mouse", 250)
item2= Item("Printer", 100)
item3= Item("keyboard", 50)

print(item1.name,item1.price)
print(item2.name,item2.price)
print(item3.name,item3.price)

item1.profile()

#Example-02
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
        
s1=Student("Jaya",75)
s2=Student("Suba",35)

print(s1.result())
print(s2.result())

#a class without __init__()
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

#With __init__(),
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

#Default Values in __init__()
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


#Self params-reference to the current instance of the class.
#Without self, Python would not know which object's properties you want to access
#----------------------------------------------------------------------------------------------------------------------------------------

#Class properties:

#Properties are variables that belong to a class. They store data for each object created from the class.

#Access Properties
class Car:
  year=2020 # Class property

  def __init__(self, brand, model):
    self.brand = brand # Instance property
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

#Modify Properties
car1.brand="BMW"
print(car1.brand)

# Delete Properties
#del car1.model
print(car1.model)

#Modifying Class Properties
Car.year=2018
print(car1.year)

#----------------------------------------------------------------------------------------------------------------------------------------
#Class Methods--Methods are functions that belong to a class. They define the behavior of objects created from the class.
#Example-01
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

#Methods with Parameters
#Example-02
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

#Methods Accessing Properties
#Example-03
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

#Methods Modifying Properties
#Example-04
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

#The __str__() Method--The __str__() method is a special method that controls what is returned when the object is printed:

#Without the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

#With the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)








