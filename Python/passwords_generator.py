"""
This program can generate string passwords of the size you want
"""

import os
import string
import random

os.system("cls")

"""
With the string module we can generate de following lists in a simple manner
"""

lowercase_letters = list(string.ascii_lowercase)
capital_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)
characters = lowercase_letters + capital_letters + numbers + symbols


bander = False

while bander == False:
    try:
        size = int(input("How long do you want your password to be?: "))
        if size < 4 and size > 0:
            print("A strong password must be at least 4 characters long")
            print()
        elif size <= 0:
            print("No negative numbers allowed")
            print()
        else:
            bander = True
    except:
        print("The value entered is invalid")
        print()
        

password = [random.choice(lowercase_letters), random.choice(capital_letters), random.choice(numbers), random.choice(symbols)]

for i in range(size -4):
    character = random.choice(characters)
    password.append(character)

random.shuffle(password) #This is to mix the characters
password = "".join(password) #Convert the list to a string

print(f"Your passport is: {password}")