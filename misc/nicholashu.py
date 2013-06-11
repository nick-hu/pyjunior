#!/usr/bin/python

sen = raw_input(); n = 0

for word in sen.split():
	if len(word) == 3: n = n+1

print n
