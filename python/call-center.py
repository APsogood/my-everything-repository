while True:
    call = input("Hello! It seems you called to renew your (credit card) or (rent a house). Which one do you want to do? \n")

    if call.lower() == "credit card":
        reply = input("Okay, we will need to know which bank's credit card you need. Please specify: \n")
        reply_2 = input("So you need a " + reply + " credit card, is that correct? (yes) or (no) \n")
        if reply_2.lower() == "yes":
            print("Okay, your " + reply + " credit card will be sent to you in 2 weeks.\n")
            break
        elif reply_2.lower() == "no":
            print("Ok we will ask you the question again as you wish.\n")
            break
        else:
            print("Invalid input. Let me ask the question again.\n")

    elif call.lower() == "rent a house":
        answer = input("You have chosen to rent a house. Would you like to rent a (small house for 1.5k) or a (medium house for 3.5k) or a (large house for 6.7k)? And don't forget you need to rent the every 1 month!\n")
        if answer.lower() == "small house for 1.5k":
            print("The address is M93 HP1 on Duck Road. We will be waiting there for you to pay the rent!\n")
            break
        if answer.lower() == "medium house for 3.5k":
            print("Good choice, The address is MJ3 JIA on Tree Street. We will be waiting there for you to pay the rent!\n")
            break
        if answer.lower() == "large house for 6.7k":
            print("Amazing choice! The address is U8A HJ6 on King Street. We will be waiting there for you to pay the rent!\n")
            break

    else:
        print("Invalid option. Let me ask the question again.\n")

