#!/usr/bin/python

import curses
import time

stdscr = curses.initscr()
stdscr.nodelay(1)
curses.noecho()
curses.cbreak()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.curs_set(0)

windowsize = stdscr.getmaxyx()
y = windowsize[0]
x = windowsize[1]

while 1:
    c = stdscr.getch()
    if c == ord('q'): break
    windowsize = stdscr.getmaxyx()
    newy = windowsize[0]
    newx = windowsize[1]
    if (newy != y) or (newx != x):
        y = newy
        x = newx
        stdscr.clear()
    
    #s = str(time.strftime("%H:%M:%S", time.gmtime()))
    s = str(time.clock())
    stdscr.addstr(y / 2, (x / 2) - (len(s) / 2), s, curses.color_pair(1) )
    stdscr.refresh()


curses.nocbreak()
curses.echo()
curses.endwin()
