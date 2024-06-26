print("This quiz has 15 questions. Can you get them all correct? If you decide to quit, Type quit")

questions = (
    "How many elements are in the periodic table?: ",
    "What animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "Who found out about gravity?: ",
    "What is the hottest planet in our solar system?: ",
    "Who made the first phone?: ",
    "Who made the first car?: ",
    "How many eggs are in 1 dozen of eggs?: ",
    "What is the Earth's core temperature?: ",
    "Who made the company Apple?: ",
    "Who was the first person to land on our moon?: ",
    "What meat is eaten the most around the world?: ",
    "Who made the first computer?: ",
    "How many countries are there on Earth?: ",
    "BONUS what was discovered last? Uranus or Antarctica: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. Isaac Newton", "B. Abraham Lincoln", "C. Thomas Edison", "D. Charles Goodyear"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. James Cope", "B. Alexander Graham Bell", "C. Domingo Pelliza", "D. Joseph Adams"),
    ("A. Vincent van Gogh", "B. Albert Einstein", "C. Amelia Earhart", "D. Carl/Karl Benz"),
    ("A. 12", "B. 15", "C. 14", "D. 17"),
    ("A. 100,000° Celsius (180032° Fahrenheit)", "B. 10,000° Celsius (18032° Fahrenheit)", "C. 5,200° Celsius (9,392° Fahrenheit)", "D. 1000° Celsius (1832° Fahrenheit)"),
    ("A. Oscar Williams", "B. Spencer Tracy", "C. Agnes Moorehead", "D. Steve Jobs"),
    ("A. Buzz Aldrin", "B. Charles Pete", "C. Neil Armstrong", "D. Alan LaVern Bean"),
    ("A. Chicken", "B. Pork", "C. Beef", "D. Steak"),
    ("A. Nikola Tesla", "B. Coco Chanel", "C. Jelly Roll Morton", "D. Charles Babbage"),
    ("A. 195", "B. 194", "C. 176", "D. 165"),
    ("A. Uranus", "B. Antarctica")
)

answers = ("C", "D", "A", "A", "B", "B", "D", "A", "C", "D", "C", "B", "D", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D) or type 'quit' to exit: ").upper()

    if guess == 'QUIT'.upper():
        print("You have chosen to exit the quiz.")
        break
    
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("You are correct!")
    else:
        print(f"Sorry, but your answer is incorrect. The correct answer was{answers[question_num]} is the correct answer.")

    
    question_num += 1

print("-------------------------")
print(f"Your total score is: {score}/{question_num}")
