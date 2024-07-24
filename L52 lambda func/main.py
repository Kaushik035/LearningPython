# def sum(a,b):
#     return(a+b)

sum = lambda x,y: x + y

print(sum(5,4))


# passing function as arguments to  functions

def apply(fx,a,b):
    return(6 + fx(a,b))

print(apply(sum,1,3))