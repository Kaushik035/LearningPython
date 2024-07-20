# Sets are unordered collection of data items.
# mutable
# sets are unchangeble,that is we cant obtain any value through its index and change it, as sets are unordered
# same as list just values can't repeat and unordered

s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

a = {} 
print(type(a),a) #dict


harry = set() # empty set
print(type(harry),harry) # set

for value in info:
    print(value)