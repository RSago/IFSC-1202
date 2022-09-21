def Fibonacci(n):
    if (n <1): # if n less than 1
        return n
    if(n==0):
        return 0
    if (n == 1 or n == 2): # if n is 1 or 2
        return 1
    return ((Fibonacci(n-1)) + (Fibonacci(n-2))) #recursive calling function
n = int(input("Enter Fibonacci Sequesnce Number: "))
print("Fibonacci Number:",Fibonacci(n))