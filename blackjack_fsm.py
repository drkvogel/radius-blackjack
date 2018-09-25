#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
Blackjack

Play a game of Blackjack from the command line, one player against the dealer
"""

import curses
import getpass
import random
import time
import datetime 
import backtrace

backtrace.hook(reverse=False, align=False, strip_path=False, enable_on_envvar_only=False, on_tty=False, conservative=False, styles={})

class Game:
    actions = {
        "b": "bet",
        "d": "deal",
        "q": "Quit",
        "h": "Hit",
        "s": "Stand",
        "p": "Split",
        "o": "Double",
        "r": "Surrender"
    }
    def __init__(self, _minimum_bet=1, _maximum_bet=5000, _bet_increment=50):   # _players, 
        # players = []  # ?
        # self.players = _players
        self.minimum_bet = _minimum_bet
        self.maximum_bet = _maximum_bet
        self.bet_increment = _bet_increment

"""
Simulate a standard(?) 52-card deck of cards
TODO: different pack types?
TODO: test
"""
class Deck:
    card_names = ["Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self):
        self.cards = []
        self.cards += 4 * [1]
        self.cards += 4 * [2]
        self.cards += 4 * [3]
        self.cards += 4 * [4]
        self.cards += 4 * [5]
        self.cards += 4 * [6]
        self.cards += 4 * [7]
        self.cards += 4 * [9]
        self.cards += 4 * [10]
        self.cards += 4 * [11]
        self.cards += 4 * [12]
        self.cards += 4 * [13]

    def shuffle(self, sleep_time=1):
        random.shuffle(self.cards)
        time.sleep(sleep_time)

    def pick(self):
        # if self.cards:
            return self.cards.pop() # ?

"""
The value of cards two through ten is their pip value (2 through 10). 
Face cards (Jack, Queen, and King) are all worth ten. 
Aces can be worth one or eleven.
"""
class Hand():
    def __init__(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def min_value(self):
        value = 0
        for card in self.cards:
            if card >= 1 and card <= 10:    # ace - ten
                value += card
            elif card >= 11 and card <= 13: # jack, queen, king
                value += 10
            else:
                raise "Invalid card value: " + str(card)
    def max_value(self):
        value = 0
        for card in self.cards:
            if card == 1:                   # ace
                value += 11
            elif card >= 2 and card <= 10:  # two - ten
                value += card
            elif card >= 11 and card <= 13: # jack, queen, king
                value += 10
            else:
                raise "Invalid card value: " + str(card)

class Participant:
    def __init__(self, _name):
        self.name = _name
        self.cards = []

class Player(Participant):
    def __init__(self, _name, _bankroll=10000):
        # self.name = _name
        self.cards = []
        self.bank = _bankroll
        self.stake = 0
        self.winnings = 0

    def bet(self, increment=50):
        if self.bank >= increment:
            self.stake += increment
            self.bank -= increment
        else:
            raise "Out of cash" # TODO ?

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
    def __init__(self):
        pass

    def deal(self):
        pass

"""
Dimensions for curses screen
"""
class Curses_UI:
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
    YPOS_STATUS = 17
    XPOS_STATUS = 10
    YPOS_DEBUG = 20

def show_status(message):
    stdscr.addstr(Curses_UI.YPOS_STATUS, Curses_UI.XPOS_STATUS, rpad(message))
    stdscr.refresh()

def show_header():
    # build a new window
    win = curses.newwin(15, 40, 0, 0)    # height, width, y, x
    stdscr.addstr(Curses_UI.YPOS_TITLE, 0, "Blackjack by Chris Bird (chrisjbird@gmail.com)")
    stdscr.addstr(Curses_UI.YPOS_DEALER_NAME, 0, "Dealer:")
    stdscr.addstr(Curses_UI.YPOS_PLAYER_NAME, 0, name + ":")
    stdscr.addstr(Curses_UI.YPOS_KEYS, 0, "(d)eal (b)et (h)it (s)tand s(p)lit d(o)uble su(r)render (q)uit")
    stdscr.refresh()

"""
Utility function for curses - print a string right-padded with spaces to a certain width
to blank out any existing text on that line
"""
def rpad(string, width=80):
    num = width - len(string)
    return string + ' '*num


STATE_PLACE_BETS, STATE_BETS_PLACED, STATE_PLAYER_TURN, STATE_DEALER_TURN, STATE_PLAYER_LOSS, STATE_PUSH, \
    STATE_PLAYER_WIN, STATE_SURRENDER, STATE_QUIT = range(10)

def transition_place_bets():
    pass
def transition_dummy():
    pass

fsm = FSM_MAP = ( #  {'src':, 'dst':, 'condition':, 'callback': },
    {'src': STATE_PLACE_BETS,    'dst': STATE_BETS_PLACED,       'condition': "", 'callback': transition_place_bets},
    {'src': STATE_BETS_PLACED,    'dst': STATE_PLAYER_TURN,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PLAYER_TURN,    'dst': STATE_PLAYER_TURN,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PLAYER_TURN,    'dst': STATE_PLAYER_WIN,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PLAYER_TURN,    'dst': STATE_PLAYER_LOSS,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PLAYER_TURN,    'dst': STATE_DEALER_TURN,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_DEALER_TURN,    'dst': STATE_PLAYER_WIN,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_DEALER_TURN,    'dst': STATE_PLAYER_LOSS,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_DEALER_TURN,    'dst': STATE_PUSH,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PLAYER_WIN,    'dst': STATE_PLACE_BETS,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PLAYER_LOSS,    'dst': STATE_PLACE_BETS,       'condition': "", 'callback': transition_dummy},
    {'src': STATE_PUSH,    'dst': STATE_PLACE_BETS,       'condition': "", 'callback': transition_dummy},
    {'src': "",    'dst': "",       'condition': "", 'callback': transition_dummy},
    {'src': "",    'dst': "",       'condition': "", 'callback': transition_dummy},
    {'src': "",    'dst': "",       'condition': "", 'callback': transition_dummy}
)

def play(name):
    show_header()
    game = Game()
    deck = Deck()
    # stdscr.addstr(Dims.YPOS_ACTION, 0, rpad("Shuffling..."))
    show_status("Shuffling...")
    stdscr.refresh()
    deck.shuffle()
    time.sleep(1)
    show_status("")
    stdscr.refresh()
    dealer = Dealer()
    player = Player(name)

    while True:
        stdscr.addstr(Curses_UI.YPOS_DEALER_HAND, 0, rpad(str(sum(dealer.cards)) + ": " + str([Deck.card_names[card] for card in dealer.cards])))
        stdscr.addstr(Curses_UI.YPOS_PLAYER_HAND, 0, rpad(str(sum(player.cards)) + ": " + str([Deck.card_names[card] for card in player.cards])))
        stdscr.addstr(Curses_UI.YPOS_PLAYER_BANK, 0, rpad("Bank: £" + str(player.bank)))
        stdscr.addstr(Curses_UI.YPOS_PLAYER_WINNINGS, 0, rpad("Winnings: £" + str(player.winnings)))
        stdscr.addstr(Curses_UI.YPOS_PLAYER_BET, 0, rpad("Bet: £" + str(player.stake)))
        debug_text = rpad(str(deck.cards), 180)  # can be at least 165 chars long
        stdscr.addstr(Curses_UI.YPOS_DEBUG, 0, rpad(debug_text))
        stdscr.refresh()

        c = stdscr.getch() # c = win.getch()
        if c == ord('b'):                           # bet
            try:
                player.bet(game.bet_increment)
            except:
                pass    # TODO provide feedback - out of money
        elif c == ord('d'):                         # deal
            try:
                player.cards.append(deck.pick())
                player.cards.append(deck.pick())
            except: # IndexError?
                pass    # TODO provide feedback - no more cards
        elif c == ord('h'):                         # hit
            stdscr.addstr(1, 0, "")
            pass
        elif c == ord('s'):                         # stand
            pass
        elif c == ord('p'):                         # split
            pass
        elif c == ord('d'):                         # double
            pass
        elif c == ord('r'):                         # surrender
            pass
        elif c == ord('q'):                         # quit
            break
        elif c == ord('t'):                         # test
            show_status("This is a test at " + str(datetime.datetime.now()))
            time.sleep(1)
            show_status("")
        try:
            action = Game.actions[chr(c)]
        except KeyError:
            action = "Action not found: '" + str(chr(c)) + "'"  # TODO: Use string interpolation 
        stdscr.addstr(Curses_UI.YPOS_ACTION, 0, rpad(action))


if __name__ == "__main__":
    print ("Welcome to Blackjack")
    default = getpass.getuser()
    name = input("Enter your name to start [" + default + "]: ")
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
        # restore command line environment
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()