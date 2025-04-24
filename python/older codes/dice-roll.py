import random
import time

def roll_dice():
    print("This dice only rolls numbers from 1 to 6.")
    roll = input("Do you wish to roll? (yes/no): ").lower()
    
    if roll == "yes":
        print("Rolling the dice...")
        time.sleep(2)
        number = random.randint(1, 6)
        print(f"Dice rolled! The number is {number}")
    elif roll == "no":
        print("As you wish.")
        return

roll_dice()