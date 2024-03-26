weight_input = input("Enter the weight of a 1 to 10-year-old kid: ")

if weight_input.isdigit():
    weight = int(weight_input)
    if weight > 10:
        print(f"{weight} is too high of a number.")
    elif weight < 1:
        print(f"{weight} is too low of a number.")
    else:
        print(f"{weight} is within the valid range.")
        if weight == 1:
            print("For boys: 9.6 kgs (21 pounds), For girls: 8.9 kgs (19 pounds)")
        elif weight == 2:
            print("For boys: 11 to 14 kgs (24.25 to 30.8 pounds), For girls: 10 to 13 kgs (22 to 28.6 pounds)")
        elif weight == 3:
            print("For boys: 15 to 17 kgs (33 to 37.5 pounds), For girls: 14 to 16 kgs (30.8 to 35.2 pounds)")
        elif weight == 4:
            print("For boys: 16 to 19 kgs (35.2 to 42 pounds), For girls: 15 to 18 kgs (33 to 39.6 pounds)")
        elif weight == 5:
            print("For boys: 18 to 22 kgs (39.6 to 48.5 pounds), For girls: 17 to 21 kgs (37.4 to 46.2 pounds)")
        elif weight == 6:
            print("For boys: 20 to 25 kgs (44 to 55 pounds), For girls: 19 to 24 kgs (41.8 to 52.8 pounds)")
        elif weight == 7:
            print("For boys: 22 to 27 kgs (48.5 to 59.5 pounds), For girls: 21 to 26 kgs (46.2 to 57.2 pounds)")
        elif weight == 8:
            print("For boys: 24 to 29 kgs (53 to 64 pounds), For girls: 23 to 28 kgs (50.6 to 61.6 pounds)")
        elif weight == 9:
            print("For boys: 26 to 31 kgs (57.2 to 68.5 pounds), For girls: 25 to 30 kgs (55 to 66 pounds)")
        elif weight == 10:
            print("For boys: 27 to 33 kgs (59.5 to 73 pounds), For girls: 26 to 32 kgs (57.2 to 70.4 pounds)")
else:
    print(f"'{weight_input}' is not a valid answer.")
