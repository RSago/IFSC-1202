threeDigit = int(input())
units = threeDigit % 10
tens = int((threeDigit % 10 - units)/10)
hundreds =int((threeDigit % 1000 - threeDigit % 100)/100)
if hundreds < tens < units:
    print("YES")
else:
    print("NO")