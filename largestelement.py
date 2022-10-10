integers = input("Enter Values Saparated by Spaces: ")
integers = [int(i) for i in integers.split()]
largest_index = 0
largest_val = integers[0]
for i in range(len(integers)):
    if integers[i] > largest_val:
        largest_val = integers[i]
        largest_index = i

print(f'Largest Value: {largest_val}')
print(f'Index of Largest Value: {largest_index}')