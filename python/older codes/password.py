while True:
    password = input("Put a password. Say 'quit' if you want to quit: ").lower()
    
    if password == 'quit':
        print("As you wish.")
        break
    
    elif len(password) < 8:
        print("Too short!")
    
    elif len(password) > 8:
        password_2 = input("Good, now make a password that includes special characters (!@#$%^&*_+/): ")
        
        if any(char in "!@#$%^&*_+/" for char in password_2):
            print("Good password.")
        else:
            print("Password must include at least one special character!")
