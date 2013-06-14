#!/usr/bin/python

from fltk import *


def button_cb(widget):
    widget.color(FL_RED)
    widget.redraw()

window = Fl_Window(500, 300, 310, 100, 'Three red buttons')
window.color(FL_BLACK)
window.begin()

for pos, n in zip(xrange(10, 310, 100), xrange(1, 4)):
    exec 'button' + str(n) + ' = Fl_Button(' + str(pos) + ', 10, 90, 80)'
    exec 'button' + str(n) + ".label('Button" + str(n) + "')"
    exec 'button' + str(n) + '.callback(button_cb)'

window.end()
window.show()
Fl.run()
