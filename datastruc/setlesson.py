#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Sets are unordered and unindexable!'''

A = set([1,2,2,3,4])
B = set([3,4,5,5,6])

print 'Set A:', A
print 'Set B:', B, '\n'

print A-B # elements in complement of A, A ∖ B
print B-A # elements in complement of B, B ∖ A
print A|B # elements in union of A and B, A ∪ B
print A&B # elements in intersection of A and B, A ∩ B
print A^B # elements in symmetric difference of A and B, (A∖B)∪(B∖A)
		# ^ can also be written (A∪B)-(A∩B)

C = set([1,2])
D = set([1,2,3,4])

print C <= A # tests if C is a subset of A, C ⊆ A
print D >= A # tests if A is a subset of D, D ⊇ A
print C < A # tests if C is a proper subset of A, C ⊊ A
print D > A # tests if A is a proper subset of D, D ⊋ A
