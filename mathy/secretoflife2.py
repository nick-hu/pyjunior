#!/usr/bin/python

import time
prev2 = 0
prev = 1

while True:
	time.sleep(0.5)
	print prev2
	prev2, prev = prev, prev2+prev
