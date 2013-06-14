#!/usr/bin/python

def ispal(x):
	if x [::-1] == x:
		return True
	return False
		
print ispal('ogopogo')
print ispal('hello')
