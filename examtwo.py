data=[]	
fp=open("carsales.txt","r")	
for line in fp:	
	line=line.replace("\n","")	
	line=line.split(",")	
	data.append(line)	
fp.close()

car_count=0 	
total_price=0 	
for car in data:	
	car_count+=1 	
	total_price+=float(car[1])  
avg_price=total_price/car_count 	
print("{:>5} Total Cars - Average Price: ${}".format(car_count,round(avg_price)))	
inp=input("Enter Car Make: ")	
while(inp!=""):	
	cur_car_count=0 	
	cur_total_price=0 	
	for car in data:	
		if car[0]==inp:	
			cur_car_count+=1 
			cur_total_price+=float(car[1])
	if(cur_car_count!=0): 
		cur_avg_price=cur_total_price/cur_car_count	
		print("{:>6}  Cars Sold".format(cur_car_count))
		print("${:>5}  Average Price".format(round(cur_avg_price)))
		diff=cur_avg_price-avg_price	
		percent_diff=(diff*100)/avg_price
		print("{:>5}% Above/Below Average".format(round(percent_diff,2)))
	else:	
		print("Car Make Not Found")
	inp=input("Enter Car Make: ")	