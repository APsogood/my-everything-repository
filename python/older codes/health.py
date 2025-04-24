prompt_displayed = True

while True:
    if prompt_displayed:
        first = input("You came to the right place! Do you want to do 'weight loss' tips, 'healthy eating' tips, or 'dieting' tips? ")
    else:
        first = input()

    first = first.lower()  # Convert user input to lowercase
    
    if first == "weight loss":
        print("So you want to do weight loss, eh? Good choice. I recommend this diet: In the morning, eat something low in carbs and sugar. Stay hungry until 3pm or 4pm, then have a light snack or dinner. If you feel hungry later, you can eat a piece of fruit or a vegetable.")
        break
    elif first == "healthy eating":
        print("Healthy eating, not bad! I recommend eating fewer carbs and more vegetables than fruits.")
        break
    elif first == "dieting":
        print("Good choice! For dieting, in the morning eat some fruits and vegetables or low-carb foods and low sugar or no sugar foods. Stay hungry until your usual dinner time. If you're still hungry after dinner, have some fruits or vegetables.")
        break
    else:
        print("Invalid input. Please choose one of the options: 'healthy eating', 'weight loss', or 'dieting'.")
        prompt_displayed = False
