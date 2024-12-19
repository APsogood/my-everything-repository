import datetime
import webbrowser
import random # Libraries

def greet_user():
    """Greet the user based on the time of day."""
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def perform_calculation():
    """Perform basic arithmetic operations."""
    try:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
        
        if operation == '+':
            return f"The result is: {num1 + num2}"
        elif operation == '-':
            return f"The result is: {num1 - num2}"
        elif operation == '*':
            return f"The result is: {num1 * num2}"
        elif operation == '/':
            return f"The result is: {num1 / num2}" if num2 != 0 else "Error: Division by zero."
        else:
            return "Invalid operation. Please try again."
    except ValueError:
        return "Error: Please enter valid numbers."

def get_date_time():
    """Provide the current date and time."""
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def open_website():
    """Open a website in the default browser."""
    url = input("Enter the URL of the website (e.g., https://www.google.com): ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    try:
        webbrowser.open(url)
        return f"Opening {url}..."
    except Exception as e:
        return f"Error: Could not open the website. {e}"

def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
    ]
    return random.choice(jokes)

def facts():
    """Tell facts about Canada."""
    fact_list = [
        "Canada's national dish is poutine.",
        "Canada and the US share the world's longest border.",
        "New York City's GDP surpasses all of Canada's GDP.",
    ]
    return random.choice(fact_list)

def play_rock_paper_scissors():
    """Play Rock-Paper-Scissors with the user."""
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if user_choice not in choices:
        return "Invalid choice. Please choose rock, paper, or scissors."
    
    ai_choice = random.choice(choices)
    print(f"AI chose: {ai_choice}")
    
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and ai_choice == "scissors") or \
         (user_choice == "scissors" and ai_choice == "paper") or \
         (user_choice == "paper" and ai_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    """Main function for the AI assistant."""
    print("Hello! I am your basic AI assistant.")
    print(greet_user())
    
    menu = """
What would you like me to do?
1. Perform a calculation
2. Get the current date and time
3. Open a website
4. Tell me a joke
5. Facts about Canada
6. Play rock-paper-scissors
7. Exit
"""
    
    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            print(perform_calculation())
        elif choice == '2':
            print(get_date_time())
        elif choice == '3':
            print(open_website())
        elif choice == '4':
            print(tell_joke())
        elif choice == '5':
            print(facts())
        elif choice == '6':
            print(play_rock_paper_scissors())
        elif choice == '7':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()