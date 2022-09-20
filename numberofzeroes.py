N = int(input("Enter N: "))
count=0 
for  num  in range(N):
    num=int(input("Enter Number: "))
    if num==0:
        count=count+1
print("Number of Zeros: ",count) 