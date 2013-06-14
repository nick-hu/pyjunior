#!/usr/bin/python

s = raw_input('Enter a sentence:')
w = 1
prev = ''

for let in s:
	if prev != ' ' and let == ' ':
		w = w+1
	prev = let
	
if sen[-1] == ' ':
	w = w-1

print 'There are', w, 'words in the sentence.'
