def adventure_game():
    print("Welcome to the game Quest of Epicness this game is still getting update!")
    print("You are in a dark forest. You can go left or right.")
    
    choice = input("Which direction do you choose? (left/right): ").lower()
    
    if choice == "left":
        decide = input("You walked left. You think something is following you... Will you (run) or (find out what it is)?").lower()
    if decide == "run":
        print("You ran. Now the thing which was following you is not following you anymore ")
    elif decide == "find out what it is":
        print("An old man gave you a treasure chest! Rest to be continued...")
    elif choice == "right":
        eat = ("You walked right. You found a fruit. This one seems different... Eat or throw away?")
        if eat == "eat":
            print("Your body feels different... To be continued...")
        elif eat == "throw away":
            print("The fruit got thrown away. An old man said those can go around for 350,000,000 dollars and if consumed it is said to give you special super-human powers.")

    else:
        print("Invalid choice. You wander around and get eaten by a giant bird. You lose!")

adventure_game()
