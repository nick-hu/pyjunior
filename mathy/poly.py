#!/usr/bin/python

def factor(coef):
	const = int(coef[-1])
	posfacc = []
	facc = []
	for n in range(1,const+1):
		if const % n == 0:
			posfacc.append(n)
	for n in posfacc:
		facc.append(n)
		facc.append(-1*n)
	for n in facc:
		val = 0
		for exp in range(len(coef),-1,-1):
			if exp == 0:
				val = val + n
			else:
				val = val + n**exp
		if val == 0:
			break
	
	

coef = []

dpx = int(raw_input('Enter the degree of P(x):'))
for x in range(dpx,-1,-1):
	print 'x ^', x, ':'
	n = int(raw_input())
	coef.append(n)
 
factor(coef)
