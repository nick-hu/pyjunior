#!/usr/bin/python

import sys

while True:
	try:
		n = int(raw_input('Enter an integer:'))
		k = int(raw_input('Enter an integer:'))
		assert n <= 1000000 and k <= 1000000
		try:
			print n, '/', k, '=', n/k
			break
		except:
			print 'Error: Division by zero!'
	except:
		print 'Error: Non-integer value / number is too large!'
