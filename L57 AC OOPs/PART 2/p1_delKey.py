# del keyword is used to delete object properties or object itself

class Student:
    def __init__(self,name,roll):
        self.name =name
        self.roll = roll

s1 = Student('Kaushik',422)
print(s1.name)
print(s1.roll)

del s1

# print(s1) # will give error as s1 is already deleted