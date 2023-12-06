import time
import os
import sys


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

def print_text_slowly(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

def press_any_key_to_continue():
    input("Press Enter to continue...")

