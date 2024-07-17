# Lists are changeable meaning we can alter them after creation. But Tuples are non changable after creation

list_1 =[0,1,2,3,4,5,6,7,8,9]

print('Using positive index : ')


print(list_1[0])
print(list_1[1])
print(list_1[2])
print(list_1[6])
print(list_1[9])


print('Using negative index : ')

print(list_1[-1])
print(len(list_1) - 1) # conversion of above negative index to positive index
# good to convert negative to positive index
print(list_1[-5])
print(list_1[-9])
print(list_1[-10])

# We can check if a given item is present in the list. This is done using the "in" keyword.(CAN BE USED IN STRING ALSO)

if 7 in list_1:
    print('yes')
else:
    print('no')

print(list_1)
print(list_1[:]) # [0: len(list_1)]
print(list_1[2:]) # [2: len(list_1)]


#print(list_1[1:-1]) #convert it to positive index (10-1 = 9) :-
print(list_1[1:9])

print(list_1[1:9:2]) # 2 is the jump index o/p => [1,3,5,7]

# ---------- LIST COMPREHENSION ----------

list_2 = [el for el in range(5)] # [0,1,2,3,4]
print(list_2)

list_3 = [el*el for el in range(5)] # [0,1,4,9,16]
print(list_3)

list_4 = [el for el in list_1[1:7]] # [1,2,3,4,5,6]
print(list_4)

list_4 = [el for el in list_1[1:7] if el%2 == 0] # [2,4,6]
print(list_4)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

namesGreater_4 = [item for item in names if (len(item) > 4)]
print(namesGreater_4)







