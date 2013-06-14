#!/usr/bin/python

import sys
import textwrap

with open(sys.argv[2]) as f:
	s = f.read()
	for line in textwrap.wrap(s, int(sys.argv[1])):
		print line
