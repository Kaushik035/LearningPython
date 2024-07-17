# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


current_time =int(time.strftime('%H'))

if (current_time >=0 and current_time < 12):
    print('GOOD MORNING')
elif (current_time >=12 and current_time < 18):
    print('GOOD AFTERNOON')
else :
    print('GOOD EVENING')


