# All classes have a function called __init__(), which is always executed when the object is being initiated.

class Students:
    name ='Kaushik'
    roll = '21'

    # constructor

    def __init__(self): # self parameter is the object that we create(here s1)
        print('new student object is created')
        print(self)

# constructor agar hum khud create nhi krte toh python humare liye khud create kr deta hai

s1 = Students()
print(s1)




# passing more arguments to the constructor:


class Car:
    def __init__(self,color,number):
        self.color = color # argument named color is created
        self.num = number
        print('creating car object')

car1 = Car('blue',7)
print(car1.color) # blue
print(car1.num) #7



# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.