import random
def rolling():
    randNumb=random.randint(1,6)
    print(randNumb)
    if randNumb==1:
        print(" -----")
        print("|     |")
        print("|  *  |")
        print("|     |")
        print(" -----")
    elif randNumb==2:
        print(" -----")
        print("|*    |")
        print("|     |")
        print("|    *|")
        print(" -----")
    elif randNumb==3:
        print(" -----")
        print("|  *  |")
        print("|  *  |")
        print("|  *  |")
        print(" -----")
    elif randNumb==4:
        print(" -----")
        print("|*   *|")
        print("|     |")
        print("|*   *|")
        print(" -----")
    elif randNumb==5:
        print(" -----")
        print("|*   *|")
        print("|  *  |")
        print("|*   *|")
        print(" -----")
    elif randNumb==6:
        print(" -----")
        print("|*   *|")
        print("|*   *|")
        print("|*   *|")
        print(" -----")
        rolling()

print("To roll the dice press 1\nTo exit press 2")
userChoice=int(input("Enter your choice: "))
while True:
    if userChoice==1:
        rolling()
    else:
        exit()