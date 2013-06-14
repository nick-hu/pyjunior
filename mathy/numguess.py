#!/usr/bin/python

from random import *

min = int(raw_input('Guess from: '))
max = int(raw_input('Guess to: '))
x = randrange(min,max+1)
n = 1

while True:
	g = int(raw_input('Guess: '))
	if g < x:
		print 'Higher!'
	elif g > x:
		print 'Lower!'
	else:
		break
	n = n+1

print 'Congratulations, you win! Number of guesses:', n
