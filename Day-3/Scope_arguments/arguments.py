#Arguments

#Example-01
def greetings(fname,age):
    print(f"welcome ",fname)
    print(f"your age is ",age)

greetings("jaya",23)
greetings("suba",25)
greetings("ram",18)

#Parameters vs Arguments
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.

#Example-02
def sum(num1,num2):#this is a parameter
    return f"Sum of the values is {num1+num2}"
print(sum(20,2))
print(sum(20,2))

#Number of Arguments
#If you try to call the function with the wrong number of arguments, you will get an error:
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

#Default Parameter Values

#Example-03
def radius(diameter=10):
    return diameter/2
print(radius(12))
print(radius())

#Keyword Arguments

#Example-04
def my_function_kw(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function_kw(name = "Buddy", animal = "dog")

#Positional Arguments--When you call a function with arguments without using keywords, they are called positional arguments.
#Switching the order changes the result---The order matters with positional arguments:

#Example-05
def my_function_pw(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function_pw("Buddy", "dog")

#Mixing Positional and Keyword Arguments

#Example-06
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#Passing Different Data Types

#Example-07
def diff_datas(names):
   for name in names:
      print(name)

names=["jaya","suba","ram"]
diff_datas(names)

#Example-08
def profile(details):
   print("Name",details["name"])
   print("Location",details["location"])

details={
   "name":"jaya",
   "location":"Chennai"
}
profile(details)
      
#Return Values

#Example-09
def calculate(x,y):
   return x+y

result=calculate(2,5)
print(result)

#Returning Different Data Types

#Example-10
def list_function():
   return ["apple","mango",25,True]
result=list_function()
print(result[0])
print(result[1])
print(result[2])

#Positional-Only Arguments

#Example-11
def invite(name,/):
   print("Hello",name)
invite("jaya")

# def invite(name,/):
#    print("Hello",name)
# invite(name="jaya")#this will raise an error

#Keyword-Only Arguments

##Example-12
def kw_arguments(*, name):
  print("Hello", name)

kw_arguments(name = "Emil")

# def kw_arguments(*, name):
#   print("Hello", name)

# kw_arguments("jaya")



#ARGUMENTS_TYPES
#1. Positional Arguments
def greet(name,age):
   print(name,age)
greet("jaya",20)

#2.Keyword Arguments
def invite(name,age):
   print(name,age)
   greet(name="jaya",age=23)

#3.Default Arguments
def person(name,age=18):
   print(name)
   print(age)

person("jaya",23)
person("bharathi")

#4.Variable-length Positional Arguments(*args)
def add(*numbers):
   print(numbers)
add(1,20,4,56)

#5.Variable-length Keyword Arguments (**kwargs)
def profile(**data):
    print(data)

profile(name="jaya", age=20)





