import datetime
import webbrowser
import random

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
        print("Enter the operation you want to perform (+, -, *, /): ")
        operation = input("Operation: ").strip()
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())
        
        if operation == '+':
            return f"The result is: {num1 + num2}"
        elif operation == '-':
            return f"The result is: {num1 - num2}"
        elif operation == '*':
            return f"The result is: {num1 * num2}"
        elif operation == '/':
            if num2 != 0:
                return f"The result is: {num1 / num2}"
            else:
                return "Error: Division by zero is not allowed."
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
    print("Enter the URL of the website you want to open (e.g., https://www.google.com): ")
    url = input("Website URL: ").strip()
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

def main():
    """Main function for the AI assistant."""
    print("Hello! I am your basic AI assistant.")
    print(greet_user())
    
    while True:
        print("\nWhat would you like me to do?")
        print("1. Perform a calculation")
        print("2. Get the current date and time")
        print("3. Open a website")
        print("4. Tell me a joke")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            print(perform_calculation())
        elif choice == '2':
            print(get_date_time())
        elif choice == '3':
            print(open_website())
        elif choice == '4':
            print(tell_joke())
        elif choice == '5':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
