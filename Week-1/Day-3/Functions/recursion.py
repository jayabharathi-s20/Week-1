import sys

#Python Recursion

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

#Base Case and Recursive Case
#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument

#Recursion Depth Limit

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

