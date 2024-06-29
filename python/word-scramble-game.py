import random

def show_rules():
    print("These are the rules:")
    print("1. You will have 4 rounds in this game.")
    print("2. If you guess the correct word then you will get 1 point.")
    print("3. If you didn't guess the correct word then you will get 0 points.")
    print("Good luck!!!")

def start_game():
    words_tuple = ("Giraffe", "Laptop", "Garage", "Marathon", "Medium", "Chicken", "School", "Random", "Antarctica", "Scramble", "Telephone", "Airplane", "Critical", "Microwave", "Chair")
    
    used_words = set()
    points = 0
    rounds = 4
    
    for i in range(1, rounds + 1):
        while True:
            word = random.choice(words_tuple).upper()
            if word not in used_words:
                used_words.add(word)
                break
        
        computer_word = word
        scrambled_word = ''.join(random.sample(word, len(word)))
        
        print(f"ROUND - {i}")
        print(f"Scrambled word: {scrambled_word}")

        user_word = input("Guess the word: ").upper()

        if user_word == computer_word:
            points += 1
            print("You guessed the correct word!")
        else:
            print(f"You didn't guess the word. The correct word was: {computer_word}")
    
    print(f"Game over! Your total points: {points}")

def main():
    show_rules()
    
    inp = input("Enter any key except (n/N) to start the game: ")
    
    if inp.lower() == 'n':
        print("Please don't type in (n/N). Let's try that again.")
        return
    
    start_game()

if __name__ == "__main__":
    main()
