name = input("Enter your name: ")
strength = int(input("Enter strength (1-10): "))
health = int(input("Enter health (1-10): "))
luck = int(input("Enter luck (1-10): "))
if strength + health + luck > 15:
    print("Stats are too high. All stats reset to default value of 5.")