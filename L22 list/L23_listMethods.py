# LISTS ARE CHANGABLE

random = [1,True,'kaushik',55]
print(random)

random.append(8) # [1,True,'kaushik',55,8]
print(random)


num =[0,1,1,8,56,47,1001,2,56,1]
print(num)

print(num.index(56)) # index of first occourance of 56 is 4

print(num.count(1))

num.reverse()
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2,'kaushik')
print(num)

newList = ['sonu','papai','kanik']

num.extend(newList)
print(num)

k = num + newList  #concatination of lists
print(k)


# IMPOTANT

a = [1,2,3]
print(a)
b= a
print(b)

b[1] =55

print(a)
print(b)



c = [5,6,7]
d =c.copy()

print(c)
print(d)

d[2] = 69

print(c)
print(d)









