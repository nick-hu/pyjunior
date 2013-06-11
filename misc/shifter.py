#!/usr/bin/python

import sys

queue = [char for char in sys.argv[1]]
for rot in range(len(queue)):
	print ''.join(queue)
	queue.append(queue.pop(0))
