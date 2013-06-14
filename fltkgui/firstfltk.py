#!/usr/bin/python

from fltk import *


def b1callb(widget):
    print 'Button A pressed!'


window = Fl_Window(500, 300, 400, 400, 'Window title')
# (xpos, ypos, w, h, label) or (w, h, label)
window.begin()

button = Fl_Button(75, 100, 125, 30, 'Button &A label')
# or use button.label('&Button label')
button.color(FL_DARK_GREEN)
button.callback(b1callb)

button2 = Fl_Button(200, 100, 125, 30, 'Button &B label')
button2.color(FL_RED)

window.end()
window.show()  # Show the window
Fl.run()
