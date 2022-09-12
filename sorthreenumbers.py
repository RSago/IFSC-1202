x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)