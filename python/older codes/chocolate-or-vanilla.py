while True:
    question = input("What ice cream flavor do you prefer? Vanilla or Chocolate?\n")
    if question.lower() == "vanilla":
        print("Good choice. Vanilla ice cream is really good!\n")
        break
    elif question.lower() == "chocolate":
        print("Chocolate. You can never go wrong with chocolate. Good choice!\n")
        break
    else:
        print(f"{question} was not a proper answer. Let me ask again.\n")
