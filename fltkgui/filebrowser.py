#!/usr/bin/python

from fltk import *


def but_cb(widget):
    global fdict

    fname = fl_file_chooser('Pick a text file', '', '/home/junior/bigbook.txt')
    fdict = dict((chr(let), 0) for let in xrange(65, 91))
    with open(fname) as f:
        for line in f:
            for let in line:
                let = let.upper()
                if let in fdict:
                    fdict[let] = fdict[let] + 1

    for let in sorted(fdict, key=lambda x: fdict[x], reverse=True):
        browser.add(let + ': ' + str(fdict[let]))
    browser.redraw()


window = Fl_Window(500, 100, 300, 300, 'File character counter')

window.begin()
but = Fl_Button(10, 10, 80, 30, 'Open')
browser = Fl_Browser(10, 50, 280, 240)
window.end()

but.callback(but_cb)

window.show()
Fl.run()
