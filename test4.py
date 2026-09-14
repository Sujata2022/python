# dictionary
# one of the very imp datatype

# collection of key value pair 
# d = {"name":"saurabh" , "marks":21}
# print(d)
# print(type(d))

# print(d["name"])

# import pandas as pd
# data = {"name":[chr(96+ i) for i in range(1 , 11)] , "marks":list(range(81 , 91))}
# print(data)
# df = pd.DataFrame(data)
# print(df)


# range 
# it will simply create one range type object 
# and allocate memory to only start , stop , step
# whenever you will try to create sequence 
# that time you ahve to do the typecasting 
# your collection will be generated 

# a list of values 1 to 1000
# use the range in this case 
# img = range(1 , 1001)
# print(img)
# print(list(img))


data = {"name":"saurabh" , "marks":93}
print(data.keys())
print(data.values())

data = {"name":"vishal" , "marks":"45" , "name":"saurabh"}

print(data["name"])
print(data["name"])
print(data["marks"])

data["grade"] = "C"
print(data)

# this is unorderd collection
# you cant use indexing and slicing on dict 
# because this is unorderd 