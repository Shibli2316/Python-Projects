import random
randnumber=random.randint(1,4)

import pyttsx3
engine = pyttsx3.init()

if randnumber==1:
    noun1=str(input("Enter a noun: "))
    noun2=str(input("Enter a noun: "))
    pronoun1=str(input("Enter a pronoun: "))
    pronoun2=str(input("Enter a pronoun: "))
    number1=int(input("Enter a number: "))
    plural1=str(input("Enter a plural word: "))
    adjective1=str(input("Enter an adjective: "))
    engine.say(f"Once upon a time there lived a {noun2} named {noun1}. {pronoun1} always used to ask his {plural1} to practice daily but they would never listen to {pronoun1}. As time went by {noun2} was getting {adjective1} at his work. Later {pronoun1} collaborated with {pronoun2} and made {number1} projects. This being the first in many.")
    engine.runAndWait()
    print(f"Once upon a time there lived a {noun2} named {noun1}. {pronoun1} always used to ask his {plural1} to practice daily but they would never listen to {pronoun1}. As time went by {noun2} was getting {adjective1} at his work. Later {pronoun1} collaborated with {pronoun2} and made {number1} projects. This being the first in many.")

if randnumber==2:
    place1=str(input("Enter the name of a place you like: "))
    noun1=str(input("Enter a noun: "))
    place2=str(input("Enter the name of a place you like: "))
    adjective1=str(input("Enter an adjective: "))
    adjective2=str(input("Enter an adjective: "))
    adjective3=str(input("Enter an adjective: "))
    engine.say(f"This is a story of a lost {place1}. There lived a {adjective1} {noun1} who always created problem for the parents and they were very {adjective2} of {noun1}. One day they decided to put him in a {place2}. {noun1} was very {adjective2}, but nevermind {noun1} never stopped doing {adjective3}")
    engine.runAndWait()
    print(f"This is a story of a lost {place1}. There lived a {adjective1} {noun1} who always created problem for the parents and they were very {adjective2} of {noun1}. One day they decided to put him in a {place2}. {noun1} was very {adjective2}, but nevermind {noun1} never stopped doing {adjective3}")

if randnumber==3:
    verb1=str(input("Enter a verb: "))
    verb2=str(input("Enter a verb: "))
    verb3=str(input("Enter a verb: "))
    adjective1=str(input("Enter an adjective: "))
    adjective2=str(input("Enter an adjective: "))
    noun1=str(input("Enter a noun: "))
    noun2=str(input("Enter a noun: "))
    villan=str(input("Enter the name of a villan: "))
    food=str(input("Enter your fav food: "))
    engine.say(f"It was {adjective1} day at school, and {noun1} was super {adjective2} for lunch. But when she went outside to eat, a {villan} stole her {food} ! {noun1} chased the {villan} all over school. She {verb1} , {verb2} , and {verb3} through the playground. Then {noun1} tripped on her {noun2} and the {villan} escaped! Luckily, {noun1}'s friends were willing to share their {food} with her.")
    engine.runAndWait()
    print(f"It was {adjective1} day at school, and {noun1} was super {adjective2} for lunch. But when she went outside to eat, a {villan} stole her {food} ! {noun1} chased the {villan} all over school. She {verb1} , {verb2} , and {verb3} through the playground. Then {noun1} tripped on her {noun2} and the {villan} escaped! Luckily, {noun1}'s friends were willing to share their {food} with her.")

if randnumber==4:
    verb1=str(input("Enter a verb: "))
    verb2=str(input("Enter a verb: "))
    verb3=str(input("Enter a verb: "))
    adjective1=str(input("Enter an adjective: "))
    adjective2=str(input("Enter an adjective: "))
    adjective3=str(input("Enter an adjective: "))
    adjective4=str(input("Enter an adjective: "))
    adverb1=str(input("Enter an abverb: "))
    adverb2=str(input("Enter an abverb: "))
    noun1=str(input("Enter a noun: "))
    noun2=str(input("Enter a noun: "))
    engine.say(f"Today I went to the zoo. I saw a {adjective1} {noun1} jumping up and down in its tree. He {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. I got some peanuts and passed them through the cage to a gigantic gray {noun2} towering above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. It filled my stomach. Afterwards I had to {verb2} {adverb2} to catch our bus. When I got home I {verb3} my mom for a {adjective4} day at the zoo.") 
    engine.runAndWait()
    print(f"Today I went to the zoo. I saw a {adjective1} {noun1} jumping up and down in its tree. He {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. I got some peanuts and passed them through the cage to a gigantic gray {noun2} towering above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. It filled my stomach. Afterwards I had to {verb2} {adverb2} to catch our bus. When I got home I {verb3} my mom for a {adjective4} day at the zoo.")