import random


def readIntFromUserInput():
    while True:
        guess = input('Please enter a number:')
        try:
            return int(guess)
        except ValueError:
            print('Incorrect input.s')


print('Welcome to Guess Game!')
print('Computer picks randomly integer from 1 to 100')
print('The goal is to guess the picked number. You will be prompted to help you to understand the trend.\n')
print('After the 1st guess\n\tyou will see "WARM!" if the guess is within 10 of the number\n\tyou will see "COLD!" if the guess is further than 10 away from the number.')
print('On all subsequent turns,\n\t"WARMER!" is shown if the guess is closer to the number than the previous guess\n\t"COLDER!" is shown if the guess is farther from the number than the previous guess.\n\t"WARM!" is shown if the guess is within 10 of the number.')
print('\n')

numberToGuess = random.randint(0,101)

guesses = []
# attempts = 0
while True:
    guess = readIntFromUserInput()
    guesses.append(guess)

    if guess == numberToGuess:
        print(f'You have found the picked number after {len(guesses)} attempts.')
        break
    elif guess < 1 or guess > 100:
        print('OUT OF BOUNDS')
    elif len(guesses) == 1:
        if abs(guess - numberToGuess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(guess - numberToGuess) > abs(guesses[-2] - numberToGuess):
            print('COLDER!')
        else:
            print('WARMER!')



