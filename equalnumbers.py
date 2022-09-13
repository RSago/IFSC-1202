a=int(input('Enter First Number'))

b=int(input('Enter Second Number'))

c=int(input('Enter Third Number'))

if(a==b==c):
    print('3')

elif (a==b and a!=c) or (b==c and c!=a) or (a==c and c!=b):
    print('2')

elif(a!=b!=c):
    print ('0')