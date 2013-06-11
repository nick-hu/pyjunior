#!/usr/bin/python

from random import *

def isin(x,lst):
	for item in lst:
		if x == item:
			return True
	return False

l = []; c = 1

while c < 20:
	num = (randrange(10,100))
	if isin(num,l):
		continue
	l.append(num)
	c += 1

print l

'''
while count<21:
	num = (randrange(10,100))
	if num in nums:
		continue
	nums.append(num)
	count = count+1

print nums
'''
