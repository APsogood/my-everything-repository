age = int(input("Enter your age: "))

while True:
    if_has_kids = input("Does your kids have kids? (yes/no): ").lower()
    if if_has_kids == "yes":
        while True:
            gender = input("Are you a boy or a girl? ").lower()
            if gender == "boy" or gender == "girl":
                break
            else:
                print("Please enter 'boy' or 'girl'.")
        break
    elif if_has_kids == "no":
        break
    else:
        print("Please enter 'yes' or 'no'.")

if age < 1:
    print("You're a baby.\n")
elif age < 3:
    print("You're a toddler.\n")
elif age < 5:
    print("You're a kid.\n")
elif age < 13:
    print("You're a teenager.\n")
elif age < 18:
    print("You're an adult.\n")
else:
    if if_has_kids == "yes":
        if gender == "boy":
            print("You're a grandpa.\n")
        else:
            print("You're a grandma.\n")
    else:
        print("You're an adult.\n")