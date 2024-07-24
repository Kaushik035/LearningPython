import random

choices = {
    'snake' : '0',
    'water' : '1',
    'gun' : '2'
}

user = input(f'Enter  --> 0 for SNAKE \n --> 1 for WATER \n --> 2 for GUN \n : ')

computer = random.choice(list(choices.values()))
print(f"Computer chooses : {computer}")

if user == computer:
    print('DRAW')

elif user

