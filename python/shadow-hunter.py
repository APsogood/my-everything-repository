import time
import random

username = ""
gold = 300
has_vacuum = False
has_detector = False
crafted_items = []

def craft_weapons():
    global gold, has_vacuum, has_detector, crafted_items
    while True:
        choice = input("Which one do you want to craft first, vacuum or shadow detector? \n").lower()
        if choice == "vacuum" and "vacuum" not in crafted_items:
            if gold >= 100:
                print("Crafting your vacuum...\n")
                start_time = time.time()
                time.sleep(10)
                end_time = time.time()
                print("You've crafted a vacuum.\n")
                has_vacuum = True
                gold -= 100
                crafted_items.append("vacuum")
                print(f"Crafting took {end_time - start_time:.2f} seconds.\n")
                return True
            else:
                print("Not enough gold.\n")
        elif choice == "shadow detector" and "shadow detector" not in crafted_items:
            if gold >= 100:
                print("Crafting your shadow detector...\n")
                start_time = time.time()
                time.sleep(10)
                end_time = time.time()
                print("You've crafted a shadow detector.\n")
                has_detector = True
                gold -= 100
                crafted_items.append("shadow detector")
                print(f"Crafting took {end_time - start_time:.2f} seconds.\n")
                return True
            else:
                print("Not enough gold.\n")
        elif choice in crafted_items:
            print("You've already crafted this item.\n")
        else:
            print("Invalid choice. Please choose either vacuum or shadow detector.\n")

def player_attack():
    return random.randint(50, 100)

def shadow_attack():
    return random.randint(30, 70)

def battle():
    global gold, has_detector, has_vacuum
    print("Now, we need to find the shadow monster that caused this problem. Don't worry! It will be easy with the shadow detector.\n")
    time.sleep(3)
    print("It's us, the shadow monsters. If you want to go anywhere else, you will have to go through me.\n")
    print("Now, let's start this battle!\n")
    shadow_hp = 100
    player_hp = 300
    while shadow_hp > 0 and player_hp > 0:
        # Determine who attacks first
        first_attack = random.choice(["player", "shadow"])
        if first_attack == "player":
            print("You attack first!\n")
            player_damage = player_attack()
            print(f"You dealt {player_damage} damage to the shadow!\n")
            shadow_hp -= player_damage
        else:
            print("The shadow attacks first!\n")
        while True:
            attack = input("What ability do you want to use? 'extreme winds' or 'whirlwind blow'? \n").lower()
            if attack == "extreme winds":
                print("You use extreme winds!\n")
                shadow_hp -= 50
                break
            elif attack == "whirlwind blow":
                print("You use whirlwind blow!\n")
                shadow_hp -= 75
                break
            else:
                print("Invalid ability. Please choose 'extreme winds' or 'whirlwind blow'.\n")
        if shadow_hp <= 0:
            print("You defeated the shadow monster!\n")
            break
        print(f"The shadow's HP: {shadow_hp}\n")
        shadow_damage = shadow_attack()
        print(f"The shadow dealt {shadow_damage} damage to you!\n")
        player_hp -= shadow_damage
        print(f"Your HP: {player_hp}\n")
        if player_hp <= 0:
            print("You were defeated by the shadow monster!\n")
            break

while True:
    if not username:
        username = input("Welcome to Shadow Hunter. First, you'll need to make a username. Enter your username (3 to 20 characters), but don't use your real name: \n")

        if len(username) > 20:
            print("Username is too long. Please enter a username with 20 characters or fewer.\n")
            continue
        elif len(username) < 3:
            print("Username is too short. Please enter a username with at least 3 characters.\n")
            continue
        else:
            print(f"Hi {username}, we have been seeing shadows appearing and people have gone missing! You have to protect our village chief {username}.\n")
            input("Press Enter to continue...\n")
            time.sleep(3)
            print("Tip: Shadow monsters don't attack during the day; they attack at night.\n")
            input("Press Enter to continue...\n")
            time.sleep(3)
            print("We can craft a vacuum and a shadow detector here. You can unlock more powerful weapons here.\n")
            input("Press Enter to continue...\n")
            print("Type quit if you want to exit the game.\n")
            time.sleep(3)
            print("You currently have", gold, "gold.\n")

    if not has_detector or not has_vacuum:
        if not craft_weapons():
            continue
    else:
        battle()
