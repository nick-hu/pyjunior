#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
	l = f.read().split()
	ppl = [(l[i], int(l[i+1])) for i in range(0, len(l), 2)]

with open(sys.argv[2], 'w') as newf:
	for person, age in sorted(ppl, key = lambda pair: pair[1]):
		newf.write(person + ' ' + str(age) + '\n')
