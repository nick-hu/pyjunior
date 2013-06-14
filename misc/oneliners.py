#!/usr/bin/python

# Factorial
print reduce(lambda x, y: x*y, xrange(1, int(raw_input()) + 1))

# Primes
print [x for x in xrange(2, int(raw_input())) if all(x % n != 0 for n in xrange(2, int(x**0.5) + 1))]
 
# Alphabet
print [chr(n) for n in xrange(65, 91)]
