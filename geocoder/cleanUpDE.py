# This python file uses the following encoding: utf-8

import csv

ifile = open('db/DE.tab', "r")
reader = csv.reader(ifile, delimiter='\t')

ofile = open('DE_cleanedUp.tab', "wb")
writer = csv.writer(ofile, delimiter='\t', quoting= csv.QUOTE_NONE)

unsortedList = []

for row in reader:
	if (row[4] not in "" and row[5] not in "" and row[9] not in ("", "einwohner") and row[12] not in ("", "Gemeinde", "Ortsteil", "Amt")):
		newList = [row[3].lower(), row[4], row[5], int(row[9]), row[12]]
		unsortedList.append(newList)

sortedList = sorted(unsortedList, key=lambda x: -x[3])

for i in sortedList:
	writer.writerow(i)

print "---cleanUpDE.py FINISHED---"