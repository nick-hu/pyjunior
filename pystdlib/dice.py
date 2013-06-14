#!/usr/bin/python

import random
import time

while True:
	time.sleep(0.5)
	a = random.randrange(1,7)
	b = random.randrange(1,7)
	print a, '|', b
	print 'Sum =', a+b
