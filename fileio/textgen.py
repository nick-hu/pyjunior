#!/usr/bin/python

import random, string

char = int(raw_input('Enter number of characters to generate: '))
while True:
	f = raw_input('Enter file name: ')
	try: 
		doc = open(f,'w')
		break
	except: pass

print 'Generating...'

for x in xrange(char):
	w = random.choice(string.printable)
	doc.write(w)
	if x/float(char)*100 % 5 == 0: 
		print str(int(x/float(char)*100))+'% done...'

print 'Done!' 
