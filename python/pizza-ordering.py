import time

while True:
    question = input("What pizza restaurant are you ordering from? ")
    
    print('Calling ' + question + '...')
    time.sleep(3)
    
    while True:
        greeting = input(f"Hello! Welcome to {question}. What pizza would you like to order: 'cheese' or 'pepperoni'? ")
        
        if greeting.lower() == "cheese" or greeting.lower() == "pepperoni":
            print(f"Thank you for placing your order. Come to your nearest {question} store and pay for your pizza!")
            break
        else:
            print("Invalid choice. Please choose either 'cheese' or 'pepperoni'.")

    break
