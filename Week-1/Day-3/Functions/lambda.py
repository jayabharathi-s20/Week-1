#Lambda Functions--anonymous funtions

#Example-01
x=lambda a :a+10
print(x(5))

#Example-02
y=lambda a,b :a*b
print(y(2,2))

#Example-03
z=lambda a,b,c : a+b+c
print(z(5,5,4))

#Example-04
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Lambda with Built-in Functions

#Examples-05--Using Lambda with map()
lists=[1,2,3,4,5]
double=list(map(lambda x : x*x,lists))
print(double)

#Example-06
numbers=[1,2,3,4,5]
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)

#EXample-07
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_list=sorted(students,key=lambda x:x[1])
print(sorted_list)

#Example-08
words = ["apple", "pie", "banana", "cherry"]
sorted_words=sorted(words,key=lambda x:len(x))
print(sorted_words)
