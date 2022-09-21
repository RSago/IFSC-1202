print("Winners and Losers")
human=0
computer=0
for i in range(5):
    print("Round:{}"(i+1))
humanNumber=int(input("Enter Your Guess: "))
computerGeneratedNumber=random.randint(1,5)
if (humanNumber+computerGeneratedNumber)%2==0:
    human=human+1
else:
    computer=computer+1
if (humanNumber+computerGeneratedNumber)%2==0:
    print("Sum is even.")
else:
    print("Sum is odd")
print("Human Score: {}\nComputer Score: {}".format(human,computer))
if human>computer:
    print("Human Wins")
else:
    print("Computer Wins")

