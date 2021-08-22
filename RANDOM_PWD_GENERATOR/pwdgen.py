#!/usr/bin/env python 3

# Imports
import random, string

if __name__ == "__main__":
    # Get ASCII characters (lowercase & uppercase letters, digits and special characters)
    letter = string.ascii_letters
    digits = string.digits
    punct = string.punctuation

    # Initialise password
    pwd = ''

    # Set password variables (length, number of digits and number of special characters)
    pwdLength = 12
    ranDig = random.randint(3,5)
    ranPunct = random.randint(3,5)

    # Generate password (set order : digits, special characters and letters)
    for i in range(ranDig):
        pwd += random.choice(digits)
    for i in range(ranPunct):
        pwd += random.choice(punct)
    for i in range(pwdLength - (ranDig + ranPunct)):
        pwd += random.choice(letter)
    
    # Randomise password characters
    pwd = list(pwd)
    random.shuffle(pwd)

    # Display generated password
    print(''.join(pwd))
