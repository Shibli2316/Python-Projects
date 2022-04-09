import random
from weakref import WeakValueDictionary

def guessing_game(guessingLimit, number):
    random_number=random.randint(1,number)
    try:
        while guessingLimit>0:
            guess = int(input("What is your Guess?\n"))
            guessingLimit-=1
            if random_number==guess:
                print('Congratulations, You got it right')
                break
            elif guess> number:
                print("Your guess is out of range!!")
                print(f"You have {guessingLimit} guess(es) left")
            else:
                print("That was wrong")
                print(f"You have {guessingLimit} guess(es) left")
        print("Game Over")
        print(f"The number was {random_number}")
    except ValueError:
        print("Only integers are allowed")


def easy():
    print("You have to guess a number between 1-10, and you have 6 guesses")
    guessing_game(6,10)

def  medium():
    print("You have to guess a number between 1-20, and you have 4 guesses")
    guessing_game(4,20)

def  hard():
    print("You have to guess a number between 1-50, and you have 3 guesses")
    guessing_game(3,50)

def try_again():
    again=input("Do you want to play the game again? Yes/No:\n")
    if again.upper()=="YES":
        welcome()
    elif again.upper()=="NO":
        print("Thanks for playing")
    else:
        print("Wrong input")
        try_again()

def welcome():
    print("Welcome to the IMPROVED guessing game")
    difficulty = input("\tChoose your level:\n\tEasy.\n\tMedium.\n\tHard.:\n")
    if  difficulty.upper()=="EASY":
        easy()
        try_again()
    elif  difficulty.upper()=="MEDIUM":
        medium()
        try_again()
    elif  difficulty.upper()=="HARD":
        hard()
        try_again()
    else:
        print("You gave a wrong input")
        welcome()

welcome()