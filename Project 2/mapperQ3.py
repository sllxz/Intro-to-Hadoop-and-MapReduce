import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip_address, identity, username, datetime, timezone, method, path, proto, status, size = data
        cleanpath=re.sub(r"^http://wwww.the-associates.co.uk",'',path)
        print cleanpath