#!/usr/bin/python

import random

d = dict([(chr(c),random.randint(1,100)) for c in range(65,91)])

for k, v in sorted(d.items(), key = lambda i: i[1]):
	print k, v
