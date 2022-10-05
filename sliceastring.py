userInput=input("Enter string: ")

print(userInput[2])
print(userInput[-2])
print(userInput[:5])
print(userInput[:-2])

for index in range(len(userInput)):
    if index % 2 == 0:
        print(userInput[index], end='')
print()
for index in range(len(userInput)):
    if index % 2 != 0:
        print(userInput[index], end='')
print()
print(userInput[::-1])

index=len(userInput)-1
while index>=0:
    print(userInput[index],end="")
    index-=2
print()
print(len(userInput))