import curses
from random import choice, randint

# Character set to use for the Matrix rain, adding more symbols will give a different aesthetic
matrix_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{}|;:,.<>?'

def start_matrix(win):
    curses.curs_set(0)  # Hide cursor
    win.nodelay(True)  # Don't block I/O calls
    win.timeout(100)  # Wait 100ms before the screen updates

    max_y, max_x = win.getmaxyx()  # Get window size
    code_cols = [1] * max_x  # Initialize rain columns

    while True:
        for i in range(max_x - 1):  # Adjusted to avoid writing beyond the rightmost column
            if code_cols[i] < max_y - 1:  # Adjusted to avoid writing in the bottom row
                if randint(0, 1):
                    char = choice(matrix_chars)
                    try:
                        win.addstr(code_cols[i], i, char, curses.color_pair(1))
                        code_cols[i] += 1
                    except curses.error:
                        pass  # Ignore errors related to attempting to add a character out of bounds
            else:
                code_cols[i] = 1

        win.refresh()

        # Exit on any key press
        if win.getch() != -1:
            break

def main():
    curses.initscr()  # Initialize screen
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Set color scheme
    curses.wrapper(start_matrix)  # Protect program and use 'curses' environment properly

if __name__ == "__main__":
    main()
