#!/usr/bin/env python3

"""
Blackjack

Play a game of Blackjack from the command line, one player against the dealer
"""

import curses
import termios, fcntl, sys, os

class Deck:
    cards = []

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

# def main():
#     pass

def show_status():
    print()

def play():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
                if c != '':
                    # print ("Got character", repr(c))
                    # print(': {0}\r'.format(c),)
                    print(str(c)+'\r', end='')
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


if __name__ == "__main__":
    print ("Welcome to Blackjack")
    name = input("What's your name?: ")
    print("Hello", name)
    play()