#Guess the number game. so much fun!

import random

print('hello! what is your name?')
name = input()

secretNumber = random.randint(1,100)

print(name + ', I am thinking of a number between 1 and 100. Try to guess it in six guesses.')

for guessesTaken in range(1,10):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break

if guess == secretNumber:
    print("Holy crap! You got it, " + name + "! It took you " + str(guessesTaken) + " guesses to do it.")
else:
    print('Darn! Better luck next time. The number was ' + str(secretNumber))
    
