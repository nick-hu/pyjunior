t = 0
x = 0
while True:
	n = float(raw_input('Enter a number:'))
	x = x+1
	t = t+n
	if n == 0:
		x = x-1
		break
print 'The average is:', t/x
