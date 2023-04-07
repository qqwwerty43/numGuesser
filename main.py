from random import randint

RandomNumber = 0
trying = 0
rightBorder = 0
print("Hi! Welcome to numGuesser")
name = str(input("Enter your name: "))


def newgame(fname):
    n = ''
    while not is_digit(n):
        n = str(input(f'{fname}, enter the right border: '))
    randomnumber = randint(1, int(n))
    tryin = 0
    return int(n), randomnumber, tryin


def is_digit(a):
    if a.isdigit():
        return 1
    else:
        return 0

rightBorder, RandomNumber, trying = newgame(name)

while True:
    YourNumber = input(f'{name}, enter a number from 1 to {rightBorder}: ')
    if not is_digit(YourNumber):
        continue
    else:
        YourNumber = int(YourNumber)
        trying += 1
        if YourNumber > RandomNumber:
            print("Your number is greater than expected. Let's try again!")
        elif YourNumber < RandomNumber:
            print("Your number is less than expected. Let's try again!")
        else:
            print(f'Congratulations, you guessed the number!\nAttempts: {trying}')
            result = str(input(f'Do you wanna play again, {name}? Y/N: '))
            if result == 'N':
                break
            else:
                rightBorder, RandomNumber, trying = newgame(name)

