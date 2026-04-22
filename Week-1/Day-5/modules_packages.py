#The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file. 

import sample_module
import another_sample_module as mx
import platform

sample_module.myModule("Sample")

'''
The package is a simple directory having collections of modules. 
This directory contains Python modules and also having __init__.py file by which the interpreter interprets it as a Package.
'''

a = mx.person1["age"]
print(a)

a = mx.person1["age"]
print(a)

# Built-in Modules
x = platform.system()
print(x)

#List all the defined names belonging to the platform module
x = dir(platform)
print(x)


