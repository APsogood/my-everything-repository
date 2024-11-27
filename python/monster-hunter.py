import random
import time

word_tuple_easy = ("When", "Master", "Done", "Happy", "Help", "Find", "Read", "Feed", "March", "Fruit", "Simple", "Sharp", "Sheep", "Sleep", "Upset", "Then", "Runner", "Jump", "Rabbit", "Great", "Happy")
word_tuple_medium = ("Monster", "Destroyer", "Monkey", "Marathon", "Fisherman", "Friendly", "Demolish", "Saskatchewan", "Television", "Giraffe", "Kangaroo", "Fighter Plane", "Flag Football", "Tetanus", "Excuses", "Married", "Explosion")
word_tuple_hard = ("Discombobulated", "Confusion", "Arachnophobia", "Megalophobia", "Microphobia", "Teraphobia", "Nyctophobia", "Hematophobia", "Aibohphobia")
word_tuple_extreme = ("Hippopotomonstrosesquippedaliophobia", "Lymphangioleiomyomatosis", "Supercalifragilisticexpialidocious")
word_tuple_unbeatable = ("Pneumonoultramicroscopicsilicovolcanoconiosis",)

welcome = input("Welcome to Monster Hunter! In this game, you need to type in a word within a certain amount of time. There are 3 difficulties: (Easy), (Medium), and (Hard). Type in (tutorial) to play the tutorial: ")

if welcome.lower() == "tutorial":
    print("This is the tutorial, so there will be no timer. Go!")
    points = 0

    word1 = input("Type in (cat). You have N/A seconds before the monster gets you. Go! ").lower()
    if word1 == "cat":
        print("Great job! +1 point.")
        points += 1
    else:
        print("Incorrect, still continue!")

    word2 = input("Type in (egg). You have N/A seconds before the monster gets to you. Go! ").lower()
    if word2 == "egg":
        print("Amazing! +1 point.")
        points += 1
    else:
        print("Incorrect, keep on going!")
    word3 = input("Type in (fun). You have N/A seconds before the monster gets you. Go! ").lower()
    if word3 == "fun":
        print("Nice! +1 point.")
        points += 1
else:
    print("Incorrect, better luck next time!")
    
print("Your total points are " + str(points) + "/3. You had completed the tutorial!")