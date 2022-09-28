inputFile = open("stock.txt", "r")
data = inputFile.read()
data = [float(i) for i in data.split()]
print = ("Price     Change")
print(data[0])
for i in range(l,len(data)):
    percentage = ((data[i] - data [i-1])/data[i-1]) * 100
    print ("{:.2f}   {:+.2f}%".format(data[i],percentage))
