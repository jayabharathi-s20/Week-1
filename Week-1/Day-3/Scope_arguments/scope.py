#Local Scope

#Example-01
def my_function():
    x=10
    print(x)
my_function()

#Function Inside Function

#Example-02
def outer_function():
    x=20
    def inner_funtion():
        print(x)
    inner_funtion()
outer_function()

#Global Scope

#Example-03
x=300
def global_function():
    print(x)
global_function()
print(x)

#Example-04
x=15
def glob_funtion():
    x=20
    print(x)
glob_funtion()
print(x)

#Example-05
def global_kw():
    global x
    x=26
global_kw()
print(x)

#Example-06
#Also, use the global keyword if you want to make a change to a global variable inside a function.
x=300
def change_global():
    global x
    x=200
    print(x)
change_global()
print(x)

#Nonlocal Keyword
#Example-07
def nonlocal_function():
    x="jaya"
    def inner_funtions():
        nonlocal x
        x="bharathi"
    inner_funtions()
    return x
print(nonlocal_function())



