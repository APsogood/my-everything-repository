import random
import time
word_tupe_easy = ("When", "Master", "Done", "Happy", "Help", "Find", "Read", "Feed", "March", "Fruit", "Simple", "Sharp", "Sheep", "Sleep", "Upset", "Then", "Runner", "Jump", "Rabbit", "Great", "Happy", )
word_tuple_medium = ("Monster", "Destroyer", "Monkey", "Marathon", "Fisherman", "Friendly", "Demolish", "Saskatchewan", "Television", "Giraffe", "Kangaroo", "Fighter Plane", "Flag Football", "Tetanus", "Excuses", "Married", "Explosion")
word_tuple_hard = ("Discombobulated", "Confusion", "Arachnophobia", "Megalophobia", "Microphobia", "Teraphobia", "Nyctophobia", "Hematophobia", "Aibohphobia" "")
word_tuple_extreme = ("Hippopotomonstrosesquippedaliophobia", "Lymphangioleiomyomatosis", "Supercalifragilisticexpialidocious")
word_tuple_unbeatable = ("Pneumonoultramicroscopicsilicovolcanoconiosis")


welcome = input("Welcome to Monster Hunter! In this game, you need to type in a word within a certain amount of time. There are 3 difficulties. Easy, Medium and Hard. Type in (tutorial) to play the tutorial! ")
if welcome == "tutorial".lower():
    pass