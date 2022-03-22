with open('hiscore.txt', 'w') as f:
    f.write(str(100))
import random
randNumber=random.randint(1, 100)
# print(randNumber)
userGuess=None
guesses=0
guesses_limit=5
out_of_guesses=False
while(userGuess !=randNumber) and not(out_of_guesses):
    if guesses<guesses_limit:
        try:
            userGuess=int(input("Entre your guess:\n"))
            guesses+=1
        except Exception as e:
            print("You entered an alphabet. Please entre a number.")
            continue
    else:
        out_of_guesses=True
    
        if out_of_guesses:
            print("You ran out of guesses. You lose")
            print(f"The number was {randNumber}")
        break
    
    if (userGuess==randNumber):
            print("You guessed it right!")
    else:       
            if (userGuess>randNumber):
                print("You guessed it wrong! Entre a smaller number")
            else:
                print("You guessed it wrong! Entre a larger number")

if (userGuess==randNumber):
    print(f"You guessed the number in {guesses} guesses")
    with open('hiscore.txt', 'r') as f:
        hiscore=int(f.read())

    if (guesses<hiscore):
        print("CONGRATULATION!")
        print(f"You have just broken the highscore. The new highscore is {guesses}")
        with open('hiscore.txt', 'w') as f:
            f.write(str(guesses))
    else:
        with open('hiscore.txt', 'r') as f:
            g=int(f.read())
        print(f"You coudnt break the high score. The highscore is {g}")