#Author: Shane Kramer
#Date: 10/5/2017
#Descpt: Higher or Lower
#        The computer will generate a random number between 1-100
#        and you will have limited tries to guess it. It will give
#        you a hint to either guess higher or lower.
#
#Binary Search Algorithm: log (base2) 100 = 6.6 or roughly 7 guesses needed

import random

numTries = random.randint(3,10)
rNumber = random.randint(1,101)
print("I'm thinking of a number between 1-100. You have " + str(numTries) + " guesses.")

guess = int(input("First guess: "))
won = 0
for x in range(2, numTries):
    if(guess == rNumber):
        print("You guessed it! What are the odds!?")
        won = 1
        break
    elif(guess < rNumber):
        print("Sorry you are too low.")
    else:
        print("Sorry you are too high.")
    guess = int(input("Guess #" + str(x) + ":"))

if(won == 0):
    print("Sorry, you didn't guess it in " + str(numTries) + " tries. You lose.")

