#!/usr/bin/python

import subprocess as sub
import time

def filt(i):
	if ppl[i] not in ignore: return True
	return False 

name = raw_input('Name: ')
freq = float(raw_input('Frequency of check: '))
ignore = ['root']
ignore.append(name)

while True:
	check = sub.Popen(['who'], stdout = sub.PIPE)
	ppl = check.communicate()[0].split()
	ipl = set([ppl[i] for i in range(len(ppl)) if i%5 == 0 and filt(i)])
	disp = 'Intruder ALERT!: '
	t = '\t As of: ' + time.strftime('%H:%M:%S', time.localtime())
	for i in ipl: disp = disp + i + ', '
	if len(ipl) == 0: print '\033[32mNo intruders\033[0m' + t
	else: print '\033[31;1m' + disp + '\033[0m' + t
	time.sleep(freq)
