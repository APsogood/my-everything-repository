print("This quiz has 15 questions. Can you get them all correct?")
questions = ("1How many elements are in the periodic table?: ",
             "2What animal lays the largest eggs?: ",
             "3What is the most abundant gas in Earth's atmosphere?: ",
             "4Who found out about gravity?: ",
             "5What is the hottest planet in our solar system?: ",
             "6Who made the first phone?: ",
             "7Who made the first car?: ",
             "8How many eggs are in a carton of a dozen eggs?: ",
             "9What is the Earth's core temperature?: ",
             "10Who made the company Apple?: ",
             "11Who was the first person to land on our moon?: ",
             "12What meat is eaten the most around the world?: ",
             "13Who made the first computer?: ",
             "14How many seeds are in a cherry?: ", 
             "BONUS what was discovered first? Uranus or Antarctica: ")

options = (("1A. 116", "B. 117", "C. 118", "D. 119"),
           ("2A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("3A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
           ("4A. Isaac Newton", "B. Abraham Lincoln", "C. Thomas Edison", "D. Charles Goodyear"), 
           ("5A. Mercury", "B. Venus", "C. Earth", "D. Mars"), 
           ("6A. James Cope", "B. Alexander Graham Bell", "C. Domingo Pelliza", "D. Joseph Adams"), 
           ("7A. Carl/Karl Benz", "B. Albert Einstein", "C. Amelia Earhart", "D. Vincent van Gogh"), 
           ("8A. 12", "B. 15", "C. 14", "D. 17"), 
           ("9A. 100,000° Celsius (180032° Fahrenheit)", "B. 10,000° Celsius (18032° Fahrenheit)", "C. 1000° Celsius (1832° Fahrenheit)", "D. 5,200° Celsius (9,392° Fahrenheit)"), 
           ("10A. Oscar Williams", "B. Spencer Tracy", "C. Agnes Moorehead", "D. Steve Jobs"), 
           ("11A. Buzz Aldrin", "B. Charles Pete", "C. Neil Armstrong", "D. Alan LaVern Bean"), 
           ("12A. Chicken", "B. Beef", "C. Pork", "D. Steak"), 
           ("13A. Nikola Tesla", "B. Coco Chanel", "C. Charles Babbage", "D. Jelly Roll Morton"), 
           ("14A. 3", "B. 1", "C. 17", "D. 100"), 
           ("15A. Uranus", "Antarctica"))


answers = ()
guesses = []
score = 0
question_num = 0