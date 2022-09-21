N = int(input("Enter N: "))
sum =0
fact = 1
for i in range(1, N + 1):
  fact *= i
  sum += fact
print("Sum of Factorials: {}".format(sum))