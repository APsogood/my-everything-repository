def adventure_game():
    print("Welcome to the game Quest of Epicness this game is still getting update!")
    print("You are in a dark forest. You can go left or right.")
    
    choice = input("Which direction do you choose? (left/right): ").lower()
    
    if choice == "left":
        decide = input("You walked left. You think something is following you... Will you (run) or (find out what it is)?").lower()
    if decide == "run":
        pass
    elif decide == "find out what it is":
        pass
    elif choice == "right":
        print("You walked right. Rest to be continued.")
    else:
        print("Invalid choice. You wander around and get eaten by a giant bird. You lose!")

adventure_game()
