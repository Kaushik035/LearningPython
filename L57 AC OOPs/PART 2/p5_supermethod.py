# method used to access method of the parent class
# Super means parents

class Car:

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print('car started...')

    @staticmethod
    def stop():
        print('car stopped..')

class ToyataCar(Car):

    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyataCar('pirus','electric')
print(car1.type)