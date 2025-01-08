import datetime  # For date and time
import webbrowser  # For opening websites
import random  # For random selections

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
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation not in ['+', '-', '*', '/']:
            return "Invalid operation. Please choose from +, -, *, /."

        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())

        if operation == '/' and num2 == 0:
            return "Error: Division by zero is not allowed."

        result = {
            '+': num1 + num2,
            '-': num1 - num2,
            '*': num1 * num2,
            '/': num1 / num2
        }[operation]

        return f"The result of {num1} {operation} {num2} is: {result}"
    except ValueError:
        return "Error: Please enter valid numbers."

def get_date_time():
    """Provide the current date and time."""
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def open_website():
    """Open a website in the default browser."""
    url = input("Enter the URL of the website (default: google.com): ").strip() or "google.com"
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    if "." not in url:  # Basic validation for a domain
        return "Invalid URL. Please enter a valid website."
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
    """Tell a fact about a selected location."""
    locations = {
        '1': ["Canada's national dish is poutine.", "Canada shares the longest border with the US."],
        '2': ["The US has 50 states.", "Yellowstone was the first national park in the world."],
        '3': ["China's national animal is the giant panda.", "The Great Wall of China is over 13,000 miles long."],
        '4': ["India is the largest democracy in the world.", "India has the world's tallest statue, the Statue of Unity."],
        '5': ["Russia spans 11 time zones.", "Lake Baikal in Russia is the deepest freshwater lake."],
        '6': ["Miami is the 'Cruise Capital of the World.'", "Miami has the largest collection of Art Deco buildings."],
        '7': ["Nassau is the capital of the Bahamas.", "The Bahamas became independent in 1973."]
    }

    print("\nChoose a location to hear a fact:")
    for key, value in locations.items():
        print(f"{key}. {value[0].split()[0]}")

    choice = input("Enter your choice (1-7): ").strip()
    if choice in locations:
        return random.choice(locations[choice])
    else:
        return "Invalid choice. Please select a valid option."

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

    menu = {
        '1': perform_calculation,
        '2': get_date_time,
        '3': open_website,
        '4': tell_joke,
        '5': tell_fact,
        '6': play_rock_paper_scissors,
    }

    while True:
        print("\nWhat would you like me to do?")
        for option, func in menu.items():
            print(f"{option}. {func.__doc__.strip()}")

        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '7':
            print("Goodbye! Have a great day!")
            break
        elif choice in menu:
            try:
                print(menu[choice]())
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
