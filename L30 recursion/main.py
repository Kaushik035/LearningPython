# fact(n) = n* fact(n-1)

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 5; 
print("Number: ",num)
print("Factorial: ",factorial(num))

# recursion is calling a function inside itself


# fibonnavhi sequence

def fibo(n):
    if (n== 0):
        return 0
    elif (n==1):
        return 1
    else:
        a = fibo(n-1)
        b = fibo(n-2)
        return (a + b)
    
print (fibo(11))