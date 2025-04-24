def repeat_string():
    user_string = input("Please enter a word: ")

    while True:
        try:
            repeat_count = int(input("Please enter a number to print repeat the word: "))
            if repeat_count < 0:
                print("The number should be non-negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(repeat_count):
        print(user_string)


repeat_string()
