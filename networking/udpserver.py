#!/usr/bin/python

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_ : Address Family
# INET: IPv4 addresses, SOCK_DGRAM: UDP datagrams
# (INET6: IPv6 addresse, SOCK_STREAM: TCP)
conn.bind(('', 3334))  # Bind to port 1234 to receive

while True:
    data, addr = conn.recvfrom(1024)  # This line blocks (i.e. waits)
    # addr is the address in a tuple of (address, port)
    if data[0] == '\x00':
        break
    print addr[0] + ':' + str(addr[1]), 'says:\n', data, '\n'

print 'Connection ended'
