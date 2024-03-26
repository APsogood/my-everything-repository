weight_input = input("Enter the weight of a 1 to 10-year-old kid: ")

if weight_input.isdigit():  # Check if input consists of only digits
    weight = int(weight_input)
    if weight > 10:
        print(f"{weight} is too high of a number.")
    elif weight < 1:
        print(f"{weight} is too low of a number.")
    else:
        print(f"{weight} is within the valid range.")
        if weight == 1:
            print("An average weight for boys is 9.6 kgs or 21 pounds. For girls, an average weight is 8.9 kgs or 19 pounds.")
        elif weight == 2:
            print("For an average boy they should weight 11 to 14 kgs or 21 33.5 pounds")
        elif weight == 3:
            print("For an average boy they should weight 15 to 17 kgs or 33 to 37.5 pounds")
        elif weight == 4:
            print("For an average boy they should weight 16 to 19 kgs or 35.5 to 42 pounds")
        elif weight == 5:
            print("For an average boy they should weight 18 to 22 kgs or 39.5 to 48.5 pounds")
        elif weight == 6:
            print("For an average boy they should weight 20 to 25 kgs or 44 to 55 pounds")
        elif weight == 7:
            print("For an average boy they should weight 22 to 27 kgs or 48.5 to 59.5 pounds")
        elif weight == 8:
            print("For an average boy they should weight 24 to 29 kgs or 53 to 64 pounds")
        elif weight == 9:
            print("For an average boy they should weight 26 to 31 kgs or 57 to 68.5 pounds")
        elif weight == 10:
            print("For an average boy they should weight 27 to 33 kgs or 59.5 to 73 pounds")
else:
    print(f"'{weight_input}' is not a valid answer.")
