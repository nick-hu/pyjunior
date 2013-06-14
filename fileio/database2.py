#!/usr/bin/python

with open('database.txt') as data:
	if data.readline() == '': tbook = {}
	else: 
		data.seek(0)
		exec data.readline()

while True:
	act = raw_input('\nAdd(a)/Delete(d)/Find(f)/Quit(q): ')
		
	if act == 'a':
		aname = raw_input('\nEnter name to add: ')
		anumb = raw_input('Enter number to add: ')
		tbook[aname] = anumb
	
	elif act == 'd':
		dname = raw_input('\nEnter name to delete: ')
		if dname in tbook: del tbook[dname]
		else: print 'Error: Name not in database'
	
	elif act == 'f':
		fname = raw_input('\nEnter name to find: ')
		if fname in tbook: print fname + "'s number is:", tbook[fname]
		else: print 'Error: Name not found'
		
	else: 
		print '\n'
		break
		
	with open('database.txt', 'w') as data:	
		data.write('tbook = ' + repr(tbook))
