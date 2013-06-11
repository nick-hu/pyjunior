#!/usr/bin/python

import sys

with open(sys.argv[2]) as f:
	for line in f.readlines():
		if sys.argv[1] in line: print line,
