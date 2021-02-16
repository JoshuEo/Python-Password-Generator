import random


class PasswordGenerator:

    UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    SPECIAL = ["!", """, "#", "$", "%", "&", """, "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    chartype = [UPPER, LOWER, NUMBERS, SPECIAL]

    # Instance variables
    def __init__(self):
        self.length = 0
        self.upper = False
        self.lower = False
        self.number = False
        self.special = False
        self.chars = []

    def welcome(self):
        print("WELCOME TO THE PYTHON PASSWORD GENERATOR!")
        print("-" * 40)
        print("Please enter the necessary characteristics you want the password to have:")

    def checkInput(self, value):
        if value.upper() == "Y" or value.upper() == "YES":
            return True
        elif value.upper() == "N" or value.upper() == "NO":
            return False
        else:
            print("Please enter valid inputs (Either \"yes\" or \"no\")")

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
        addnumber = input("Add numbers? (Y/N): ")
        self.number = self.checkInput(addnumber)

    def setSpecial(self):
        addspecial = input("Add special characters? (Y/N): ")
        self.special = self.checkInput(addspecial)

    def chooseChars(self):
        usersCharacteristics = [self.upper, self.lower, self.number, self.special]
        index = 0
        for types in usersCharacteristics:
            if types == True:
                self.chars.append(self.chartype[index])
                index += 1
            else:
                index += 1
                continue

    def generate(self):
        newpass = ""
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
        print("Please enter valid inputs (Either \"yes\" or \"no\"")