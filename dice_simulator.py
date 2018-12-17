"""Dice Simulator"""

import os
import random


def display_title():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')
    print("""
╔═════════════════════════════════════════════════════╗
║                    Dice Simulator                   ║
╚═════════════════════════════════════════════════════╝
""")


def get_user_choice():
    # Let users know what they can do.
    print("""
[1] Roll a D6.
[2] Roll a D8.
[3] Roll a D10.
[4] Roll a D20.
[5] Roll a D50.
[6] Roll a D100.
[7] Roll a custom dice.
[q] Quit.
""")
    return input("What would you like to do? ")


choice = ''
display_title()
while choice != 'q':

    max_value = 0
    choice = get_user_choice()
    # Respond to the user's choice.
    display_title()
    if choice == '1':
        max_value = 6
    elif choice == '2':
        max_value = 8
    elif choice == '3':
        max_value = 10
    elif choice == '4':
        max_value = 20
    elif choice == '5':
        max_value = 50
    elif choice == '6':
        max_value = 100
    elif choice == '7':
        max_value = int(input("Whats the desired size of the dice? "))
    elif choice == 'q':
        print("Thanks for playing. See you next time.\n")
        os.system('pause')
    else:
        print("Invalid choice.")

    if max_value > 0:
        dice = random.randint(1, max_value)
        print(f"The result is: {dice}")
        if choice == '4':
            if dice == 1:
                print("Tough luck!")
            elif dice == 20:
                print("Jackpot!")
