#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
	for line in f.readlines()[-1::-1]:
		print line,
