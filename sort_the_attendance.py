import os
from datetime import date

today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
lines_seen = set() # holds lines already seen
outfile = open(str(d1)+"attendance.txt", "w")
for line in open("att.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
os.remove("temp_attendance.csv")
