import curses
import random
from entities import Enemy, Player, Weapons, Pots, Treasures
import main_file


    # INSTANCE OF PLAYER CLASS
player = Player(200, 100, random.randint(1, 10), 3, 3)

    # INSTANCES OF ENEMY CLASS
Pollutant = Enemy("Pollutant", 5, 20)
Toxigore = Enemy("Toxigore", 10, 15)
Contaminoid = Enemy("Contaminoid", 50, 50)
Pollutiax = Enemy("Pollutiax", 20, 500)


    # INSTANCES OF WEAPONS CLASS
Broom = Weapons("Broom", random.randint(10, 15))
WaterGun = Weapons("Water Gun", random.randint(15, 30))
Vaccum = Weapons("Vaccum", random.randint(30, 50))
BleachBane = Weapons("Bleach Bane", random.randint(50, 100))

    # INSTANCES OF TREASURES CLASS
safeguard_gun = Treasures("Safeguard Gun")
shampoo_portal_juice = Treasures("Shampoo Portal Juice")
shower_head = Treasures("Shower Head")

inventory = main_file.collected_treasures

    # INSTANCES OF POTS CLASS
health_pots = Pots("Health pot", random.randint(20, 50), 0)
energy_pots = Pots("Energy pots", random.randint(10, 20), 0)


def display_commands(stdscr):
    stdscr.addstr(curses.LINES - 18, 0, "Move with arrow keys. Press Esc to exit. ", curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 17, 0, "  '1': to attack                         ", curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 16, 0, "  '2': to use health potions             ", curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 15, 0, "  '3': to use energy potions             ", curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 14, 0, "  '4': to pick up weapons or pots        ", curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 13, 0, "  '5': run away from a battle            ", curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 12,  0, "  'space bar': to pick up treasures      ", curses.A_REVERSE)
    stdscr.refresh()

def display_stats(stdscr, player, enemy):
    stdscr.clear()
    stdscr.addstr(curses.LINES - 29, 49, f" PLAYER STATS ",curses.A_REVERSE)
    stdscr.addstr(curses.LINES - 27, 45, f"  HP: {player.health}", curses.A_BOLD)
    stdscr.addstr(curses.LINES - 26, 45, f"  STAMINA: {player.stamina}", curses.A_BOLD)
    stdscr.addstr(curses.LINES - 25, 45, f"  WEAPON DAMAGE: {player.damage}", curses.A_BOLD)
    stdscr.addstr(curses.LINES - 24, 45, f"  Health Pots: {player.hp_pots}", curses.A_BOLD)
    stdscr.addstr(curses.LINES - 23, 45, f"  Energy Pots: {player.enrg_pots}", curses.A_BOLD)
    stdscr.addstr(curses.LINES - 22, 45, f"  INVENTORY: {inventory}", curses.A_BOLD)
    stdscr.refresh()
    
    if enemy:
        stdscr.addstr(14, 46, f"You encountered a {enemy.name}")
        stdscr.addstr(13, 46, f"Enemy Health: {enemy.health}")
        stdscr.addstr(12, 46, f"Enemy Damage: {enemy.damage}")

    stdscr.refresh()

def combat(stdscr, player, enemy):
    if enemy is None:
        return "No enemies in sight..."

    while player.health > 0 and (enemy is None or enemy.health > 0):
        
        display_stats(stdscr, player, enemy)

        key = stdscr.getch()

        if key == ord('1'):
            player.attack(enemy)
            
        elif key == ord('2'):
            stdscr.addstr(14, 1, f"{player.use_hp_pot()}")
        elif key == ord('3'):
            stdscr.addstr(14, 1, f"{player.use_enrg_pot()}")
        elif key == ord('4'):
            stdscr.addstr(14, 1, f"{player.run()}")

            

        # Enemy's turn
        if enemy:
            enemy.attack(player)
            

        stdscr.refresh()

    if player.health <= 0:
        return "You have been defeated. Game over."
    elif enemy and enemy.health <= 0:
        player.stamina -= 5
        return f" You defeated the {enemy.name}."


def encounter_enemy():
    chance = random.randint(1, 100)
    if chance <= 50:
        return None
    elif chance <= 75:
        return Pollutant
    elif chance <= 90:
        return Toxigore
    elif chance <= 100:
        return Contaminoid

        

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    display_commands(stdscr)
    display_stats(stdscr,player,enemy)

    enemy = encounter_enemy()
    player = Player(250,100,10,3,3)

    result = combat(stdscr, player, enemy)
    stdscr.addstr(13, 0, result)
    stdscr.addstr(12, 0, "  Press any key to continue.  ", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()



if __name__ == "__main__":
    curses.wrapper(main)
