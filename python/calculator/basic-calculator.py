print("Thank you for using my basic calculator. Please follow me and give this repository a like!!!\n")

while True:
    operator = input("Enter an operator (addition, subtraction, multiplication, or division): ").lower()
    if operator in ["addition", "subtraction", "multiplication", "division"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operator == "addition": # When the user inputs addition it does the addition same for everything
            result = num1 + num2
        elif operator == "subtraction":
            result = num1 - num2
        elif operator == "multiplication":
            result = num1 * num2
        elif operator == "division":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero")
                continue
        print("Result:", result)
        break
    els:
        print(f"{operator} is not a valid operator. Please try again.")