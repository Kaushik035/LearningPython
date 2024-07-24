l1 = [1,2,3]
l2 = l1
l3 =[1,2,3]

print(l1 == l2)
print(l1 is l2)
print(l1 == l3)
print(l1 is l3)


# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.