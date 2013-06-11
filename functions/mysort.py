#!/usr/bin/python

def findmin(seq):
	m = seq[0]
	for i in seq:
		if i < m: m = i
	return m
	
def mysort(seq):
	sseq = []
	while len(seq) > 0:
		sseq.append(findmin(seq))
		seq.remove(findmin(seq))
	return sseq

print mysort([6,2,8,2,1,5,8])
