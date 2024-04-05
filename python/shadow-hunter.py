import time

username = ""
gold = 300
has_vacuum = False
has_detector = False

def craft_weapons():
    global gold, has_vacuum, has_detector
    while True:
        choice = input("Which one do you want to craft first, vacuum or shadow detector? ").lower()
        if choice == "vacuum":
            if gold >= 100:
                print("Crafting your vacuum...")
                start_time = time.time()  # Record start time
                time.sleep(10)  # Simulate crafting time
                end_time = time.time()  # Record end time
                print("You've crafted a vacuum.")
                has_vacuum = True
                gold -= 100
                print(f"Crafting took {end_time - start_time:.2f} seconds.")  # Calculate and display crafting time
                return True
            else:
                print("Not enough gold.")
        elif choice == "shadow detector":
            if gold >= 100:
                print("Crafting your shadow detector...")
                start_time = time.time()  # Record start time
                time.sleep(10)  # Simulate crafting time
                end_time = time.time()  # Record end time
                print("You've crafted a shadow detector.")
                has_detector = True
                gold -= 100
                print(f"Crafting took {end_time - start_time:.2f} seconds.")  # Calculate and display crafting time
                return True
            else:
                print("Not enough gold.")
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
            print("Type quit if you want to exit the game.")
            time.sleep(3)
            print("You currently have", gold, "gold.")

    if not has_detector or not has_vacuum:
        if not craft_weapons():
            continue
    else:
        print("Now, we need to find the shadow monster that caused this problem. Don't worry! It will be easy with the shadow detector.")
        time.sleep(3)
        print("It's us the shadow monsters if you want to go anywhere else you will have to go through me.")
        print("Now, let's start this battle!")
        shadow_hp = 100
        player_hp = 300
        extreme_winds = 50
        whirlwind_blow = 75
        attack = input("What ability do you want to use? 'extreme winds' or 'whirlwind blow'?").lower()
        if attack == "extreme winds":
            print(f"You dealt {extreme_winds} damage.")
            shadow_hp -= extreme_winds




