#!/usr/bin/python

import sys
from decimal import Decimal, getcontext

pi, denom = Decimal('4'), Decimal('3')
add = False
count = 1
		
getcontext().prec = int(raw_input('Precision: '))

while True:
	sys.stdout.write('Pi = ' + str(pi) + '\t' + str(count) + '\r')
	sys.stdout.flush()
	if add: 
        pi = pi + (Decimal('4')/denom)
	else: 
        pi = pi - (Decimal('4')/denom)
	denom = denom + Decimal('2')
	add = not add
	
	count = count + 1
