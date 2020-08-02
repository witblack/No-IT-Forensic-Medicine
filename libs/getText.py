#!/usr/bin/python
value = raw_input('Do you want check update for "python" package? [y/n]: ')
if str.lower(value) == 'y' or str.lower(value) == 'yes':
	exit(0)
else:
	exit(1)
