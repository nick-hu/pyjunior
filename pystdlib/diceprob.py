#!/usr/bin/python

from random import *
from time import *

data = []
rolls = int(raw_input('Number of rolls:'))

for roll in range(1,rolls+1):
	a = randrange(1,7)
	b = randrange(1,7)
	data.append(a+b)

print '|', data.count(2),'|', data.count(3),'|', data.count(4),'|', data.count(5),'|', data.count(6),'|', data.count(7),'|', data.count(8),'|', data.count(9),'|', data.count(10),'|', data.count(11),'|', data.count(12)
print 'Done!(', clock(), 's )'
