# P1: Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high,
# or too low. This will get you started with the random library if you haven't already used it.
# A script developed by Fasil Tesema, Longyearbyen, December 28 2019
from random import randint
x = randint(0, 20)
guesses = 0
while guesses <= 5:
    guesses += 1
    guess = input('enter your guess as integer: ')
    if guess < x:
        print('guess is too low')
    elif guess > x:
        print('guess is too high')
    elif guess == x:
        print('You get it right. Congratulations!')
        break
else:
    print('you reached maximum number of guesses (6 guesses) ')
    print 'the secret number was', x

# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
# Such type of else is useful only if there is an if condition present inside the loop which somehow depends on the loop variable.
