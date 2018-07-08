import sys

salesDOW = [0] * 7
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        weekday, sale = data
        salesDOW[weekday] += float(sale)

for weekday, sales_total in enumerate(salesDOW):
    print "{0}\t{1}".format(weekday, sales_total)