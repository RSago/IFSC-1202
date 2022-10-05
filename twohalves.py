s = input("Enter a string: ")

half = int(len(s)/2)

print(s[half:] + s[:half])