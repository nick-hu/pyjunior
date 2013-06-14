#!/usr/bin/python

import sys
import string

normchars = string.ascii_letters + string.digits + string.punctuation

with open(sys.argv[1]) as f:
	norm = f.read()

with open(sys.argv[1], 'w') as f:
	for char in norm:
		if sys.argv[2] == 'e':
			if char in normchars: f.write(chr(ord(char)+1))
			else: f.write(char)
		elif sys.argv[2] == 'd':
			if char in normchars: f.write(chr(ord(char)-1))
			else: f.write(char)				
