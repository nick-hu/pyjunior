#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], int(sys.argv[2])))

sock.send(raw_input('Send: '))

data = sock.recv(1024)
print '[' + sys.argv[1] + ':' + sys.argv[2] + ']', data
