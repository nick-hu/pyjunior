#!/usr/bin/python

n = int(raw_input('Enter a number:'))
fact = 1
for x in range(1,n+1):
	fact = fact*x
print n, '! is equal to', fact, '.'
