#Factory patterns--The Factory Pattern in Python is a design pattern where you create objects using a separate function or class instead of creating them directly.
#but lets subclasses decide which object to create.

# Without Factory
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"


animal = Dog()   

# With Factory Pattern
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"


class AnimalFactory:
    @staticmethod #@staticmethod is used to define a method inside a class that doesn’t need access to instance or class data.
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
        
animal = AnimalFactory.create_animal("dog")
print(animal.speak())

#The Singleton Pattern is a design pattern where a class is allowed to have only one instance (object) in the entire program.

class Single:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


a = Single()
b = Single()

print(a is b)