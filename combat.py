from entities import Hero, Enemy
from weapon import Weapons
import curses
import random
from weapon import Fists, Broom, WaterGun, Vaccum, BleachBane
import sys


player = Hero("your character", 250, stamina = 5, pots = 3)




def combat(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    enemy = encounter_enemy()

    

    key = 0
    while key != 27:
        stdscr.clear()


        display_stats(stdscr, player, enemy)

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            player.attack(enemy)
            enemy.attack(player)


            display_stats(stdscr, player, enemy)

            stdscr.refresh()

            if player.health <= 0:
                stdscr.clear()
                stdscr.addstr(13, 0, "You have been defeated. Game over.")
                stdscr.refresh()
                sys.exit()

            if enemy.health <= 0:
                stdscr.addstr(10, 0, "You defeated the enemy!")
                dropped = random.choice(weapons_list)
                if dropped == None:
                    stdscr.addstr(13, 0, "The enemy didnt drop anything..")
                    stdscr.addstr(14, 0, "Press any key to continue...")
                else:
                    stdscr.addstr(13, 0, f"The enemy dropped a {dropped.name}")
                    stdscr.addstr(14, 0, "Press 3 to equip..")
                    stdscr.addstr(15, 0, "Or press any key twice to ignore..")

                    stdscr.refresh()
                    equip_key = stdscr.getch()

                    if equip_key == ord('3'):
                        player.weapon = dropped
                        stdscr.addstr(16, 0, f"You equipped the {dropped.name}")
                        stdscr.addstr(17, 0, "Press any key to continue...")
                        stdscr.refresh()
                    

                break

                

        if key == ord('2'):
            if player.hp_pot():
                player.hp_pot()
            else:
                 stdscr.addstr(13, 0, "You are out of health pots..")




        if key == ord('4'):
            if player.run():
                stdscr.addstr(13, 0, "You ran away from the enemy")
                stdscr.addstr(14, 0, "Press any key to continue...")
                break
            else:
                stdscr.addstr(13, 0, "You are out of stamina..")
    


        
    stdscr.getch()



def encounter_enemy():
    chance = random.randint(1, 100)
    if chance <= 60:
        return Enemy("Pollutant",20, Weapons("Dirty Fists", damage = random.randint(1, 10)))
    elif chance <= 75:
        return Enemy("Toxigore", 35, Weapons("Toxic Swarm", damage = random.randint(10, 20)))
    elif chance <= 100:
        return Enemy("Contaminoid", 30, Weapons("Germ explosion", damage = random.randint(20, 50)))


def display_stats(stdscr, player, enemy):
    stdscr.clear()
    stdscr.addstr(7, 49, f" PLAYER STATS ",curses.A_REVERSE)
    stdscr.addstr(8, 45, f"  HP: {player.health}", curses.A_BOLD)
    stdscr.addstr(9, 45, f"  STAMINA: {player.stamina}", curses.A_BOLD)
    stdscr.addstr(10, 45, f"  WEAPON: {player.weapon.name}", curses.A_BOLD)
    stdscr.addstr(11, 45, f"  Health Pots: {player.pots}", curses.A_BOLD)

    stdscr.addstr(8, 0, f"You encounterd a {enemy.name}", curses.A_REVERSE)
    stdscr.addstr(9, 0, f"Enemy Health: {enemy.health}")
    stdscr.addstr(10, 0, f"Enemy Weapon: {enemy.weapon.name}")
    stdscr.addstr(11, 0, f"Enemy Damage: {enemy.weapon.damage}")

    stdscr.addstr(2, 0, "  '1': to attack                         ", curses.A_REVERSE)
    stdscr.addstr(3, 0, "  '2': to use health potions             ", curses.A_REVERSE)
    stdscr.addstr(4, 0, "  '3': to pick up weapons                ", curses.A_REVERSE)
    stdscr.addstr(5, 0, "  '4': run away from a battle            ", curses.A_REVERSE)
    stdscr.addstr(6,  0, "  'space bar': to pick up treasures      ", curses.A_REVERSE)
    stdscr.refresh()

weapons_list = [None, Broom, WaterGun, Vaccum]




