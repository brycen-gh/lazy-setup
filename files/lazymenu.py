import yaml, shutil, curses

# Configable Variables

# Dynamically Assigned
selected_role = "analyst"

from os import system
import curses
import time

x = 0

while x != ord('q'):
    screen = curses.initscr()
    curses.curs_set(False) 
    screen.clear() # clear screen
    screen.border(0) # draw border around screen
    screen.addstr(1, 2, "BLAH BLAH ", # add text to screen, line 1, column 2
              curses.A_REVERSE) # highlight text

    ltime = time.asctime(time.localtime(time.time()))

    screen.addstr(3, 2,'BLAH1: ' + ltime)    
    screen.addstr(4, 2, "BLAH2")

    screen.refresh()

    x = screen.getch(7,2)
    


curses.endwin()