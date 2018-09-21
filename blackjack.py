#!/usr/bin/env python3

"""
Blackjack

Play a game of Blackjack from the command line, one player against the dealer
"""

import curses
import getpass
# import termios, fcntl, sys, os

class Deck:
    cards = []
    def Deck():
        cards 

    def shuffle(self):
        pass

class Player:
    cards = []

    def hit(self):
        pass
    
    def split(self):
        pass
    
    def stand(self):
        pass

    def surrender(self):
        pass

class Dealer: # inherit from superclass common to Player?
    cards = []

def show_status():
    print()

def rpad(string, width=80):
    num = width - len(string)
    return string + ' '*num 

def play(name): # (stdscr)
    # build a new window
    begin_x = 0; begin_y = 0
    height = 15; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    stdscr.refresh()

    YPOS_TITLE = 0
    YPOS_DEALER_NAME = 3
    YPOS_DEALER_HAND = 4
    YPOS_PLAYER_NAME = 5
    YPOS_PLAYER_HAND = 6
    YPOS_KEYS = 9
    YPOS_ACTION = 10
    YPOS_DEBUG = 15

    card_names = ["Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    deck = []
    deck += 4 * [1]
    deck += 4 * [2]
    deck += 4 * [3]
    deck += 4 * [4]
    deck += 4 * [5]
    deck += 4 * [6]
    deck += 4 * [7]
    deck += 4 * [9]
    deck += 4 * [10]
    deck += 4 * [11]
    deck += 4 * [12]
    deck += 4 * [13]

    cards_dealer = []

    debug_text = str(deck)

    stdscr.addstr(YPOS_TITLE, 0, "Blackjack by chrisjbird@gmail.com")
    stdscr.addstr(YPOS_DEALER_NAME, 0, "Dealer:")
    # stdscr.addstr(YPOS_DEALER_HAND, 0, "[]")
    stdscr.addstr(YPOS_DEALER_HAND, 0, str(cards_dealer))
    stdscr.addstr(YPOS_PLAYER_NAME, 0, name + ":")
    stdscr.addstr(YPOS_PLAYER_HAND, 0, "[]")
    stdscr.addstr(YPOS_KEYS, 0, "(h)it (s)tand s(p)lit (d)ouble su(r)render (q)uit")
    stdscr.addstr(YPOS_DEBUG, 0, debug_text)

    actions = {
        "q": "Quit",
        "h": "Hit",
        "s": "Stand",
        "p": "Split",
        "d": "Double",
        "r": "Surrender"
    }

    while True:
        c = stdscr.getch() # c = win.getch()
        if c == ord('q'):       # quit
            break
        elif c == ord('h'):     # hit
            stdscr.addstr(1, 0, "")
            pass
        elif c == ord('s'):     # stand
            pass
        elif c == ord('p'):     # split
            pass
        elif c == ord('d'):     # double
            pass
        elif c == ord('r'):     # surrender
            pass
        try:
            action = actions[chr(c)]
        except KeyError:
            action = "Action not found: '" + str(chr(c)) + "'"  # TODO: Use string interpolation 
        stdscr.addstr(YPOS_ACTION, 0, rpad(action))
        stdscr.refresh()


if __name__ == "__main__":
    print ("Welcome to Blackjack")
    default = getpass.getuser()
    name = input("What's your name? [" + default + "]: ")
    if name == "":
        name = default
    try:
        # set up curses environment
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        play(name)
    finally:
        # restore command line
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()