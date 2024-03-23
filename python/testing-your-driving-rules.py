while True:
    street = input("What do you do on a green light? 'stop' or 'go', or type 'quit' to exit: ").lower()
    
    if street == 'quit':
        print("You have chosen to quit. Exiting the program.\n")
        break
    
    if street == 'stop':
        print("That's incorrect. Let me ask you again:\n")
    elif street == 'go':
        correct = input("Correct. Now, what do you do on a red light: 'stop', 'go', or 'scream'? \n").lower()
        if correct == 'go':
            print("That's incorrect. I will have to ask you from the first question.\n")
        elif correct == 'scream':
            print("That's silly. That's incorrect.\n")
        elif correct == 'stop':
            smart = input("Correct, but one last question: Should you speed? 'Yes' or 'No'\n").lower()
            if smart == 'no':
                print("You got them all right! Good job!\n")
                break
        elif smart == 'yes':
            print("That's incorrect. You should never speed. I will have to reset you from the start.\n")
    else:
        print(f"{street} is not a valid operator. Please try again.\n")

