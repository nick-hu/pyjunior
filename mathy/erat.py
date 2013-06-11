#!/usr/bin/python

lim = int(raw_input('Find primes up to:'))

nums = []

for n in range(2,lim+1): # Start with all the numbers
	nums.append(n)

for k in range(2,int(lim+1**0.5)): # Sieve
	m = 0
	mul = 2
	while m < lim+1:
		m = k
		m = m*mul
		try:
			nums.remove(m)
		except:
			pass
		mul = mul+1

print nums

