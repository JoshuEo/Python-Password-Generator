"""
Todo list:
- Add a try..except block in if __name__ method
Questions:
- How do you have variables and call them through methods? (talking about UPPER, LOWER, )
Extra:
- Ask for a word - then we can translate it into something a little stronger
"""
import random


class PasswordGenerator:

    # Instance variables
    def __init__(self):
        self.length = 0
        self.number = False
        self.special = False
        self.chars = []

    def welcome(self):
        print("WELCOME TO THE PYTHON PASSWORD GENERATOR!")
        print("-" * 40)
        print("Please enter the necessary characteristics you want the password to have:")

    def setLength(self):
        size = int(input("Length: "))
        self.length = size

    def setNumber(self):
        addnumber = input("Add numbers? (Y/N): ")
        if addnumber.upper == "Y" or addnumber.upper == "YES":
            self.number = True
        elif addnumber.upper == "N" or addnumber.upper == "NO":
            self.number = False

    def setSpecial(self):
        addspecial = input("Add special characters? (Y/N): ")
        if addspecial.upper == "Y" or addspecial.upper == "YES":
            self.special = True
        elif addspecial.upper == "N" or addspecial.upper == "NO":
            self.special = False

    def chooseChars(self):
        pass

    def generate(self):
        # List of characters
        UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        SPECIAL = ["!", """, "#", "$", "%", "&", """, "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
        types = [UPPER, LOWER, NUMBERS, SPECIAL]
        newpass = ""
        
        for char in range(0, self.length):
            whichtype = random.choice(types)
            char = random.choice(whichtype)
            newpass = newpass + char
        return newpass


if __name__ == "__main__":
    # Create an Password Generator Object
    password = PasswordGenerator()
    password.welcome()
    password.setLength()
    password.setNumber()
    password.setSpecial()
    print(f"Generated Password: {password.generate()}")