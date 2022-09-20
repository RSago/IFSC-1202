n= int(input("Enter N:"))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "COMPOSITE")
            break
    else:
        print(num, "PRIME")
else:
    print(num, "COMPOSITE")