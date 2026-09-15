# how to take user inputs ?
# input function
# whatever input its taking default it will be in string 
# we can convert the input in our required format using the datatype functions
# such as int , float , eval

# if i want to take integer input
age = int(input("Enter your age: "))
print(age) #34
print(type(age)) # int
# Enter your age: 89.78: # ValueError: invalid literal for int() with base 10: '89.78

# if i want to take float input
salary = float(input("Enter your salary: ")) #45.67 , 34 , "saurabh"
print(salary) # 45.67 , 34.0 , "error"
print(type(salary)) # <class 'float'> , <class 'float'> , "error"

# if i want to take any string as input
# you have no need to mention any datatype arount input function
# because every thing that its taking input will be string by default

name = input("Enter your name: ")
print(name)
print(type(name))
# everything by default will be string in input function

# but what if you wantv to take both types of input 
# int , float in same function
# that time will use eval

data = eval(input("Enter your data: ")) # saurabh
print(data)
print(type(data))


# Enter your data: 89.99
# 89.99
# <class 'float'>

# Enter your data: 78
# 78
# <class 'int'>

# Traceback (most recent call last):
# data = eval(input("Enter your data: ")) --> saurabh
# NameError: name 'saurabh' is not defined

# eval is not always afe to use because user can pass any code 
# and it will execute that code