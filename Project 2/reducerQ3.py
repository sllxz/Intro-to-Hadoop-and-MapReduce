import sys

mostpoppath=None
mostpopN=0

currentpath=None
currentN=0

for line in sys.stdin:
    pathname = line.strip().split()
    if len(pathname) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if currentpath and currentpath!= pathname:
      if currentN>mostpopN:
        mostpoppath=currentpath
        mostpopN=currentN

      currentN=0

    currentpath=pathname
    currentN+= 1

print "{0}\t{1}".format(mostpoppath,mostpopN)