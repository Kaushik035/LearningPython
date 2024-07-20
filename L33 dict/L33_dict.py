# dict are ordered

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info['name']) 
# print(info.get('name')) 


# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items()) # gives key value pair

for key, value in info.items(): # tuple gets unpacked and key gets 1st part of tuple and value gets 2nd part of tuple in info.items()
  print(f"The value corresponding to the key {key} is {value}") 