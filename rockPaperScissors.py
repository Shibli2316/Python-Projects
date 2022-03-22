import random
randNumb=random.randint(1,3)
# print(randNumb)
print("\tWelcome to the basic game of rock paper scissor")
print("\tTo play the game press 1")
print("\tTo exit press 2")
userInput=int(input("Enter your choise: "))
if userInput==1:
    while True:
        print("\tEnter your move:")
        print("\t1 For rock")
        print("\t2 For paper")
        print("\t3 For scissors")
        userMove=int(input("Enter your move: "))
        if (randNumb==1 and userMove==2) or (randNumb==2 and userMove==3) or (randNumb==3 and userMove==1):
            print("You win!!!")
        else:
            print("You lose")
else:
     exit
