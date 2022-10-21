m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(m): # A for loop for row entries
    a =[]
for j in range(n): # A for loop for column entries
    a.append(int(input()))
matrix.append(a)

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = " ")
print()
dup = []
for k in matrix:
    for i in k:
        dup.append(i)

print (max(dup))