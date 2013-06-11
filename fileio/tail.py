#!/usr/bin/python

import sys

with open(sys.argv[2]) as f:
	for l in f.readlines()[len(f.readlines())-int(sys.argv[1]):]:
		print l,
