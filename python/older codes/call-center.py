while True:
    call = input("Hello! It seems you called to (renew a passport) or (rent a house). Which one do you want to do? \n")

    if call.lower() == "renew a passport":
        reply_2 = input("Okay the fee will be 50$ please pay. Just to make sure, are you sure you want to proceed with payment? (yes) or (no)\n")
        if reply_2.lower() == "yes":
            print("Okay, your passport will be sent to you in 2 weeks.\n")
            break
        elif reply_2.lower() == "no":
            print("Ok we will ask you the question again as you wish.\n")
            continue
        else:
            print("Invalid input. Let me ask the question again.\n")

    elif call.lower() == "rent a house":
        answer = input("You have chosen to rent a house. Would you like to rent a (small house for 1.5k) or a (medium house for 3.5k) or a (large house for 6.7k)? And don't forget you need to rent every 1 month!\n")
        if answer.lower() == "small house for 1.5k":
            print("The address is M93 HP1 on Duck Road. We will be waiting there for you to pay the rent!\n")
            break
        elif answer.lower() == "medium house for 3.5k":
            print("Good choice, The address is MJ3 JIA on Tree Street.")
            break



