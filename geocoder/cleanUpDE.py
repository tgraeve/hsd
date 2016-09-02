# This python file uses the following encoding: utf-8

import csv

ifile = open('db/DE.tab', "r")
reader = csv.reader(ifile, delimiter='\t')

ofile = open('DE_cleanedUp.tab', "wb")
writer = csv.writer(ofile, delimiter='\n', quoting= csv.QUOTE_NONE)

for row in reader:
	if (row[4] not in "" and row[5] not in "" and row[9] not in "" and row[12] not in ("", "Gemeinde", "Ortsteil")):
		newRow = row[3].lower() + "\t" + row[4] + "\t" + row[5] + "\t" + row[9] + "\t" + row[12]
		writer.writerow([newRow])

print "---cleanUpDE.py FINISHED---"