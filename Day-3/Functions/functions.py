#Python Functions

# Creating a Function
def my_function():
  print("Hello from a function")

#Calling a Function
my_function()

#You can call the same function multiple times:
my_function()
my_function()
my_function()

#Example-01
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(50))

#Return Values

#Example-02
def greetings():
  return "Hello gud morning"
message=greetings()
print(message)

#or

def greetings():
  return "Hello gud morning"
print(greetings())

#Example-03
def none():
  return
print(none())

#The pass Statement
def my_funtions():
  pass



