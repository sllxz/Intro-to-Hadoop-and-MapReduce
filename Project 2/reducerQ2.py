import sys

currentip = None
pagecount=0

for line in sys.stdin:
    newip = line.strip().split()
    if len(newip) != 1:
        # Something has gone wrong. Skip this line.
        continue
    if currentip and currentip!= newip:
      print "{0}\t{1}".format(currentip,pagecount)
      pagecount=0

    currentip=newip
    pagecount+= 1

    if currentip!=None:
      print "{0}\t{1}".format(currentip,pagecount)