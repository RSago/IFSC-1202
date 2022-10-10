def calculate_change(population_list):  
    population_change = [None]          
    for i in range(1, len(population_list)):    
        population_change.append(population_list[i] - population_list[i - 1])   
    return population_change    
def calculate_percentage(change, population):                                               
    percentage = [None]         
    for i in range(1, len(population)):
        percentage.append(change[i] / population[i - 1] *100)   
    return percentage       

year = list(range(1950, 1991))  
file = open('USPopulation.txt', 'r')  

population = []  
contents = file.readlines()  
for i in contents:  
    population.append(int(i.rstrip("\n")) * 1000)  
change = calculate_change(population)   
pr = calculate_percentage(change, population)   
print("Year\t\tPopulation\t\tChange\t\tPercentage")     

for i in range(len(population)):    
    if i != 0:          
        print(f'{year[i]}\t\t{population[i]}\t\t{change[i]}\t\t{pr[i]:.2f}%')
    else:               
        print(f'{year[i]}\t\t{population[i]}\t\t{change[i]}\t\t{pr[i]}')
avg_population_change = sum(change[1:])/len(change)     

print(f"\nAverage Population Change : {avg_population_change:.3f}\n")   

min = min(change[1:])           
min_year = year[change.index(min)]

max = max(change[1:])           
max_year = year[change.index(max)]

print("Year\tMinimumPopulation_Change")   
print(f"{min_year}\t{min}\n")

print("Year\tMaximumPopulation_Change")   
print(f"{max_year}\t{max}")