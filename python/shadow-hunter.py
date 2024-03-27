import time

has_vacuum = False
has_detector = False

while True:
    print()
    username = input("Welcome to Shadow Hunter. First you'll need to make a username. Enter your username (3 to 20 characters), but don't put your real name: ")

    if len(username) > 20:
        print("Username is too long. Please enter a username with 20 characters or fewer.\n")
    elif len(username) < 3:
        print("Username is too short. Please enter a username with at least 3 characters.\n")
    else:
        print(f"Hi {username}, we have been seeing shadows appearing and people have gone missing! You have to protect our village chief {username}")
        time.sleep(3)
        print("Tip: Shadow monsters don't attack during the day; they attack at night.")
        time.sleep(3)
        print("We can craft vacuum and shadow detector here. You can unlock more powerful weapons here.\n")
        time.sleep(3)
        
        if not has_detector:
            choice = input("Which one do you want to craft first, vacuum or shadow detector?: ").lower()
            if choice == "vacuum":
                print("Crafting your vacuum...")
                time.sleep(10)
                print("You've crafted a vacuum.")
                has_vacuum = True
            elif choice == "shadow detector":
                print("Crafting your shadow detector...")
                time.sleep(10)
                print("You've crafted a shadow detector.")
                has_detector = True
            else:
                print("Invalid choice. Please choose either vacuum or shadow detector.")
                continue
        elif not has_vacuum:
            print("Now let's craft a vacuum...")
            time.sleep(10)
            print("You've crafted a vacuum.")
            has_vacuum = True
        else:
            print("Now you will have to craft the next weapon.")
            time.sleep(2)
            print("Crafting your next weapon...")
            time.sleep(10)
            print("You've crafted the next weapon.")
