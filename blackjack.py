#!/usr/bin/env python3

"""
Blackjack

Play a game of Blackjack from the command line, one player against the dealer
"""

import curses
import getpass
import random
# import termios, fcntl, sys, os

class Game:
    def Game(_players, _minimum_bet=1, _maximum_bet=5000):
        players = _players
        minimum_bet = _minimum_bet
        maximum_bet = _maximum_bet

class Deck:
    cards = []
    def Deck():
        cards 

    def shuffle(self):
        pass

class Player:
    def Player(_name, _bankroll=10000):
        name = _name
        cards = []
        bankroll = _bankroll
        bet = 0
        winnings = 0

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
    YPOS_PLAYER_NAME = 6
    YPOS_PLAYER_HAND = 7
    YPOS_PLAYER_BANK = 9
    YPOS_PLAYER_BET = 10
    YPOS_PLAYER_WINNINGS = 11
    YPOS_KEYS = 13
    YPOS_ACTION = 14
    YPOS_DEBUG = 20

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
    random.shuffle(deck)
    debug_text = str(deck)

    # test
    cards_dealer = []
    # cards_dealer += [5, 2, 12, 10]

    cards_player = []
    # cards_player += [4, 1, 3, 13, 8]

    bank = 10000
    winnings = 0
    bet = 0

    BET_INCREMENT = 50

    stdscr.addstr(YPOS_TITLE, 0, "Blackjack by Chris Bird (chrisjbird@gmail.com)")
    stdscr.addstr(YPOS_DEALER_NAME, 0, "Dealer:")
    stdscr.addstr(YPOS_PLAYER_NAME, 0, name + ":")
    stdscr.addstr(YPOS_KEYS, 0, "(h)it (s)tand s(p)lit (d)ouble su(r)render (q)uit")

    actions = {
        "b": "bet",
        "d": "deal",
        "q": "Quit",
        "h": "Hit",
        "s": "Stand",
        "p": "Split",
        "d": "Double",
        "r": "Surrender"
    }


    while True:
        stdscr.addstr(YPOS_DEALER_HAND, 0, str(sum(cards_dealer)) + ": " + str([card_names[card] for card in cards_dealer]))
        stdscr.addstr(YPOS_PLAYER_HAND, 0, str(sum(cards_player)) + ": " + str([card_names[card] for card in cards_player]))
        # stdscr.addstr(YPOS_PLAYER_BANK, 0, "Winnings: £" + str(winnings) + ", Bank: £" + str(bank) + ", Bet: £" + str(bet))
        stdscr.addstr(YPOS_PLAYER_BANK, 0, "Bank: £" + str(bank))
        stdscr.addstr(YPOS_PLAYER_WINNINGS, 0, "Winnings: £" + str(winnings))
        stdscr.addstr(YPOS_PLAYER_BET, 0, "Bet: £" + str(bet))
        stdscr.addstr(YPOS_DEBUG, 0, debug_text)
        stdscr.refresh()

        c = stdscr.getch() # c = win.getch()
        if c == ord('b'):       # bet
            bank -= BET_INCREMENT
            bet += BET_INCREMENT
        if c == ord('d'):       # deal
            pass
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

        # play
        play(name)
    finally:
        # restore command line
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()