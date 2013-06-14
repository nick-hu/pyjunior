#!/usr/bin/python

def myrange(e, st = 1): # Function generator: ~ Equivalent to xrange
	s = 0
	while s < e:
		yield s # Suspends function (remembers where stopped)
		s = s + st

print sum(xrange(1000000)) # Less RAM consumed

l = [x**2 for x in range(6) if x % 2 == 1] # List comprehension
print l

foo = lambda x: x ** 2 # Equivalent to def foo(x): return x ** 2
print foo(2)
L = ['ba', 'dc', 'ab']
print sorted(L, key = lambda x: x[1])
len_int = lambda x: len(str(abs(x)))
print len_int(11)

