import string
while True:
	s = raw_input(':')
	x = string.lower(s)
	if x == 'simon says stop' or x == 'the end':
		break
	else:
		print s
