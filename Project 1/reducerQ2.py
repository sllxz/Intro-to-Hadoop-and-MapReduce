import sys

salesmax = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
      print oldKey, "\t", salesmax
      oldKey = thisKey
      salesmax = 0

    if float(thisSale)<=salesmax:
      continue

     oldKey = thisKey
     salesmax = float(thisSale)

 if oldKey != None:
   print oldKey, "\t", salesmax