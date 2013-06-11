#!/usr/bin/python

import socket, select, sys, time

bindport = int(raw_input('Bind port: '))
sendip = raw_input('Send IP: ')
sendport = int(raw_input('Send port: '))

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(('', bindport))
conn.settimeout(2.0)

while True:
	rlist, wlist, elist = select.select([sys.stdin, conn], [conn], [])
	
	for s in rlist:
		if s == conn:
			data, addr = conn.recvfrom(1024)
			if data.startswith('\x00'):
				print '\nConnection ended'
				break
			print '[' + str(addr[0]) + ':' + str(addr[1]) + ']', data
	
		elif s == sys.stdin:
			try: 
				line = raw_input('')
				conn.sendto(line, (sendip, sendport))
			except EOFError:
				conn.sendto('\x00', (sendip, sendport))
				break

	time.sleep(0.5)
