#Cory Cusick

import string
import random

length = int(input("What is the password length: "))

print('''Choose character set for password from these :
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""

# Get character set for password
while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):

        # Add letters to possible characters
        characterList += string.ascii_letters
    elif (choice == 2):

        # Add digits to possible characters
        characterList += string.digits
    elif (choice == 3):

        # Add special characters to possible
        characterList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    # Pick a random character from our
    # character list
    randomchar = random.choice(characterList)

    password.append(randomchar)

print("The random password is " + "".join(password))
