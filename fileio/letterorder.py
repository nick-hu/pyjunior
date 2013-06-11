#!/usr/bin/python

text = str(open('textsample.txt').readlines()).lower()
lets = set(l for l in text if l in 'abcdefghijklmnopqrstuvwxyz')

freq = sorted([(text.count(l), l) for l in lets], reverse=True)
freq = [(freq[n][1], freq[n][0]) for n in range(len(freq)) if n < 10]

print 'The top 10 most popular letters are:\n'
for let in freq:
    print let[0], '('+str(let[1])+')'
