while True:
    question = input("What do you prefer, 'Basketball' or 'Soccer'? ").lower()
    if question == "soccer":
        outdoor_or_indoor = input("'Indoor soccer' or 'outdoor soccer'? ").lower()
        if outdoor_or_indoor == 'indoor soccer':
            name = input("What is your name? ")
            print(name.capitalize + ' likes ' + outdoor_or_indoor + '.')
            break
        elif outdoor_or_indoor == 'outdoor soccer':
            name_two = input("What is your name? ")
            print(name_two.capitalize + " likes " + outdoor_or_indoor)
            break
        else:
            print(f"Invalid choice: {outdoor_or_indoor}. Please choose 'Indoor soccer' or 'Outdoor soccer'.")
    elif question == "basketball":
        outdoor_or_indoor_two = input("Do you prefer 'outdoor basketball' or 'indoor basketball'? ").lower()
        if outdoor_or_indoor_two == "outdoor basketball":
            name_three = input("What is your name? ")
            print(name_three.capitalize + " likes " + outdoor_or_indoor_two + '.')
            break
        elif outdoor_or_indoor_two == "indoor basketball":
            name_four = input("What is your name? ")
            print(name_four.capitalize + " likes " + outdoor_or_indoor_two)
            break
        else:
            print(f"Invalid choice: {outdoor_or_indoor_two}. Please choose 'Indoor basketball' or 'Outdoor basketball'.")
    else:
        print(f"Invalid choice: {question}. Please choose 'Basketball' or 'Soccer'.")