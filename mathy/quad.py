#!/usr/bin/python

def quad(a,b,c):
	x1 = ((-1*(b)+(b**2-4*a*c)**0.5)/(2*a))
	x2 = ((-1*(b)-(b**2-4*a*c)**0.5)/(2*a))
	return x1, x2

a = float(raw_input('a: ')); b = float(raw_input('b: ')); c = float(raw_input('c: '))

if b**2-4*a*c < 0:
	print 'No real roots :('
else:
	print 'Root(s): x=', quad(a,b,c)

