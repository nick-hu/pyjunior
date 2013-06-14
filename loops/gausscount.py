t = 0
s = int(raw_input('Enter a start number:'))
e = int(raw_input('Enter an end number:'))
for n in range(s,e+1):
	t = t+n
print 'The sum of all numbers from', s, 'to', e, 'is:', t
