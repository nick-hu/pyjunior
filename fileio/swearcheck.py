#!/usr/bin/python

s = raw_input('Enter your message: '); l = []

for w in s.split():
	if len(w) == 4:
		l.append('****')
		continue
	l.append(w)

print ' '.join(l)	
