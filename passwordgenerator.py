import random
import string


class PasswordGenerator:

    # Constants
    UPPER = list(string.ascii_uppercase)
    LOWER = list(string.ascii_lowercase)
    NUMBERS = list(string.digits)
    SPECIAL = list(string.punctuation)
    CHARTYPE = [UPPER, LOWER, NUMBERS, SPECIAL]

    # Constructor
    def __init__(self):
        self.length = 0
        self.upper = False
        self.lower = False
        self.number = False
        self.special = False
        self.chars = []

    # Welcome Message
    def welcome(self):
        print("WELCOME TO THE PYTHON PASSWORD GENERATOR!")
        print("-" * 45)
        print("Please enter the necessary characteristics you want the password to have:")

    # Check user input (Either if they said yes or no)
    def checkInput(self, value):
        """
        Allowed inputs (case insensitive):
        TRUE IF: y, yes, yesir, siryes
        FALSE IF: n, no, nosir, sirno
        """
        if value.upper() == "Y" or value.upper() == "YES" or "YES" in value.upper():
            return True
        elif value.upper() == "N" or value.upper() == "NO" or "NO" in value.upper():
            return False
        else:
            return "bad input"

    # Setting the characteristics of the password
    def setLength(self):
        print("You may have a minimum of 9 characters and a maximum of 100 (Only a wild man would dare to do 100!)")
        while True:
            try:
                size = int(input("Length: "))
                if size == 100:
                    print("You're crazy! No one will bypass your Netflix account!")
                    self.length = size
                    break
                elif size > 8 and size < 101:
                    self.length = size
                    break
                else:
                    print("Please enter a numeric value between 9-100")
                    continue
            except ValueError:
                print("Please enter a numeric value between 9-100")
                continue

    def setUpper(self):
        while True:
            addupper = input("Uppercase Letters (Y/N): ")
            validator = self.checkInput(addupper)
            if isinstance(validator, bool):
                self.upper = validator
                break
            else:
                continue

    def setLower(self):
        while True:
            addlower = input("Lowercase Letters (Y/N): ")
            validator = self.checkInput(addlower)
            if isinstance(validator, bool):
                self.lower = validator
                break
            else:
                continue

    def setNumber(self):
        while True:
            addnumber = input("Numbers (Y/N): ")
            validator = self.checkInput(addnumber)
            if isinstance(validator, bool):
                self.number = validator
                break
            else:
                continue

    def setSpecial(self):
        while True:
            addspecial = input("Special Characters (Y/N): ")
            validator = self.checkInput(addspecial)
            if isinstance(validator, bool):
                self.special = validator
                break
            else:
                continue

    # Placing the user's preferred characteristics to a list
    def chooseChars(self):
        usersCharacteristics = [self.upper, self.lower, self.number, self.special]
        index = 0
        for types in usersCharacteristics:
            if types == True:
                self.chars.append(self.CHARTYPE[index])
                index += 1
            else:
                index += 1
                continue

    # Generating the password using random
    def generate(self):
        newpass = ""
        while True:
            if (self.upper == False and self.lower == False and self.number == False and self.special == False):
                print("Oh no! You didn't say yes for any of the characteristics!\nPassword Generation Failed")
                break
            for character in range(0, self.length):
                whichtype = random.choice(self.chars)
                character = random.choice(whichtype)
                newpass = newpass + character
            return newpass


if __name__ == "__main__":
    try:
        # Create an Password Generator Object -> Running all operations
        password = PasswordGenerator()
        password.welcome()
        password.setLength()
        password.setLower()
        password.setUpper()
        password.setNumber()
        password.setSpecial()
        password.chooseChars()
        print(f"Generated Password: {password.generate()}")
    except:
        print("Error, please run again")