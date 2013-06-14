#!/usr/bin/python

def vcount(s):
	c = 0
	for let in s:
		if let in 'aeiouAEIOU':
			c = c+1
	return c
	
f = open('names.txt')
L = f.readlines()
M = sorted(L, key = vcount)
for i in M: print i,
