import random

options = ("rock", "paper", "scissors")
playing = True
while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock), (paper), (scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        playing = False

print("Thanks for playing!")
