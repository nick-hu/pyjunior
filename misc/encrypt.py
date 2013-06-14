#!/usr/bin/python

import sys
import string

def encode(n): 
	s = ''
	for x in bin(n)[2:]:
		if x == '0': s = s + '\0'
		else: s = s + '\t'
	return s + '\v'

def decode(s):
	news = '0b'
	for c in s:
		if c == '\x00': news = news + '0'
		if c == '\t': news = news + '1'
	return chr(int(news, 2))

normchars = string.ascii_letters + string.digits + string.punctuation

with open(sys.argv[1]) as f:
	words = f.read().split(' ')

with open(sys.argv[1], 'w') as f:
	if sys.argv[2] == 'e':
		for word in words:
			for char in word:
				f.write(encode(ord(char)))
			f.write(' ')

	elif sys.argv[2] == 'd':
		for word in words[:-1]:
			for char in word.split('\v')[:-1]:
				f.write(decode(char))
			f.write(' ')
