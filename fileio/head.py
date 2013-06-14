#!/usr/bin/python

import sys

with open(sys.argv[2]) as f:
	for line in range(int(sys.argv[1])):
		print f.readline(),
