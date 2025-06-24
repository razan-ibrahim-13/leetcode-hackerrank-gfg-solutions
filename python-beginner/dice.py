import random

while True:
# This program simulates rolling a dice.
    choice= input("Do you want to roll the dice? (yes/no): ")

    if choice.lower() == 'yes':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"You rolled a {dice_1,dice_2}.")
    elif choice.lower() == 'no':
        print("Okay, maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
