num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%4
    rev=rev*4+dig
    num=num//4
if(temp==rev):
    print("YES")
else:
    print("NO")