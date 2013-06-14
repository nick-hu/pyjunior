#!/usr/bin/python

import sys
import string

with open(sys.argv[3]) as f:
	for line in f:
		print string.replace(line, sys.argv[1], sys.argv[2]),
