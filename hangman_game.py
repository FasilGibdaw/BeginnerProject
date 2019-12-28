# P5. This is probably the hardest one out of these 6 small projects. This will be similar to guessing the number,
# except we are guessing the word. The user needs to guess letters, Give the user no more than 6 attempts for guessing wrong letter.
# This will mean you will have to have a counter. You can download a 'sowpods' dictionary file or csv file to use as a way to get a random word to use.
# A script developed by Fasil Tesema, Longyearbyen, December 28 2019
from random import randint
with open("sowpods.txt", "r") as f:
    lines = [line.rstrip() for line in f]
num_guesses = 0
word_guess = randint(1, len(lines)+1)
#word_guess = 1
while num_guesses <= 5:
    num_guesses += 1
    guess = str(raw_input('enter the the word: '))
    if guess != lines[word_guess]:
        print('Wrong guess')
    elif guess == lines[word_guess]:
        print('you won! Congratulations')
        break
else:
    print('you reach your maximum number of guesses')
