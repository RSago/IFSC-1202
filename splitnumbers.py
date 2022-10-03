def isEven(number):
    return number %2 ==0

def isOdd(number):
    return number %2 ==1

def isPrime(number):
    if(number> 1):
        for index in range(2,number//2):
            if(number % index == 0):
                return False
        return True
    else:
        return False

inputFile = open("numbers.txt","r")
outputEven = open("evennumbers.txt","w+")
outputOdd = open("oddnumbers.txt","w+")
outputprime = open("primenumbers.txt","w+")

for line in inputFile:
    line = int(line.strip())

    if isEven(line):
        outputEven.write(str(line) + "\n")
    elif isOdd(line): 
        outputOdd.write(str(line) + "\n")

    if isPrime(line):
        outputprime.write(str(line) + "\n")