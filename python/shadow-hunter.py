import time

username = ""
gold = 300
has_vacuum = False
has_detector = False
shadow_hp = 100

def craft_weapons():
    global gold, has_vacuum, has_detector
    while True:
        choice = input("Which one do you want to craft first, vacuum or shadow detector? Type 'cancel' to cancel crafting: ").lower()
        if choice == "vacuum":
            if gold >= 100:
                print("Crafting your vacuum...")
                time.sleep(10)
                print("You've crafted a vacuum.")
                has_vacuum = True
                gold -= 100
                return True
            else:
                print("Not enough gold.")
        elif choice == "shadow detector":
            if gold >= 100:
                print("Crafting your shadow detector...")
                time.sleep(10)
                print("You've crafted a shadow detector.")
                has_detector = True
                gold -= 100
                return True
            else:
                print("Not enough gold.")
        elif choice == "cancel":
            print("Crafting canceled.")
            return False
        else:
            print("Invalid choice. Please choose either vacuum or shadow detector.")

while True:
    if not username:
        username = input("Welcome to Shadow Hunter. First you'll need to make a username. Enter your username (3 to 20 characters), but don't put your real name: ")

        if len(username) > 20:
            print("Username is too long. Please enter a username with 20 characters or fewer.\n")
            continue
        elif len(username) < 3:
            print("Username is too short. Please enter a username with at least 3 characters.\n")
            continue
        else:
            print(f"Hi {username}, we have been seeing shadows appearing and people have gone missing! You have to protect our village chief {username}")
            input("Press Enter to continue...")
            time.sleep(3)
            print("Tip: Shadow monsters don't attack during the day; they attack at night.")
            input("Press Enter to continue...")
            time.sleep(3)
            print("We can craft vacuum and shadow detector here. You can unlock more powerful weapons here.\n")
            input("Press Enter to continue...")
            time.sleep(3)
            print("You currently have", gold, "gold.")

    if not has_detector or not has_vacuum:
        if not craft_weapons():
            continue
    else:
        print("It's us the shadow monster! Now you will have to attack me.")
        time.sleep(3)
        print("Now, let's start this battle!")

