# Lab Exercise 3: Dice Simulator Using Random Module

import random

print("----- Dice Simulator -----")

while True:
    print("\n1. Roll the Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Generate a random number between 1 and 6
        dice = random.randint(1, 6)

        print("You rolled:", dice)

    elif choice == "2":
        print("Thank you for using Dice Simulator!")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")