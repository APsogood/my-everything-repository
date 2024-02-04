print("This is a weight converted. I took some time on this project so please give this a star and follow me!\n")

weight = float(input("What is your weight? "))
unit = input('Do you want your weight converted in (L)bs or (K)gs? ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.\n")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds.\n")