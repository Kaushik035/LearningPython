import random

# List of quiz questions
questions = [
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the largest planet in our Solar System?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the boiling point of water in Celsius?"
]

# List of corresponding answers
answers = [
    ["Paris", 'India', 'Dubai', 'Russia'],
    ["4", '5', '3', '8'],
    ["Jupiter", 'neptune', 'earth', 'mercury'],
    ["Harper Lee", 'kaushik', 'rahim', 'rohini'],
    ["100", '101', '100.2', '101.2']
]

# Randomly shuffle the indices
random_indices = random.sample(range(len(questions)), len(questions))

# Extract questions and answers in random order
random_questions = [questions[i] for i in random_indices]
random_answers = [answers[i] for i in random_indices]

name = input('Enter your name: ')

prize = 0

if name:
    i = 0

    while i < len(random_questions):
        print(random_questions[i], '\n')
        print('Enter answer from the below given options: ')

        actual_ans = random_answers[i]
        shuffle_ans = random_answers[i].copy()
        random.shuffle(shuffle_ans)

        for z in shuffle_ans:
            print(z, end=' ')
        
        print()  # Print a newline for better readability

        answer = input('Type here: ')

        if answer == actual_ans[0]:
            prize = prize + 100 * (i + 1)
        else:
            print('GALAT JABAB!')
            break

        i = i + 1
        print('\n')

print(f"{name} won {prize} rupees")
