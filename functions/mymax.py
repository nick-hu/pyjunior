#!/usr/bin/python

def mymax(x):
	tempmax = x[0]
	for i in x:	
		if i > tempmax: tempmax = i
	return tempmax
		
print mymax([9,11,7,2,99,5,99,99.5])
