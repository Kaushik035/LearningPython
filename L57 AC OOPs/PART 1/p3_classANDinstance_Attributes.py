class Students:
    
    college_name = "IIT'Bombay" # here the college_name is a class attribute (common for all obj created and takes space in memory only once)
    
    def __init__(self,name,roll):
        self.name = name 
        self.roll_no = roll

        # here name,roll_no is a object/instance attribute (unique for all obj created and takes space in memory seperately for each obj created)

s1 = Students('Kaushik',422)
print(s1.name,s1.roll_no)

print(s1.college_name) 
#or
print(Students.college_name)

