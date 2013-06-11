#!/usr/bin/python

import socket
import sys

sock = socket.socket(2, 1)
sock.setsockopt(1, 2, 1)
sock.bind(('', int(sys.argv[1])))

sock.listen(1)
conn, addr = sock.accept()

while True:
    print '\nClient guess:', conn.recv(1024)
    re = raw_input('Reply: ')
    conn.send(re)
    if re == 'Correct':
        break
conn.close()
