help = input("Welcome to math 1o! We are still developing our math questions. Need some help? Type in (math 1o help) for help! To play, type in (math questions) to answer the math questions! NOTE THAT THIS CODE IS STILL BEING PROGRAMMED! Game is not playable yet. ")

if help == "math 1o help":
    print("""1 - You will have math questions
             2 - Solve the math questions
             3 - You have to type the math questions in.
             3 - Try to get 10/10 questions correct. Good luck!""")
if help == "math questions":
    math_operations = input("What operation would you like to do (addition) or (subtraction)? ")
if math_operations == "addition":
    addition_yes_or_no = input("Are you sure you would like to addition? (yes) or (no) ")
    if addition_yes_or_no == "yes":
        questions = input("What is 35+35?")
        
    
    elif addition_yes_or_no == "no":
        print("As you wish.")
        quit
    
    
    
    
    elif math_operations == "subtraction":
        subtraction_yes_or_no = input("Are you sure you would like to do subtraction? (yes) or (no) ")
        if subtraction_yes_or_no == "yes":
            pass
        elif subtraction_yes_or_no == "no":
         print("As you wish.")
         quit
    
         
