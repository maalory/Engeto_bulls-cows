"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tomas Balak
email: tomasbalak@gmail.com
discord: Tomas Balak#tomasbalak
"""

import random
number = []
attempts = 0
spliter = "-" * 40

# generating random 4 digits number
def MakeNumber():
    global number
    number.clear()
    #1st digit cannot be 0
    first_digit = random.randrange(1,10)
    number.append(first_digit)
    #next 3 digits
    while len(number) < 4:
        x = random.randrange(0,10)
        if x not in number:
            number.append(x)
def WelcomeMessage():
    print("Hi there!")
    print(spliter)
    print("I've generated a random 4 digit number for you." + "\nLet's play a bulls and cows game.", ''.join(map(str,number))) #ZOBRAZÍ ČÍSLO
    print(spliter)

def ValidateInput(user_input): #user input check
    if len(user_input) != 4:
        print("Input must have exactly 4 digits.")
        return False
    if not user_input.isdigit():
        print("Input must contain only digits.")
        return False
    if user_input[0] == '0':
        print("Input cannot start with zero.")
        return False
    if len(user_input) != len(set(user_input)):
        print("Input contains duplicate digits.")
        return False
    return True

def PlayGame(): #spustí hru
    global attempts
    attempts = 0
    while True:
        user_input = input("Enter a number: ")
        if ValidateInput(user_input):
            attempts += 1
            guess = [int(digit) for digit in user_input]
            bulls, cows = 0, 0
            used_indices_number = []

            # Výpočet bulls a cows
            for i in range(4):
                if guess[i] == number[i]:
                    bulls += 1
                else:
                    for j in range(4):
                        if guess[i] == number[j] and j not in used_indices_number and guess[j] != number[j]:
                            cows += 1
                            used_indices_number.append(j)
                            break
            bull_text = "bull" if bulls <= 1 else "bulls"
            cow_text = "cow" if cows <= 1 else "cows"
            print(f"{bulls} {bull_text}, {cows} {cow_text}")

            if bulls == 4:
                print(f"You won after {attempts} attempts!")
                break
MakeNumber()
WelcomeMessage()
PlayGame()
