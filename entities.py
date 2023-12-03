from weapon import Fists, Broom, WaterGun, Vaccum, BleachBane
import random

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = Fists

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)



    
class Hero(Character):
    def __init__(self, name: str, health: int, pots: int, stamina: int):
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon
        self.stamina = stamina
        self.pots = pots
        
    def equip(self, weapon) -> None:
        self.weapon = weapon


    
    def hp_pot(self):
        if self.pots > 0:
            self.pots -= 1
            self.health += random.randint(25, 100)
        else:
            return False

    def run(self):
        if self.stamina > 0:
            self.stamina -= 1
            return True
        else:
            return False




class Enemy(Character):
    def __init__(self, name: str, health: int, weapon):
        super().__init__(name=name, health=health)
        self.weapon = weapon

