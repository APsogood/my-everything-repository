# Please don't put sensitive passwords like bank account passwords. This warning is for your safety.
master_pwd = input("What is the master password to check passwords and add passwords? ")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", passw)



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


# Please don't put sensitive passwords like bank account passwords. This warning is for your safety.
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter 'view' or 'add' or press 'q' to quit.")
# Please don't put sensitive passwords like bank account passwords. This warning is for your safety.