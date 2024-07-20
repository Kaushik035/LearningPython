info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

#o/p ->
# {'name': 'Karan', 'age': 19, 'eligible': True}
# {'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}

# we can also use the del keyword to remove a dictionary item.

del info['age']
print(info)

# If key is not provided, then the del keyword will delete the dictionary entirely.

dict_1 = {'adam' : 25,'eve':51,'joe':66}

print(dict_1)

del dict_1
print(dict_1) # this will cause an error because "dict_1" no longer exists.



ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
print(ep1)

# The pop() method removes the key-value pair whose key is passed as a parameter.

ep1.pop(123)
print(ep1)

# The popitem() method removes the last key-value pair from the dictionary.

ep1.popitem()
print(ep1)

ep1.clear()
print(ep1)




