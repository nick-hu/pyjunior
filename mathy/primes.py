#!/usr/bin/python

lim = int(raw_input('Find primes up to:'))

for num in xrange(2,lim+1): 
	for fac in xrange(2,int(num**0.5)+1):
		if num % fac == 0:
			break
	else:
		print num

# Note! xrange does not generate a list, wheras range does
