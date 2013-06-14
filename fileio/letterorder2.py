#!/usr/bin/python


def foo(k):
    return d[k]

text = 'abcddefghijklmnioqrstuvwxyz'
d = {}

for let in text:
    if let in d:
        d[let] = d[let]+1
    if let not in d:
        d[let] = 1

for i in sorted(d, key=foo, reverse=True):
    print i, d[i]
