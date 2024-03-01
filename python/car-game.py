# If help required, type in help. It will give a list of commands
command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print("Car has already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit")
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that!")