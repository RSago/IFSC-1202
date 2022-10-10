inp = raw_input("Enter values separated by spaces\n")
li = list(inp.split(" "))
n=len(li)
def Distinct(li,n):
 res=1
 for i in range(1,n):
    k=0
for k in range(i):
  #if elements are unique or distinct add 1
   if (li[i] == li [k]):
     break
  #if same element then it is not distinct and come out of loop
   if (i == k+1):
    res+=1
print("No. of Distinct elements are")
print(Distinct(li,n,))