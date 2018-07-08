#!/usr/bin/python
import sys
import csv

#create writer object
writer = csv.writer(sys.stdout,delimiter='\t')

#skip the header
reader.next()

for line in csv.reader(sys.stdin,delimiter='\t'):
 	 #if it is part of forum_users, which has 5 lines
     if len(data) == 5:
        writer.writerow([line[0]]+['A']+line[1:])

     # if part of forum_node, which has 19 lines
 	  elif(line) ==19:
 	  writer.writerow([line[3]]+['B']+line[:3]+line[5:10])