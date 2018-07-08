import sys

salesTotal = 0
salesN_Total=0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    store, sale = data
    salesTotal += float(sale)
    salesN_Total+= 1

 print "{0}\t{1}".format(salesTotal,salesN_Total)