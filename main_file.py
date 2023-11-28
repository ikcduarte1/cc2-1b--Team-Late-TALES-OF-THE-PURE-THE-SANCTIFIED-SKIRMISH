import time
import random
import os
import sys
import curses
import random
from entities import Player
from entities import Enemy
from entities import Treasures
from entities import Weapons
from entities import Pots
import gameplay


def prompt():
    print("---------------------------------------")
    print(" HEY! WOULD YOU LIKE TO PLAY OUR GAME? ")
    print("---------------------------------------")
    print("        input 'play' or 'exit'         ") 
    print("---------------------------------------")
    print("      Created by CC2B - GROUP LATE     ")
    print("               MEMBERS:                ")
    print("               DUARTE                  ")
    print("               HABON                   ")
    print("               PADILLA                 ")
    option = ""
    while option not in ['play','exit']: 
        option = input("> ").lower()
        if option == 'play':
            introduction()
        elif option == 'exit':
            sys.exit()
        else:
            print("Please input valid command('start' or 'quit')")
def introduction():
    print("-----------------------------------------------")
    print("THANK YOU FOR CHOOSING TO PLAY OUR GAME, ENJOY!")
    print("-----------------------------------------------")
    press_any_key_to_continue
    os.system('cls')
 
    introduction = """Welcome to 'Tales of the Pure: The Sanctified Skirmish' a thrilling adventure game that takes you on a journey
through a maze overrun by filth and plagued by dirty enemies. In this epic game, you assume the role of a 
determined hero on a mission to restore cleanliness and purity to a once-pristine realm now besieged by darkness.
        
As the protagonist, you must navigate through polluted landscapes, engage in challenging battles with nefarious 
adversaries, and collect treasures, all while armed with an arsenal of unique cleaning tools and gadgets. 
Your quest is to vanquish the vile forces of dirt and grime, and cleanse the world from their corruption and filth."""

    print_text_slowly(introduction)
    press_any_key_to_continue()
    os.system('cls')
    character_name = input(print_text_slowly("What is your characters name:"))
    print_text_slowly(f"Welcome {character_name}!, your quest begins now!")
    press_any_key_to_continue()
    os.system('cls')

    instructions = f"""Your goal is to find all 3 hidden treasures randomly placed around the maze, when you find these 
treasures you are then ableto open a portal that brings you to Pollutiax's lair, there you can defeat him and free 
the world of his corruption and filth. BEWARE! the maze is filled with dirty monsters that can easily defile you 
if you aren't careful! GOOD LUCK! {character_name}"""
    print_text_slowly(instructions)
    press_any_key_to_continue()
    os.system('cls')

def print_text_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

def press_any_key_to_continue():
    input("Press Enter to continue...")


def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    stack = [(1, 1)]

    while stack:
        current_cell = stack[-1]
        maze[current_cell[0]][current_cell[1]] = ' '

        neighbors = [
            (current_cell[0] - 2, current_cell[1]),
            (current_cell[0] + 2, current_cell[1]),
            (current_cell[0], current_cell[1] - 2),
            (current_cell[0], current_cell[1] + 2),
        ]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 < neighbor[0] < rows and 0 < neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == '#']

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            maze[(current_cell[0] + next_cell[0]) // 2][(current_cell[1] + next_cell[1]) // 2] = ' '
            stack.append(next_cell)
        else:
            stack.pop()

    place_treasures(maze, rows, cols)
    return maze

def place_treasures(maze, rows, cols):
    treasures = 0
    min_distance_between_treasures = 4  # Adjust this value based on your preference

    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    while treasures < 3:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if maze[row][col] == ' ' and (row, col) != (1, 1):  # Ensure it's not the starting position
            # Check proximity with existing treasures
            too_close = any(distance((row, col), treasure) < min_distance_between_treasures for treasure in [(i, j) for i in range(rows) for j in range(cols) if maze[i][j] == 'T'])

            if not too_close:
                maze[row][col] = 'T'
                treasures += 1


def print_maze(stdscr, maze, player_pos):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                stdscr.addch(i, j * 2, 'P')
            else:
                stdscr.addch(i, j * 2, cell)


def move_player(player_pos, key):
    row, col = player_pos
    if key == curses.KEY_UP:
        return row - 1, col
    elif key == curses.KEY_DOWN:
        return row + 1, col
    elif key == curses.KEY_LEFT:
        return row, col - 1
    elif key == curses.KEY_RIGHT:
        return row, col + 1
    else:
        return player_pos



    # INSTANCES OF TREASURES CLASS
safeguard_gun = Treasures("Safeguard Gun")
shampoo_portal_juice = Treasures("Shampoo Portal Juice")
shower_head = Treasures("Shower Head")

collected_treasures = []

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    rows = 11
    cols = 21
    maze = generate_maze(rows, cols)
    player_pos = (1, 1)

        

    while True:
        enemy = gameplay.encounter_enemy()
        player = Player(250,100,10,3,3)
  
        gameplay.display_stats(stdscr, player, enemy)
        if maze[player_pos[0]][player_pos[1]] == 'T':

            stdscr.addstr(curses.LINES - 7, 45, f"YOU FOUND A TREASURE!")
            stdscr.addstr(curses.LINES - 6, 45, "To place in your inventory press the Space Bar")
            if key == ord(' '):
                maze[player_pos[0]][player_pos[1]] = ' '
                uncollected_treasures = [safeguard_gun.name,shampoo_portal_juice.name,shower_head.name]
                found_treasure = random.choice(uncollected_treasures)
                collected_treasures.append(found_treasure)
                uncollected_treasures.remove(found_treasure)
                stdscr.refresh()

        stdscr.addstr(curses.LINES - 20, 45, f" Player moved to position: {player_pos}",curses.A_BOLD)
        gameplay.display_commands(stdscr)
        
        print_maze(stdscr, maze, player_pos)
        key = stdscr.getch()

        if key == 27:
            break

        new_pos = move_player(player_pos, key)
        if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] != '#':
            player_pos = new_pos
            
            stdscr.refresh()

if __name__ == "__main__":
    prompt()
    curses.wrapper(main)
