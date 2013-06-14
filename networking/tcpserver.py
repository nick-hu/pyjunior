#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# To reuse the same port

sock.bind(('', int(sys.argv[1])))
# localhost for one computer, 0.0.0.0 for multiple computers
sock.listen(1)
conn, addr = sock.accept()  # Blocks
print 'Connection accepted from', addr[0] + ':' + str(addr[1]) + '\n'
data = conn.recv(1024) * 2
print '[' + addr[0] + ':' + str(addr[1]) + ']', data

raw_input()
conn.send(data)  # or sock.sendall
conn.close()
