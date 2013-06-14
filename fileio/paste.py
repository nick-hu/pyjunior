#!/usr/bin/python

import sys

with open(sys.argv[1]) as f1:
	l1 = f1.readlines()
with open(sys.argv[2]) as f2:
	l2 = f2.readlines()

for line in zip(l1, l2):
	print line[0].strip() + ' ' + line[1],
