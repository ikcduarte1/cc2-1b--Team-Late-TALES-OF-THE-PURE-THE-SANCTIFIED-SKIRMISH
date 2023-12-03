import random

class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


    # INSTANCES OF WEAPONS CLASS
Fists = Weapons(name = "Fists", damage = random.randint(5,10))
Broom = Weapons("Broom", damage = random.randint(10, 15))
WaterGun = Weapons("Water Gun", damage = random.randint(15, 25))
Vaccum = Weapons("Vaccum", damage = random.randint(25, 40))
BleachBane = Weapons("Bleach Bane", damage = random.randint(40, 100))

    # FOR ENEMIES
Dirty_fists = Weapons("Dirty Fists", damage = random.randint(1, 10))
Toxic_swarm = Weapons("Toxic Swarm", damage = random.randint(10, 20))
Germ_explosion = Weapons("Germ explosion", damage = random.randint(20, 50))
Bad_breath = Weapons("Bad Breath", damage = random.randint(20, 50))
        