import random


class Player:
    def __init__(self, health, stamina, damage, hp_pots, enrg_pots):
        self.health = health
        self.stamina = stamina
        self.damage = damage
        self.hp_pots = hp_pots
        self.enrg_pots = enrg_pots

    def attack(self, enemy):
        damage = random.randint(1, 10)
        enemy.health -= damage
        return f"You dealt {damage} damage to your enemy"

    def use_hp_pot(self):
        if self.hp_pots > 0:
            self.health += random.randint(20, 50)
            self.hp_pots -= 1
            return "You used a potion and restored some health."
        else:
            return "You don't have any health potions left."
        
    def use_enrg_pot(self):
        if self.enrg_pots > 0:
            self.stamina += random.randint(20, 30)
            self.enrg_pots -= 1
            return "You used a potion and restored some energy."
        else:
            return "You don't have any energy potions left."

    def run(self):
        self.stamina -= 10
        return "You ran away and lost 10 stamina."

class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        damage = random.randint(1, self.damage)
        player.health -= damage
        return f"The enemy dealt {damage} damage to you"
    

class Pots:
    def __init__(self, type, power, count):
        self.type = type
        self.power = power
        self.count = count

class HealthPots(Pots):
    ...


class EnergyPots(Pots):
    ...

class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Treasures:
    def __init__(self, name):
        self.name = name






