strNumbers=input("\nEnter Values Separated by Spaces: ")

numbers=strNumbers.split()

arr=[]

for num in numbers:
    arr.append(num)

print("\nValues with an odd index number:")

for i in range(0,len(arr)):
    if(i%2!=0):
        print(arr[i],end="\n")