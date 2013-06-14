import string
s = raw_input(':')
x = string.lower(s)
while x!= 'simon says stop' and x!= 'the end':
	print s
	s = raw_input(':')
	x = string.lower(s)


