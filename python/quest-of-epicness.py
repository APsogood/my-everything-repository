def adventure_game():
    print("Welcome to the game Quest of Epicness this game is still getting update!")
    print("You are in a dark forest. You can go left or right.")
    
    choice = input("Which direction do you choose? (left/right): ").lower()
    
    if choice == "left":
        print("You encounter a friendly dragon. He gives you treasure. You win!")
    elif choice == "right":
        print("You fall into a pit and stuck their forever. You lose!")
    else:
        print("Invalid choice. You wander around and find nothing. The game ends.")

adventure_game()
