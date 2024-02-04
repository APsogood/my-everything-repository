print("This is a guessing game and you need to guess the secret number! Are you able to do it? And please give a star and follow me.")

import random

def guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize the number of attempts
    attempts = 0
    
    print("I hope you enjoy my guessing game!")
    
    # Loop until the user guesses the correct number
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break

guessing_game()
