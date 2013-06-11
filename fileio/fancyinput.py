#!/usr/bin/python

import sys

with open('stuff.txt', 'w') as f:
	f.writelines(sys.stdin.readlines())
