#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
	print('Expected format: strip.py [file]')
	sys.exit(1)

lines = []
with open(sys.argv[1]) as old:
	lines = old.readlines()
	if lines[6].find('style.css') != -1:
		print('File {} already stripped'.format(sys.argv[1]))
		sys.exit(2)

with open(sys.argv[1], 'w') as new:
	new.writelines(lines[0:6]+['\t\t\t<link rel="stylesheet" href="../style.css">\n']+lines[260:-1])
