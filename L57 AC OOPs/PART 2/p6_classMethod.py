# A class method is bound to the class and recieves the class as an implicit first argument

# NOTE :- Static method cant access or modify cclass state and general for utility

# class Person:

#     name = 'anonymous'

#     def changeName(self,name):
#         self.name = name

# p1 = Person()
# print(p1.name) # anonymous
# p1.changeName('Kaushik')
# print(p1.name) # kaushik
# print(Person.name) # anonymus


# in the above example the change name method doesnt change the class name attribute,instead it creates a name variabe for the p1 attribute and assign it name kaushik

# to change the class attriebute following ways:

#1

# class Person:

#     name = 'anonymous'

#     def changeName(self,name):
#         Person.name = name

# p1 = Person()
# print(p1.name) # anonymous
# p1.changeName('Kaushik')
# print(p1.name) # kaushik
# print(Person.name) # kaushik

#2


# class Person:

#     name = 'anonymous'

#     def changeName(self,name):
#         self.__class__.name = name

# p1 = Person()
# print(p1.name) # anonymous
# p1.changeName('Kaushik')
# print(p1.name) # kaushik
# print(Person.name) # kaushik


#3


class Person:

    name = 'anonymous'

    @classmethod # decorator
    def changeName(cls,name): # here cls is actually reffering to the Person class
        cls.name = name

p1 = Person()
print(p1.name) # anonymous
p1.changeName('Kaushik')
print(p1.name) # kaushik
print(Person.name) # kaushik




