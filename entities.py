import random


class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self):
        print(f"Your character used {self.name} to attack and dealth {self.damage} damage!")
    class CurrentWeapon:
        def __init__(self, current_weapon):
            self.current_weapon = current_weapon
        def replace(self, new_weapon):
            self.current_weapon = new_weapon
            print(f"Replaced current weapon to {new_weapon.name}")


Broom = Weapons("Broom", random.randint(5,10))
WaterGun = Weapons("Water Gun", random.randint(10,20))
Vaccum = Weapons("Vaccum", random.randint(30,50))
BleachBane = Weapons("Bleach Bane", random.randint(50, 100))

class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
    
    def attack(self):
        print(f"The {self.name} attacks you for {self.damage} damage")

    def attacked(self):
        print(f"The current health of {self.name} is {self.health}")
        if self.health <= 0:
            print(f"The {self.name} has died")
    
    def __str__(self):
        return f"You have encountered a {self.name}"
    

Pollutant = Enemy("Pollutant", 5, 20)
Toxigore = Enemy("Toxigore", 10, 15)
Contaminoid = Enemy("Contaminoid", 100, 50)
Pollutiax = Enemy("Pollutiax", 20, 500)


class Treasures:
    def __init__(self, name):
        self.name = name

safeguard_gun = Treasures("Safeguard Gun")
shampoo_portal_juice = Treasures("Shampoo Portal Juice")
shower_head = Treasures("Shower Head")



class Character:
    
    alive = True
    def __init__(self, health, collected_treasures, weapon):
        self.health = health
        self.collected_treasures = collected_treasures
        self.weapon = weapon
    
    def heal(self):
        pass
        

    def attacked(self):
        print(f"Your current health is {self.health}")
        if self.health <= 0:
            print("You have DIED!")
            alive = False


myCharacter = Character(100, [], Broom)






myCharacter = Character(100, [], Broom)



