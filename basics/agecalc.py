running = True
n = raw_input('Hello! I am Python. What is your name?')
print 'Hello,', n, '. I am going to calculate how old you are and how many days you have been alive. Please input the following information:'

while running:
	m = int(raw_input('Please enter the current month:'))
	y = int(raw_input('Please enter the current year:'))
	bm = int(raw_input('Please enter your month of birth:'))
	by = int (raw_input('Please enter your year of birth:'))
	print 'You are', (((y-by)*365)+((m-bm)*30))/365, 'years old.'
	if m >= bm:
		print 'You have been alive for approximately', ((y-by)*365)+((m-bm)*30), 'days.'
	if m < bm:
		print 'You have been alive for approximately', ((y-by-1)*365)+((m-bm)*30), 'days.'
	a = raw_input('Do you want to do this again?')
	if a == 'yes':
		running = True
	elif a == 'no':
		running = False
	c = raw_input('Do you want to see me list multiples of a number up to 1000?')
	if c == 'yes':
		q = int(raw_input('Multiples of what number?'))
		for i in range (q,1001,q):
			print i,
	if c == 'no':
		continue
	
print 'Well, goodbye', n, '!'









