# P4. Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be, and how many letters and numbers they want in their password. 
# Have a mix of upper and lowercase letters, as well as numbers and symbols. 
# The password should be a minimum of 6 characters long.
# A script developed by Fasil Tesema, Longyearbyen, December 28 2019
from random import randint, sample, shuffle

letter_lower = 'abcdefghijklmnopqrstuvwxyz'
letter_upper = letter_lower.upper()
numbers = '0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#try:
while True:
    length_of_password = input('enter the length of password which is >= 4: ')
    sy, ll, ul, n = input(
        'enter how many symbols,lower letters, upper letters, and numbers in your password like a,b,c,d: ')
    password_length = [sy, ll, ul, n]
    if ll == 0 or sy == 0 or ul == 0 or n == 0:
        print('you have to include all the possibility of the password ')
    elif sum(password_length) == length_of_password:
        i = ''.join(sample(symbols, sy))
        j = ''.join(sample(letter_lower, ll))
        k = ''.join(sample(letter_upper, ul))
        l = ''.join(sample(numbers, n))
        print 'your password is', ''.join(sample(''.join([i, j, k, l]), length_of_password)) # join the poossible combination and shuffle it randomly
        break
   # else:
     #   print('your password length should be at most 6 characters long')
      #  continue
#except (ValueError, NameError):
    #print('inputs must be four integers')
    # print(sample(letter_lower, 3))
