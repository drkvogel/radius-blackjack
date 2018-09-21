import termios, fcntl, sys, os
import curses
# from curses import wrapper
# from curses import *

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
                    # print("Got character", repr(c))   # print line 
                    # print(': {0}\r'.format(c),)       # ?
                    print(str(c)+'\r', end='')          # replace current line
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def rpad(string, width=80):
    # pass
    num = width - len(string)
    return string + ' '*num 

# def try_curses(stdscr):
def try_curses():
    # set up curses environment
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    # build a new window
    begin_x = 0; begin_y = 0
    height = 15; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    stdscr.refresh()
    # win.getch()

    YPOS_TITLE = 0
    YPOS_DEALER_HAND = 3
    YPOS_PLAYER1_HAND = 4
    YPOS_KEYS = 9
    YPOS_ACTION = 10

    stdscr.addstr(YPOS_TITLE, 0, "Blackjack by chrisjbird@gmail.com")
    stdscr.addstr(YPOS_DEALER_HAND, 0,  "Dealer  : []")
    stdscr.addstr(YPOS_PLAYER1_HAND, 0, "Player 1: []")
    stdscr.addstr(YPOS_KEYS, 0, "(h)it (s)tand s(p)lit (d)ouble su(r)render (q)uit")

    actions = {
        "q": "Quit",
        "h": "Hit",
        "s": "Stand",
        "p": "Split",
        "d": "Double",
        "r": "Surrender"
    }

    while True:
        # stdscr.addstr(0, 0, "(h)it (s)tand s(p)lit (d)ouble su(r)render (q)uit")
        # c = win.getch()
        c = stdscr.getch()
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
        # stdscr.addstr(0, 0, "(h)it (s)tand s(p)lit (d)ouble su(r)render (q)uit")
        # stdscr.addstr(1, 0, "Current mode: " + str(c)) #, curses.A_REVERSE)
        # stdscr.addstr(YPOS_ACTION, 0, str(chr(c)))
        try:
            action = actions[chr(c)]
        except KeyError:
            action = "Action not found: '" + str(chr(c)) + "'"  # TODO: Use string interpolation 
        stdscr.addstr(YPOS_ACTION, 0, rpad(action))
        stdscr.refresh()

    # restore command line
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()



# def kill_curses(self):
#     curses.nocbreak()
#     stdscr.keypad(False)
#     curses.echo()
#     curses.endwin()

# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)

# curses.wrapper(try_curses)

if __name__ == "__main__":
    # play()
    # try_curses(stdscr)
    try_curses()
