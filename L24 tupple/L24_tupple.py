# TUPLES ARE SIMILAR TO LISTS,JUST Tuples ARE NON CHANGABLE(immutable)

tup = (0,1,2,3)

print(type(tup),tup)

# tup[1] = 55 # tuples are not changable

tup_1 =(5)
print(type(tup_1)) # int

tup_2 =(5,)
print(type(tup_2)) # tuple



if 2 in tup:
    print ('yes')
else: 
    print('no')


tup_3 = tup[1:3]
print(tup_3)

tup_4 = tup[0:4:2]
print(tup_4)

tup_5 = tup[0:4]
print(tup_5)