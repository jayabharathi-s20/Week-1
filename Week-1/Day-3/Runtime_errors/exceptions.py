#Exception Handling

#Example-01
try:
    print(x)
except:
    print("exceptions occured")

#Many Exceptions
#Example-02
try:
    print(x)
except NameError:
    print("variable not defined")
except:
    print("exception occured")

#Else
#Example-03
try:
    print("hello")
except:
    print("exception occured")
else:
    print("exception occured")

#Finally
#Example-04
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#Example-05
try:
   number=int(input("enter a number : "))
   result=10/number
   print(result)
except ZeroDivisionError:
   print("denominator cannot be zero")
except ValueError:
   print("Invalid input")

#Example-06
try:
    age=int(input("enter your age : "))
    if age <18:
        raise ValueError("you must be above 18")
    else:
       print("access granted")
except ValueError as e:
   print(e)
   

#Example-07

def withdraw(balance,amount):
    try:
        if amount > balance:
            raise Exception("Insufficient balance")
        else:
           balance-=amount
           print(balance)
    except Exception as e:
        print(e)

withdraw(1000,6000)

#Example-08
try:
    username = input("Enter username: ")
    if username == "":
        raise Exception("Username cannot be empty")

    print("Login success")

except Exception as e:
    print("Error:", e)

finally:
    print("thank you")
        
      
   
   
