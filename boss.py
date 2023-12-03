import curses
import random
import sys
from entities import Hero
from weapon import BleachBane


player = Hero("your character", 500, 5, 3)
player.equip(BleachBane)



class Boss:
    def __init__(self, health=500):
        self.health = health


    def attack(self, player):
        damage_dealt = random.randint(20, 50)
        player.health -= damage_dealt
        return damage_dealt

def draw_boss(stdscr):
    boss_ascii = """
     .--.
    |o_o |
    |:_/ | .--["I'M SO DIRTY!"]
   //   \\ \\
  (|     | )
 /'\\_   _/`\\
 \\___)=(___/
    """
    stdscr.addstr(0, 0, boss_ascii)
def draw_stats(stdscr, player, boss):
    stdscr.addstr(7, 49, f" PLAYER STATS ",curses.A_REVERSE)
    stdscr.addstr(8, 45, f"  HP: {player.health}", curses.A_BOLD)
    stdscr.addstr(9, 45, f"  STAMINA: {player.stamina}", curses.A_BOLD)
    stdscr.addstr(10, 45, f"  WEAPON: {player.weapon.name}", curses.A_BOLD)
    stdscr.addstr(11, 45, f"  Health Pots: {player.pots}", curses.A_BOLD)

    stdscr.addstr(13, 0, f"Boss Health: {boss.health}")

def boss_fight(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    boss = Boss()

    while True:
        stdscr.clear()

        draw_boss(stdscr)
        draw_stats(stdscr, player, boss)

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('1'):
            player_damage = player.attack(boss)
            boss_damage = boss.attack(player)

            stdscr.addstr(15, 0, f"You dealt {player_damage} damage to the boss!")
            stdscr.addstr(16, 0, f"The boss dealt {boss_damage} damage to you!")

            if player.health <= 0:
                stdscr.addstr(18, 0, "You have been defeated. Game over.")
                sys.exit()

            if boss.health <= 0:
                stdscr.addstr(18, 0, "Congratulations! You defeated the boss!")
                sys.exit()

        stdscr.refresh()
