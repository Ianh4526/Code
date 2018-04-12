# A Short Program: Guess the Number

#THIS IS A Guess THE NUMBER GAME

import random

print('Hello. What is your name')
name = input()

print('well , ' + name + ' , I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print('take a guesse.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too High.')
    else:
        break # this condition is for the correct guess

if guess == secretNumber:
    print('Good job, '+ name + ' You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print(' NOPE!!!!   the number was:  '+ str(secretNumber))

print('You took  ' + str(guessesTaken) + '  guesses.')
