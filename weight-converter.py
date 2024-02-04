print("This is a weight converter. I took some time on this project so please give this a star and follow me! \n")

weight = float(input("What is your weight? \n"))
unit = input('Do you want your weight converted in (L)bs or (K)gs? \n')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos. \n")
else:
    converted = weight / 0.45 
    print(f"You are {converted} pounds. \n")

print("Thanks for using my weight converter and please give this code a star and follow me. Have a great day! \n")