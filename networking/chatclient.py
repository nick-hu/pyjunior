#!/usr/bin/python

import socket, sys

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data, send = '', ''

while data != 'quit' and send != 'quit':
	send = raw_input('>>> ')
	conn.sendto(send, (sys.argv[1], int(sys.argv[2])))
	
	data, addr = conn.recvfrom(1024)
	print '<' + addr[0] + ':' + int(addr[1]) + '>', data
