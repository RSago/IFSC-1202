num = int(input("Enter a number (zero to quit): "))
if num == 0:
    print("Division by Zero")
    quit()
total = 0
average = 0
i = 0
while num > 0:
    total = total + num
    num = int(input("Enter a number (zero to quit): "))
    i = i+1
average = total / i
print("Average:", average)