# Methods that don’t use the self parameter (work at class level)


class Student:

    @staticmethod #decorator
    def college():
        print( 'IIT bombay' )

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

s1 = Student()
s1.college()



# Abstraction --> Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation --> Wrapping data and functions into a single unit (object).