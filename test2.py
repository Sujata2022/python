# strings are immutable 
# you cant perform change in same object 
# hence strings are immutable 

# what is the datatype which is mutable 
# List -- mutable 
# we can perform change in a same object 


# l = [1,2,3,4]
# print(l , id(l))

# l.append(20)
# print(l , id(l))

# [1, 2, 3, 4] 4312209536
# [1, 2, 3, 4, 20] 4312209536

# by looking at the output you can say that list is mutable 
# why because change is performed inside same object

# data = [1 ,2, "saurabh" , None , True, [1,2,3] , False]
# print(data[5])
# print(data[6])

# you can store the elememts of diff datatypes in the list 
# thats why its called as the hetrogenous collection of elements 
# as compared to array lists are slow 
# because there is no specified size for the list your list can have 
# any number of elements 

# data = [1 ,2, "saurabh" , None , True, [1,2,3] , False]

# print(data[-1])
# print(data[-5])

# print(data[-2][-2])
# print(data[-2][1])
# print(data[5][1])


# False
# saurabh

# so -ve imndexing starts with -1
# and +ve indexing starts with 0

# data = [1 ,2, "saurabh" , None , True, [1,2,3] , False]

# by using slicing i can extract the part of the list 
# if you want to extract thebpart of the list 
# you should pass data[start_index : stop_index +1]

# print(data[2:5]) # List output
# print(data[23]) # indexing this will give error
# # IndexError: list index out of range

# but slicing will never give me a error 
# data = [1 ,2, "saurabh" , None , True, [1,2,3] , False]
# print(data[999:10022]) # you will get empty list but you wont 
# get an error
# step -- in slicing 
# data[start_index : stop_index + 1 :step] 
# step will alwaya have default value 1

# 2 -> 4 my step will update my start
# 2 --> 3 step 1

# data = [1 ,2, "saurabh" , None , True, [1,2,3] , False]
# print(data[0:7:2])
# print(data[-1:-6:-1])
# print(data[-1:-6:]) # []

# tuple