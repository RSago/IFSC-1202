int(input("Enter Number: "))
sum =0
fact = 1
for i in range(1, N + 1):
  fact *= i
  sum += fact
print("SUM: {}".format(sum))