# methods are functions that belongs to objects

# class consist of 2 things --> 1. Data(afttributes) /Properties
#                               2. Methods

# always takes a 'self' parameter

class Students:
    
    college_name = "IIT'Bombay"
    
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = roll
        self.marks=marks

    # method 
    def intro(self):
        print(f"Hello, my name is {self.name} and my college name is {self.college_name}")

    def roll_no(self):
        return self.roll
    
    def avg_mark(self):
        sum = 0
        for mark in self.marks:
            sum = sum + mark
        
        avg = sum/len(self.marks)

        return avg
    
s1 = Students('Kaushik',422,[89,92,96])
 
s1.intro()

roll_num = s1.roll_no()
print(roll_num)

average = s1.avg_mark()
print(average)