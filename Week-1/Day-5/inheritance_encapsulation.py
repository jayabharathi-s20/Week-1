#Python Inheritance--Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):   # Dog inherits from Animal
    pass

dog = Dog()
dog.speak()

# Add the __init__() Function
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed

dog = Dog("Labrador")
# print(dog.name)
print(dog.breed)

#Use super()-- super() function that will make the child class inherit all the methods and properties from its parent:
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # super keyword--call parent constructor
        self.breed = breed

dog = Dog("Buddy", "Labrador")
print(dog.name)

#TYPES OF INHERITANCES
#Single inheritance--One child inherits from one parent
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()

#Multiple Inheritance--One child inherits from multiple parents
class Father:
    def fathers_work(self):
        print("Driving")


class Mother:
    def mothers_work(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()
c.fathers_work()
c.mothers_work()

#Multilevel Inheritance--Chain of inheritance (grandparent → parent → child)
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Puppy(Dog):
    pass


p = Puppy()
p.eat()
p.bark()

#Hierarchical Inheritance--One parent, multiple children
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.speak()
c.speak()

#Hybrid Inheritance--Combination of multiple types (complex structure)
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
d.show()

#------------------------------------------------------------------------------------------------------------------------

#Encapsulation--Encapsulation is about protecting data inside a class.

#It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

#This prevents accidental changes to your data and hides the internal details of how your class works.

#Private Properties--double underscore __ prefix

# Example
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
# print(p1.__age) # This will cause an error

# Get Private Property Value---To access a private property, you can create a getter method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())

#Set Private Property Value--To modify a private property, you can create a setter method.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

#Protected Properties--a single underscore _ prefix:

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) 









