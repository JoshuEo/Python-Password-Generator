# STILL IN THE WORKINGS!
#
#
#

import click
import string
import random



# Constants
UPPER = list(string.ascii_uppercase)
LOWER = list(string.ascii_lowercase)
NUMBERS = list(string.digits)
SPECIAL = list(string.punctuation)
CHARTYPE = [UPPER, LOWER, NUMBERS, SPECIAL]

length = 10
upper = False
lower = False
number = False
special = False
chars = []

# Setting the characteristics of the password

@click.command()
@click.option("--length", "-L", "length", default=10, help="Length of password (Default: 10)")
@click.option("--upper", "-u", "upper", default=False, is_flag=True, help="Include uppercase characters in password")
@click.option("--lower", "-l", "lower", default=False, is_flag=True, help="Include lowercase characters in password")
@click.option("--number", "-n", "number", default=False, is_flag=True, help="Include numbers characters in password")
@click.option("--special", "-s", "special", default=False, is_flag=True, help="Include special characters in password")
def main(length, upper, lower, number, special):
    length = length
    upper = upper
    lower = lower
    number = number
    special = special

# Placing the user's preferred characteristics to a list
def chooseChars():
    usersCharacteristics = [upper, lower, number, special]
    index = 0
    for types in usersCharacteristics:
        if types == True:
            chars.append(CHARTYPE[index])
            index += 1
        else:
            index += 1
            continue

# Generating the password using random
def generate():
    newpass = ""
    if (upper == False and lower == False and number == False and special == False):
        print("Oh no! You didn't supply any options!\nPassword Generation Failed")
    for character in range(0, length):
        whichtype = random.choice(chars)
        character = random.choice(whichtype)
        newpass = newpass + character
    return newpass
    

if __name__ == "__main__":
    main(length, upper, lower, number, special)
    chooseChars()
    print(f"Generated Password: {generate()}")