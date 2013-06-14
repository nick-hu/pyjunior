#!/usr/bin/python

def shuffle(s1,s2):
	s = ''
	for let in range(len(s1)):
		s = s + s1[let] + s2[let]
	return s

a = '123456'
b = 'abcdef'
print shuffle(a,b)
