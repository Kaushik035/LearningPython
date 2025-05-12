# 3 Types:

# 1. Single Inheritance
# 2. Multi-level inheritance
# 3. Multiple inheritance


#3 example:

class A:
    varA = 'A....'

class B:
    varB = 'B....'

class C(A,B):
    varC = 'C....'

var = C()

print(var.varA)
print(var.varB)
print(var.varC)
