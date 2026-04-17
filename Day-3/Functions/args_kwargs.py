#Arbitrary Arguments - *args

#Example-01
def arbitary_function(*names):
    print(names[1])

arbitary_function("jaya","emily","ram","suba")

#Example-02
def my_functions(*args):
    print("type",type(args))
    print(args[0])
    print(args[1])
    print(args[2])
my_functions("jaya",25,True)

#Using *args with Regular Arguments

#Example-03
def combine_args(location,*names):
    for name in names:
        print(location," - ",name)

combine_args("banglore","jaya","bharathi","ram","suba")

#Example-04
def sum_of_numbers(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
print(sum_of_numbers(10,20,30,12,55,65))
print(sum_of_numbers(1,5,4))
print(sum_of_numbers(10,205,33))

#Example-05
def max_number(*numbers):
    if len(numbers)==0:
        return None
    max_num=numbers[0]
    for num in numbers:
        if num > max_num:
            max_num=num
    return max_num
print(max_number(12,50,22,30))

#Arbitrary Keyword Arguments - **kwargs

#Example-06
def person_details(**details):
    print("His last name is ", details["lname"])

person_details(fname="jaya",lname="bharathi")

#Example-07
def kw_args(**details):
    print(type(details))
    print("Name", details["name"])
    print("Age", details["age"])
kw_args(name="jaya",age=23)

#Combining *args and **kwargs

#Example-08
def my_function(name,*nums,**kwargs):
    print(name)
    for num in nums:
        print("numbers ",num)
    # print(kwargs["name"])
    print(kwargs.get("user_name"))

my_function("jaya",12,52,1,23,user_name="anika",age=30)

