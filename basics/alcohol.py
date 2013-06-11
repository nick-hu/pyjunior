running = True

while running:
	n = raw_input('Hello! I am Python. What is your name?')
	print 'Hello,', n, '. I am going to see if you are old enough to purchase alcohol.'

	a = float(raw_input('How old are you?'))
	if a<1:
		print 'You are not born yet,', n, ',so you cannot purchase alcohol.'
	elif a<19:
		print 'Sorry,', n, ',you are too young to purchase alcohol.'
	elif a<120:
		print 'You are old enough to purchase alcohol,', n, '.'	
	else:
		print 'You are dead,', n, ',so you cannot purchase alcohol.'
	
	r = raw_input('Do you want to test again?')
	if r == 'yes':
		running = True
	else:
		running = False
	
print 'Goodbye,', n, '!'
		
	
	
	

		
		
