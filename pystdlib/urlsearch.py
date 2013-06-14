#!/usr/bin/python

import urllib as url
import sys

search, links, alert = ['<a href'] + sys.argv[1:], [], False
trans = {'<br>': '', '&quot;': '"'}

for line in url.urlopen('http://vancouver.en.craigslist.ca/zip/'):
	if all([s in line.lower() for s in search]):
		links.append(line[line.find('http://'):line.find('.html') + 5])
	
for link in links[1:]:
	for line in url.urlopen(link):
		for i in trans: line = line.replace(i, trans[i])
		if 'class="postingtitle"' in line:
			print '\033[1m' + line[line.find('>') + 1:line.find('</')]
		if '</section>' in line and alert: alert = False
		if alert: print '\033[0m' + line.strip()
		if 'id="postingbody"' in line: alert = True
	print '\n'
