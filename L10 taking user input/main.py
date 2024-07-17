# input is taken using input function

# print('What is your name ? ')
# name = input()
# print(name)

# OR

number = input("Enter your favourite number: ")
print(number)
print(type(number)) # input function returns every input value as 'STRING'

new_string_num = number + '5' # ans -> 105
new_number = int(number) + 5 # ans -> 15

print(new_string_num)
print(new_number)

#
direct_num =float(input('Enter a decimal number :'))
print(direct_num)