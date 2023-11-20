import time
import random
import os
import sys
import curses
import random
import additional


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
    additional.press_any_key_to_continue
    os.system('cls')
 
    introduction = """Welcome to 'Tales of the Pure: The Sanctified Skirmish' a thrilling adventure game that takes you on a journey
through a maze overrun by filth and plagued by dirty enemies. In this epic game, you assume the role of a 
determined hero on a mission to restore cleanliness and purity to a once-pristine realm now besieged by darkness.
        
As the protagonist, you must navigate through polluted landscapes, engage in challenging battles with nefarious 
adversaries, and collect treasures, all while armed with an arsenal of unique cleaning tools and gadgets. 
Your quest is to vanquish the vile forces of dirt and grime, and cleanse the world from their corruption and filth."""

    additional.print_text_slowly(introduction)
    additional.press_any_key_to_continue()
    os.system('cls')
    character_name = input(additional.print_text_slowly("What is your characters name:"))
    additional.print_text_slowly(f"Welcome {character_name}!, your quest begins now!")
    additional.press_any_key_to_continue()
    os.system('cls')

    instructions = f"""Your goal is to find all 3 hidden treasures randomly placed around the maze, when you find these 
    treasures you are then ableto open a portal that brings you to Pollutiax's lair, there you can defeat him and free 
    the world of his corruption and filth. BEWARE! the maze is filled with dirty monsters that can easily defile you 
    if you aren't careful! GOOD LUCK! {character_name}"""
    additional.print_text_slowly(instructions)
    additional.press_any_key_to_continue()
    os.system('cls')




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

    return maze

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

def encounter_enemy():
    from entities import Enemy
    Pollutant = Enemy("Pollutant", 5, 20)
    Toxigore = Enemy("Toxigore", 10, 15)
    Contaminoid = Enemy("Contaminoid", 100, 50)
    Pollutiax = Enemy("Pollutiax", 20, 500)
    chance = random.randint(1, 100)
    if chance <= 60:
        pass
    elif chance <= 85:
        return Pollutant
    elif chance <= 95:
        return Toxigore
    elif chance <= 100:
        return Contaminoid

def display_status(stdscr, status):
    stdscr.addstr(curses.LINES - 18, 0, status, curses.A_REVERSE)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    rows = 11
    cols = 21
    maze = generate_maze(rows, cols)
    player_pos = (1, 1)

    while True:
        stdscr.clear()
        display_status(stdscr, "Move with arrow keys. Press Esc to exit.")
        stdscr.addstr(curses.LINES - 16, 4,f"Player moved to position: {player_pos}",curses.A_BOLD)
        stdscr.addstr(curses.LINES - 14, 17,"STATUS",curses.A_BOLD)
        stdscr.addstr(curses.LINES - 13, 12,"---------------")
        stdscr.addstr(curses.LINES - 12, 13,"HP: 100")
        stdscr.addstr(curses.LINES - 11, 13,"WEAPON: BROOM")
        stdscr.addstr(curses.LINES - 10, 13,"INVENTORY: []")
        stdscr.addstr(curses.LINES - 9, 12,"---------------")
        stdscr.addstr(curses.LINES - 7, 16,"GAMEPLAY",curses.A_BOLD)
        stdscr.addstr(curses.LINES - 6, 12,"---------------")
        stdscr.addstr(curses.LINES - 5, 6, f"{encounter_enemy()}")
        
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
