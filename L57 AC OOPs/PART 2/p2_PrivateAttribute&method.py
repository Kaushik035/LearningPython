# Private attributes and methods are accessible within the class and are not accessible from outside the class


class Student:
    def __init__(self,name,roll):
        self.name =name
        self.__roll = roll # two underscore infront of attribute  makes it private

    def rollNo(self):  # not a private method
        print(self.__roll)

    def __RollNo(self):  # private method, cant be accessed outside class
        print(self.__roll)

    def forced_roll(self):
        self.__RollNo()

    

s1 = Student('Kaushik',422)
print(s1.name)
#print(s1.__roll) # will through error as __roll is a private class and cant be accessed from outside of the class

s1.rollNo()
# s1.__RollNo() # will throw error as private method

s1.forced_roll()