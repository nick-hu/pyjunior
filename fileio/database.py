#!/usr/bin/python

import cPickle

with open('database.txt') as data:
	if data.readlines() == []: tbook = {}
	else: 
		data.seek(0)
		tbook = cPickle.load(data)

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
		fname = raw_input('\nEnter name substring to find: ')
		found = False
		for name in tbook:
			if fname in name:
				found = True
				print name + '\'s number is:', tbook[name]
		if not found: print 'Error: Name not found'
	
	else: 
		print '\n'
		with open('database.txt', 'w') as data:	
			cPickle.dump(tbook, data)
		break
