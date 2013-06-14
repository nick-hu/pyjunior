#!/usr/bin/python

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Automatically bound to a random unused port: an ephemeral port

while True:
    try:
        line = raw_input()
        conn.sendto(line, ('', 3334))
    except EOFError:
        conn.sendto('\x00', ('', 3334))
        break

print 'Connection ended'
