#!/usr/bin/python

import socket, sys

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(('localhost', int(sys.argv[1])))
data, send = '', ''

while data != 'quit' and send != 'quit':
	data, addr = conn.recvfrom(1024)
	print addr
	print '<' + addr[0] + ':' + str(addr[1]) + '>', data
	
	send = raw_input('>>> ')
	conn.sendto(send, addr)
