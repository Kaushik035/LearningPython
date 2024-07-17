fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

count =0
for i in fruit:
    print(f"'fruit['{count}'] = ' {i} ")
    count = count +1

print(fruit[:5]) # Mango
print(fruit[:4]) # Mang
print(fruit[:3]) # Man

print(fruit[0:]) # Mango
print(fruit[1:]) # ango

print(fruit[0:5]) # Mango
print(fruit[0:4]) # Mang

print(fruit[2:4]) # ng  # includes 2 excludes 4

print(fruit[-4]) #a
print(fruit[-4:]) #ango
print(fruit[-5:]) #Mango









