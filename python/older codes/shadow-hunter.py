import time
import random

class ShadowHunterGame:
    def __init__(self):
        self.username = ""
        self.gold = 300
        self.has_vacuum = False
        self.has_detector = False
        self.crafted_items = []
        self.player_hp = 300

    def start(self):
        while True:
            if not self.username:
                self.get_username()
            else:
                if not self.has_vacuum or not self.has_detector:
                    self.craft_weapons()
                else:
                    self.battle()

    def get_username(self):
        self.username = input("Welcome to Shadow Hunter! Please create a username (3 to 20 characters, no real names): \n")
        if len(self.username) > 20:
            print("Username is too long. Please enter a username with 20 characters or fewer.\n")
            self.username = ""
        elif len(self.username) < 3:
            print("Username is too short. Please enter a username with at least 3 characters.\n")
            self.username = ""
        else:
            print(f"Hi {self.username}, there have been shadow sightings and missing people! You must protect our village chief.")
            input("Press Enter to continue...")
            print("Tip: Shadow monsters attack at night only.")
            input("Press Enter to continue...")
            print(f"You have {self.gold} gold available.")
    
    def craft_weapons(self):
        choice = input("What would you like to craft first? 'vacuum' or 'shadow detector': ").lower()
        
        if choice not in ['vacuum', 'shadow detector']:
            print("Invalid choice. Please choose either 'vacuum' or 'shadow detector'.")
            return
        
        if choice == 'vacuum' and self.gold >= 100 and not self.has_vacuum:
            print("Crafting your vacuum...")
            time.sleep(10)
            print("You've crafted a vacuum.")
            self.has_vacuum = True
            self.gold -= 100
            self.crafted_items.append('vacuum')
        elif choice == 'shadow detector' and self.gold >= 100 and not self.has_detector:
            print("Crafting your shadow detector...")
            time.sleep(10)
            print("You've crafted a shadow detector.")
            self.has_detector = True
            self.gold -= 100
            self.crafted_items.append('shadow detector')
        else:
            print("You can't craft this item or you lack the required gold.")

    def battle(self):
        shadow_hp = 100
        
        print("You encounter a shadow monster. Prepare to battle!\n")
        while shadow_hp > 0 and self.player_hp > 0:
            # Determine who attacks first
            attacker = random.choice(["player", "shadow"])
            if attacker == "player":
                attack_choice = self.get_attack_choice()
                if attack_choice == 'extreme winds':
                    damage = 50
                elif attack_choice == 'whirlwind blow':
                    damage = 75
                shadow_hp -= damage
                print(f"You dealt {damage} damage to the shadow monster! Shadow HP: {shadow_hp}")
            else:
                damage = random.randint(20, 40)
                self.player_hp -= damage
                print(f"The shadow monster attacked you for {damage} damage! Your HP: {self.player_hp}")
            
            if shadow_hp <= 0:
                print("You defeated the shadow monster!")
                return
            elif self.player_hp <= 0:
                print("You were defeated by the shadow monster...")
                return
    
    def get_attack_choice(self):
        while True:
            attack_choice = input("Choose an attack: 'extreme winds' or 'whirlwind blow': ").lower()
            if attack_choice in ['extreme winds', 'whirlwind blow']:
                return attack_choice
            else:
                print("Invalid choice. Please choose either 'extreme winds' or 'whirlwind blow'.")

game = ShadowHunterGame()
game.start()
