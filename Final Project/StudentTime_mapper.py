#!/usr/bin/python
import sys, csv, string

#Student Time Exercise


reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for line in reader:
	if len(line) == 1a9:
		hour = int(line[8][11:13])
		author_id = line[3]
		print "{0}\t{1}".format(author_id, hour)