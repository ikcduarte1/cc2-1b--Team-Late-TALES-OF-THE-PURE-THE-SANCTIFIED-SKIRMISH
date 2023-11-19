import time
import random
import os
import sys
import curses
import random
import entities

def prompt():
    print("#######################################")
    print(" HEY! WOULD YOU LIKE TO PLAY OUR GAME? ")
    print("#######################################")
    print("        input 'play' or 'exit'         ") 
    print("#######################################")
    print("      Created by CC2-1B-GROUP LATE     ")
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
    print("################################################")
    print("THANK YOU FOR CHOOSING TO PLAY OUR GAME, ENJOY!")
    print("################################################")
    input("input any key to continue... \n")

    os.system('cls')
 
    introduction = """Welcome to 'Tales of the Pure: The Sanctified Skirmish' a thrilling adventure game that takes you on a journey
through a maze overrun by filth and plagued by dirty enemies. In this epic game, you assume the role of a 
determined hero on a mission to restore cleanliness and purity to a once-pristine realm now besieged by darkness.
        
As the protagonist, you must navigate through polluted landscapes, engage in challenging battles with nefarious 
adversaries, and collect treasures, all while armed with an arsenal of unique cleaning tools and gadgets. 
Your quest is to vanquish the vile forces of dirt and grime, and cleanse the world from their corruption and filth."""

    print_text_slowly(introduction)
    character_name = input(print_text_slowly("What is your characters name:"))
    print_text_slowly(f"Welcome {character_name}!, your quest begins now!")
    input("input any key to continue... \n")
    os.system('cls')

    instructions = f"""
Your goal is to find all 3 hidden treasures randomly placed around the maze, when you find these treasures you are then able
to open a portal that brings you to Pollutiax's lair, there you can defeat him and free the world of his corruption and filth.
BEWARE! the maze is filled with dirty monsters that can easily defile you if you aren't careful! GOOD LUCK! {character_name}"""
    print_text_slowly(instructions)
    input("input any key to continue... \n")
    os.system('cls')


def print_text_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "



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

def main(stdscr):
    
    curses.curs_set(0)  
    stdscr.clear()

    rows = 11
    cols = 21
    maze = generate_maze(rows, cols)
    player_pos = (1, 1)

    while True:
        stdscr.clear()
        print_maze(stdscr, maze, player_pos)
        stdscr.refresh()

        key = stdscr.getch()

        if key == 27:  # 27 is the ASCII code for the Esc key
            break

        new_pos = move_player(player_pos, key)
        if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] != '#':
            player_pos = new_pos

if __name__ == "__main__":
    prompt()
    curses.wrapper(main)

