import datetime
import webbrowser
import random  # Libraries

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
    print("Available operations: +, -, *, /")
    try:
        operation = input("Enter the operation: ").strip()
        if operation not in ['+', '-', '*', '/']:
            return "Invalid operation. Please choose from +, -, *, /."
        
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        
        return f"The result of {num1} {operation} {num2} is: {result}"
    except ValueError:
        return "Error: Please enter valid numbers."

def get_date_time():
    """Provide the current date and time."""
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def open_website():
    """Open a website in the default browser."""
    url = input("Enter the URL of the website (e.g., google.com): ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        webbrowser.open(url)
        return f"Opening {url} in your browser..."
    except Exception as e:
        return f"Error: Could not open the website. Reason: {e}"

def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
    ]
    return random.choice(jokes)

def tell_fact():
    """Tell a random fact about Canada or the United States."""
    canada_facts = [
        "Canada's national dish is poutine.",
        "Canada and the US share the world's longest border.",
        "New York City's GDP surpasses all of Canada's GDP.",
    ]
    
    us_facts = [
        "The United States has 50 states.",
        "The US Constitution is the oldest written constitution still in use.",
        "Yellowstone was the first national park in the world, established in 1872.",
    ]
    
    all_facts = canada_facts + us_facts
    return random.choice(all_facts)

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
5. Share a fact
6. Play Rock-Paper-Scissors
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
            print(tell_fact())
        elif choice == '6':
            print(play_rock_paper_scissors())
        elif choice == '7':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
