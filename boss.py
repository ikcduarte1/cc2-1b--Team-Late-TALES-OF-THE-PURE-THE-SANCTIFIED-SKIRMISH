import curses
import random
import sys
from entities import Hero
from weapon import BleachBane



player = Hero("your character", 250, 5, 3)
player.equip(BleachBane)



class Boss:
    def __init__(self, health=1000):
        self.health = health


    def attack(self, player):
        damage_dealt = random.randint(20, 50)
        player.health -= damage_dealt
        return damage_dealt

def draw_boss(stdscr):
    boss_ascii = """
BOSS BATTLE!!!
    
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
        if key == ord('1'):
            player.attack(boss)
            boss.attack(player)

            stdscr.refresh()

            if player.health <= 0:
                stdscr.addstr(17, 0, "Game Over! Your health reached zero.")
                stdscr.refresh()
                break

            if boss.health <= 0:
                stdscr.addstr(17, 0, "Congratulations! You defeated the boss!")
                stdscr.refresh()
                break
                

        if key == ord('2'):
            if player.hp_pot():
                player.hp_pot()
            else:
                 stdscr.addstr(13, 0, "You are out of health pots..")

            


        stdscr.refresh()

def boss(stdscr):
    stdscr.clear()
    boss_fight(stdscr)
    stdscr.refresh()

