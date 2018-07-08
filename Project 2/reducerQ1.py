import sys

currentpath = None
pagecount=0

for line in sys.stdin:
    newpath = line.strip().split("")
    if len(newpath) != 1:
        # Something has gone wrong. Skip this line.
        continue
    if currentpath and currentpath!= newpath:
      print "{0}\t{1}".format(currentpath,pagecount)
      pagecount=0

    currentpath=newpath
    pagecount+= 1

    if currentpath!=None:
      print "{0}\t{1}".format(currentpath,pagecount)