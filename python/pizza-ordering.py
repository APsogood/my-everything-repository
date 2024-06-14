import time

while True:
    question = input("What pizza restaurant are you ordering from? ")
    
    print('Calling...')
    time.sleep(3)
    
    while True:
        greeting = input("Hello! Welcome to " + question + ". What pizza would you like to order: 'cheese' or 'pepperoni'? ")
        
        if greeting.lower() == "cheese":
            print("Thank you for placing your order. Come to your nearest " + question + " store and pay for your pizza!")
            break
        elif greeting.lower() == "pepperoni":
            print("Thank you for placing your order. Come to your nearest " + question + " store and pay for your pizza!")
            break
        else:
            print("Invalid choice. Please choose either 'cheese' or 'pepperoni'.")

    break

