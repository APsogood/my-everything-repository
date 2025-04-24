import random

def show_rules():
    """Display the rules of the game."""
    print("\n=========== RULES ===========")
    print("1. You will have a number of rounds in this game.")
    print("2. If you guess the correct word, you earn 1 point.")
    print("3. If you don't guess correctly, you earn 0 points.")
    print("4. The words will be scrambled, and you need to guess the original word.")
    print("Good luck!\n")

def get_scrambled_word(word):
    """Return a scrambled version of the input word."""
    return ''.join(random.sample(word, len(word)))

def play_round(word, round_number):
    """Handle the logic for a single round of the game."""
    scrambled_word = get_scrambled_word(word)
    print(f"\nROUND {round_number}")
    print(f"Scrambled word: {scrambled_word}")

    user_guess = input("Guess the word: ").strip().upper()
    if user_guess == word:
        print("\nCorrect! You earned 1 point.")
        return 1
    else:
        print(f"\nIncorrect. The correct word was: {word}")
        return 0

def start_game():
    """Start the word scramble game."""
    words_tuple = (
        "Giraffe", "Laptop", "Garage", "Marathon", "Medium", "Chicken", "School", "Random", "Antarctica", "Scramble",
        "Telephone", "Airplane", "Critical", "Microwave", "Chair", "Avalanche", "Chocolate", "Monkey", "Examine",
        "Tentacle", "Frequency", "Driving", "Diving", "Cooking", "Cleaning", "Entrepreneur", "Excellent", "Extreme",
        "Whipped Cream", "Maple Syrup", "Multiplication", "Division", "Algebra", "Espresso", "Cappuccino", "Porridge",
        "Sentence", "Earthquake", "Fantastic", "Poison", "Discombobulated", "Comfort"
    )

    # Convert words to uppercase for uniformity
    words_list = [word.upper() for word in words_tuple]
    rounds = int(input("Enter the number of rounds you want to play (1-10): "))
    rounds = max(1, min(rounds, 10))  # Clamp rounds between 1 and 10

    used_words = set()
    total_points = 0

    for round_number in range(1, rounds + 1):
        # Pick a unique word that hasn't been used yet
        while True:
            word = random.choice(words_list)
            if word not in used_words:
                used_words.add(word)
                break

        # Play the round
        total_points += play_round(word, round_number)

    # Display final score
    print(f"\n=========== GAME OVER ===========")
    print(f"Your total points: {total_points}/{rounds}")

def main():
    """Main function to execute the game."""
    show_rules()

    while True:
        user_input = input("Enter any key to start the game or 'n' to exit: ").strip().lower()
        if user_input == 'n':
            print("\nThanks for playing! Goodbye!\n")
            break
        start_game()

if __name__ == "__main__":
    main()
