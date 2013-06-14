moreitems = True
running = True

while running:
	print 'Welcome to the Shopping Assistant v1.0'
	print 'Please enter your items:'
	a = raw_input('')
	shoplist = [a]
	while moreitems:
		q = raw_input('Another item?')
		if q == 'yes':
			moreitems = True
			i = raw_input('')
			shoplist.append(i)
		else:
			moreitems = False
			shoplist.sort()
	delimiter = ', '
	print 'You must purchase', len(shoplist), 'items:', delimiter.join(shoplist)

	print "Now it's time to buy the items. Once bought enter the item number (0 is the 1st item, 1 is the 2nd item, etc.)."
	moreitems = True
	while moreitems:
		b = int(raw_input(''))
		bitem = shoplist [b]
		del shoplist[b]
		print 'You bought the', bitem, '. You still need to buy:', delimiter.join(shoplist)
		if len(shoplist) == 0:
			moreitems = False
		else:
			moreitems = True

	print 'Congratulations! You completed your shopping!'
	r = raw_input('Shop again?')
	if r == 'yes':
		running = True
		moreitems = True
	else:
		running = False
		print 'Goodbye!'
