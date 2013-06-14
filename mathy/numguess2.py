#!/usr/bin/python

g = 50; hg = 25; n = 1

while True:
	print "Python's guess is:", g
	x = raw_input('Lower(l)/Higher(h)/Correct(c):')
	if x == 'h':
		g = g+hg
		hg = int(25/(2**n))
		if hg == 1: hg = 2
		elif hg == 0: hg = 1

		
	elif x == 'l':
		g = g-hg
		hg = int(25/(2**n))
		if hg == 1: hg = 2
		elif hg == 0: hg = 1
		
	else: break
	
	n = n+1
	
print "Python's guess", g, "was correct! It wins! Number of guesses:", n
