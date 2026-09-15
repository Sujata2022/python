x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

res = car["brand"]
print(res)
x = car.get("model")
print(x)

# but there is one diff bw both 
# if key is not present car["mfyear"] will give error and 
# same if key is not present then car.get("mfyear") will give None 

res = car["mfyear"]
print(res)
x = car.get("mfyear",1920)
print(x)

# hashing for finding the ke in dict 
# hence its the fastest datatype with search complexity O(1)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
# KeyError: 'modell' if key is not in dict 
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.items()) # loops
