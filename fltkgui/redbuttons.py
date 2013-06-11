#!/usr/bin/python

from fltk import *


def button_cb(widget):
    widget.color(FL_RED)
    widget.redraw()

window = Fl_Window(500, 300, 310, 100, 'Three red buttons')
window.color(FL_BLACK)
window.begin()

button1 = Fl_Button(10, 10, 90, 80, 'Button 1')
button1.callback(button_cb)
button2 = Fl_Button(110, 10, 90, 80, 'Button 2')
button2.callback(button_cb)
button3 = Fl_Button(210, 10, 90, 80, 'Button 3')
button3.callback(button_cb)

window.end()
window.show()
Fl.run()
