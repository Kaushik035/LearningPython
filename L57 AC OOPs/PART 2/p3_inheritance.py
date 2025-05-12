# INHERITANCE:

# When one class(child/derived) derives the properties and methods of another class(parent/base)

class Car:

    color = 'black'

    @staticmethod
    def start():
        print('car started...')

    @staticmethod
    def stop():
        print('car stopped..')

class ToyataCar(Car):

    def __init__(self,name):
        self.name = name

car1 = ToyataCar('fortuner')
car2= ToyataCar('sirus')

print(car1.name)
car1.start()
car2.stop()

print(car2.color)