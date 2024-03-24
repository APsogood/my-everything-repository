while True:
    print()
    username = input("Welcome to Shadow Hunter. First you'll need to make a username. Enter your username (3 to 20 characters) don't put your real name: ")

    if len(username) > 20:
        print("Username is too long. Please enter a username with 20 characters or fewer.")
    elif len(username) < 3:
        print("Username is too short. Please enter a username with at least 3 characters.")
    else:
        print("Hi " + username + ", we have been seeing shadows appearing and people have gone missing! You have to protect our village chief " + username)
        print("We're the shadow monsters! Now you will have to face through me!")
        print("Tip: Shadow monsters don't attack at day they attack at night.")
        print("We have to go buy a shadow detector and a vacuum to suck them up and study them!")
        break

print("Hey! What weapon do you want to buy? (vacuum), (food), (shadow detector) and more coming soon.")
weapons = input()
