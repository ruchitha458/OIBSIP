import string
import random

def get_valid_length():
    while True:
        length_str = input("Enter password length: ")
        if length_str.isdigit():
            length = int(length_str)
            if length > 0:
                return length
            else:
                print("Password length must be a positive integer.")
        else:
            print("Please enter a valid integer for password length.")

def get_character_set(characterList):
    print('''Choose character set for password from these : 
    1. Digits
    2. Letters
    3. Special characters
    4. Exit''')
    
    while True:
        choice_str = input("Pick a number: ")
        if choice_str.isdigit():
            choice = int(choice_str)
            if 1 <= choice <= 4:
                return choice, characterList
            else:
                print("Please pick a number between 1 and 4.")
        else:
            print("Please enter a valid integer.")

length = get_valid_length()
characterList = ""

while True:
    choice, characterList = get_character_set(characterList)
    if choice == 1:
        characterList += string.ascii_letters
    elif choice == 2:
        characterList += string.digits
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break

if characterList:
    password = ''.join(random.choice(characterList) for _ in range(length))
    print("The random password is:", password)
else:
    print("No character set selected. Exiting...")
