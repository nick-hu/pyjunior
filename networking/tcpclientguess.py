#!/usr/bin/python

import socket
import sys

sock = socket.socket(2, 1)
sock.connect((sys.argv[1], int(sys.argv[2])))

while True:
    sock.send(raw_input('Guess: '))
    re = sock.recv(1024)
    print 'Server reply:', re, '\n'
    if re == 'Correct':
        break
