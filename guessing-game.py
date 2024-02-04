print("This is a guessing game and you need to guess the secret number! Are you able to do it? And please give a star and follow me. Now let-'s guess!!!\n")

import random

def guessing_game():
    secret_number = random.randint(1, 10)
    
    attempts = 0
    
    
    while True:
        guess = int(input("Guess a number between 1 and 10: \n"))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!\n")
            break

guessing_game()
