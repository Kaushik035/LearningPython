# Import string and random module
import string
import random


action = ('Code','Decode')
action_response = input(f'You want to {action[0]} or {action[1]} the word: ')

if action_response == 'Code':
    word =input('Enter the word you want to convert to sign language: ')


    if len(word)<3:
        if len(word) == 1:
            print(f"sing language word: {word}")
        else:
            l1 = word[0]
            l2 = word[1]
            sign_word = l2 + l1
            print(f"sing language word: {sign_word}")


    else:
        
        word = list(word)
        first_letter = word[0]
        word.pop(0)
        word.append(first_letter)

        new_word = ''

        for letter in word:
            letter = str(letter)

            new_word = new_word + letter
        word = new_word

        start1 = random.choice(string.ascii_letters)
        start2 = random.choice(string.ascii_letters)
        start3 = random.choice(string.ascii_letters)
        start = start1 + start2 +start3

        end1 = random.choice(string.ascii_letters)
        end2 = random.choice(string.ascii_letters)
        end3 = random.choice(string.ascii_letters)
        end = end1 + end2 +end3

        sign_word = start + word + end

        print(f'Sign langwage word: {sign_word}')
elif action_response == 'Decode':
    word =input('Enter the sign language you want to convert to normal word: ')

    
    if len(word)<3:
        if len(word) == 1:
            print(f"sing language word: {word}")
        else:
            l1 = word[0]
            l2 = word[1]
            sign_word = l2 + l1
            print(f"sing language word: {sign_word}")
    
    else:

        new_word = ''
        for letter in word[3:len(word)-3]:
            new_word = new_word + letter
            
        first = new_word[-1]

        actual_word=''

        for letter in new_word[0: len(new_word)-1]:
            actual_word = actual_word + letter

        actual_word = first + actual_word
        print(f'the actual word is: {actual_word}')

else:
    raise print(f'check the spelling of {action[0]} or {action[1]}')





    