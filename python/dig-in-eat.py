name = input("Welcome to Dig in Eat, what is your name so I can get your order? ")
greeted = False
order_total = 0
ordered_items = []

menu = "Pizza, Fish and Chips, Dumplings, Curry, Burrito, Spaghetti, Sushi, Burger, Salad, Tacos, Steak, Soup, Pancakes, Omelette, Stir-fry, Roast Beef, Lasagna, BBQ Ribs, Shawarma, Fish, Ramen, Pad Thai, Paella, Mild Chicken Sandwich, Spicy Chicken Sandwich, Fried Chicken, Cooked Chicken, Fried Lobster, Cooked Lobster, Grilled Cheese Sandwiches, Burger, Fries, Salad, Pizza, Sushi, Tacos, Burritos, Pasta, Soup, Steak, Ribs, Shrimp, Fish and Chips, Curry, Rice, Noodles, Shawarma, Kebab, Dumplings, Pancakes, Waffles, French Toast, Crepes, Omelette, Bacon, Sausages, Hash Browns, Eggs Benedict, Bagel, Croissant, Muffin, Donuts, Cupcakes, Brownies, Cookies, Ice Cream, Cake, Pie, Pudding, Milkshake, Smoothie, Tea, Coffee, Juice, Soda, Water, Beer, Wine, Cocktails"
menu_list = menu.lower().split(", ")

while True:
    if not greeted:
        print("Thank you so much for coming to Dig in Eat, " + name + "!\n")
        greeted = True

    if ordered_items:
        print("What else would you like to order? ")
    else:
        print("What would you like to order? ")

    print("This is our menu: " + menu + ".\nThere will be more items soon! Let me know what you'd like to order. ")

    while True:
        order = input().strip().lower().capitalize()
        if order.lower() in menu_list:
            break
        else:
            print("Sorry, that's not a valid item from the menu. Please choose again.")

    price = 10
    quantity = int(input("How many " + order + " would you like? \n"))
    total = price * quantity
    order_total += total
    print("Thank you. Your total is: $" + str(total) + "\n")

    ordered_items.append((order, quantity))

    choice = input = input("Would you like to order anything else? (yes/no) ")

    if choice.lower() == 'no':
        print("Sounds good, " + name + ", your total order price is: $" + str(order_total) + ". We'll have your order ready in a moment.\n")
        print("You ordered:" + "\n")
        for item in ordered_items:
            print(f"{item[1]} {item[0]}")
        break
    elif choice.lower() != 'yes':
        print("Sorry, I didn't understand that. Let's try again.\n")