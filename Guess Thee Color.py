# This is a guess the color game.
from random import random
from typing import List

random()

print('Hello, What is your name?')
name = input()
print('Well ' + name, ' I am thinking of a color from the rainbow.')
colors: List[str] = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple']

for guessesTaken in ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple']:
    print('Take a guess')
    guess = str(input())

    if guess != colors:
        print('Sorry, your guess is wrong')
    elif guess > colors:
        print('Please try again')
    else:
        break  # This condition is for the correct guess.

if guess == colors:
    print('Great job, ' + name + '! You guessed my color in str(GuessesTaken) +  guesses!')
else:
    print('Nope. The color I was thinking of was ' + str(colors))
