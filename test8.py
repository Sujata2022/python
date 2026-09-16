# conditional statmets 
# if - else - elif
# for loop --> collections -> cant be infinite 
# while loop -> until condition is true it will keep going on ..uptoo infinity
# def 

# if condition is satisfied --> if block will execute else , the else block will execute
# else block will not have any condition

# you can have only if also 
# if -elif-else #if condition is not sartisfied then will check elif 

# driving license
age  = eval(input("Enter your age: "))
if age >= 18:
    print("Eligible") #the space at the starting is called as indentation
else:
    print("Not Eligible")

# just like in java we use if{} , same way in python we use indentation
# which is equal to tab space "   "

# child , teenager , adult 
user_input = eval(input("Enter your age: "))
if user_input <= 12:
    print("You are Child.")
elif user_input <= 18:
    print("yoy are teenager")
else:
    print("you are adult")


# and , or
user_input = eval(input("Enter your age: "))
if user_input < 0 or user_input >120:
    print("invalid age")
elif user_input <= 12 and user_input >= 0 :
    print("You are Child.")
elif user_input <= 18 and user_input >=13:
    print("yoy are teenager")
else:
    print("you are adult")

# ternary operator
# single line if elif else loop 

user_input = eval(input("Enter your age: "))
status = "invalid age" if user_input < 0 or user_input >120 else "valid age"
print(status)


# gradesheet creation program
marks = eval(input("Enter your marks: "))
if marks >= 90:
    print("O Grade")
elif marks >= 80:
    print("A+ Grade")
elif marks >= 70:
    print("A Grade")
elif marks >= 60:
    print("B+ Grade")
elif marks >= 50:
    print("B Grade")
elif marks >= 40:
    print("C Grade")
else:
    print("you are fail")

# if you are writing multiple if statments then 
# every if will be checked 
# unklike if - elif - else

age = eval(input("Enter your age: "))
if age >= 18:
    print("you are no linger child")
if age >= 25:
    print("start earning now")
if age >= 75:
    print("you are old now no one will give you job")
if age >=100:
    print("now its time to rest and then rest in piece")
