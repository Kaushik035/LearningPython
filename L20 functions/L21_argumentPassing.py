def average(*numbers):
  # print(type(numbers)) //numbers as a tuple aye h from the function call
  sum = 0
  for i in numbers:
    sum = sum + i
  avg = sum / len(numbers)
  return avg



c = average(5, 6,2,10)
print(c)


# ** mei arguments as a dict pass hote h

def name(**name):
  # print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")