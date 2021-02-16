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
            print("Please enter valid inputs (Either \"yes\" or \"no\")")

    # Setting the characteristics of the password
    def setLength(self):
        size = int(input("Length: "))
        self.length = size

    def setUpper(self):
        addupper = input("Uppercase Letters (Y/N): ")
        self.upper = self.checkInput(addupper)

    def setLower(self):
        addlower = input("Lowercase Letters (Y/N): ")
        self.lower = self.checkInput(addlower)

    def setNumber(self):
        addnumber = input("Numbers (Y/N): ")
        self.number = self.checkInput(addnumber)

    def setSpecial(self):
        addspecial = input("Special Characters (Y/N): ")
        self.special = self.checkInput(addspecial)

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
        if (self.upper == False and self.lower == False and self.number == False and self.special == False):
            print("Oh no! You didn't say yes for any of the characteristics!\nPassword Generation Failed")
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
        print("Please enter valid inputs (Either \"yes\" or \"no\" for at least one)")