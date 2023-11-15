import curses
import random

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

def show_maze(stdscr):
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
    curses.wrapper(show_maze)

