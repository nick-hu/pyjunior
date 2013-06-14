#!/usr/bin/python

from string import *

s = raw_input('Enter a sentence:')	
v = 0

for let in s:
	if let in 'AaEeIiOoUu':
		v = v+1

print 'There are', len(split(s)), 'words in the sentence.'
print 'There are', v, 'vowels in the sentence.'
