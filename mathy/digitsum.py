#!/usr/bin/python

from math import log10

def digitsum(n):
	tot = 0
	for i in xrange(int(log10(n)), -1, -1):  # Length of number
		d = n / (10**i)  # Get first digit
		n = n - d * 10**i  # Remove first digit
		tot = tot + d  # Add first digit value to total
	return tot

def digitsumstr(n):
	return sum(int(i) for i in str(n))

print digitsum(123)
print digitsum(200)
