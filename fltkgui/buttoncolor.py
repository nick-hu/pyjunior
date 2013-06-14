#!/usr/bin/python

from fltk import *


def b1callb(widget):
    global ctoggle

    if ctoggle:
        button2.color(FL_MAGENTA)
    else:
        button2.color(FL_RED)
    ctoggle = not ctoggle
    button2.redraw()


def b2callb(widget):
    global ctoggle2

    if ctoggle2:
        button.color(FL_GREEN)
    else:
        button.color(FL_DARK_GREEN)
    ctoggle2 = not ctoggle2
    button.redraw()

ctoggle, ctoggle2 = 1, 1

window = Fl_Window(500, 300, 400, 400, 'Button Color')
window.begin()

button = Fl_Button(75, 100, 125, 30, '&A')
button.color(FL_DARK_GREEN)
button.callback(b1callb)

button2 = Fl_Button(200, 100, 125, 30, '&B')
button2.color(FL_RED)
button2.callback(b2callb)

window.end()
window.show()
Fl.run()
