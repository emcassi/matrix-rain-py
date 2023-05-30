import curses
import time
import random
import string

class Char:
    def __init__(self, x):
        self.x = x
        self.y = 0

chars = []

def drop_char(stdscr, char: Char):

    if char.y >= curses.LINES - 1:
        chars.remove(char)
        stdscr.addch(char.y, char.x, ' ')
        return

    new_char = random.choice(string.ascii_letters)

    stdscr.addch(char.y, char.x, ' ')
    char.y += 1
    stdscr.addch(char.y, char.x, new_char, curses.color_pair(1))

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_GREEN, -1)

    stdscr.clear()

    cols = curses.COLS

    while True:
        for c in range(cols - 1):
            if random.randint(0, 14) == 0:
                chars.append(Char(c))

        for char in chars:
            drop_char(stdscr, char)

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
